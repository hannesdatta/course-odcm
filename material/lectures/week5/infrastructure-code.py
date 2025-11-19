# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.3
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Infrastructural Considerations
#
# This notebook accompanies the lecture and **demonstrates code patterns** for:
#
# - renting a computer on Azure (high-level, you demo UI)  
# - scheduling with `cron`  
# - storing full HTML  
# - storing data as CSV / JSON  
# - using SQLite for structured storage  
# - storing files on Azure Blob Storage  
# - tracking metadata (record counts, file size, HTTP status codes, volume changes)  
# - sending notifications  
# - using `virtualenv` / `renv` and Docker (at least conceptually)  
# - managing secrets with `.env` files

# %% [markdown]
# ## 0. Setup
#
# We will use a few common Python libraries:
#
# - `requests` for HTTP requests  
# - `pandas` for tabular data  
# - `sqlite3` (built-in) for SQLite databases  
# - `python-dotenv` to load secrets from a `.env` file  
# - `azure-storage-blob` for Azure Blob Storage
#
# You **don't** have to run this cell in class, but it shows students how they would set up the environment.

# %%
# !pip install requests pandas python-dotenv azure-storage-blob

# %% [markdown]
# ## 1. Renting a Computer on Azure (conceptual)
#
# You will **demo this live** in the Azure portal. Here we just document the steps in text so students can refer back later.

# %% [markdown]
# ### How to Rent a Computer on Azure (Virtual Machine)
#
# 1. Log in to the [Azure Portal](https://portal.azure.com).  
# 2. Click **"Create a resource" → "Virtual Machine"**.  
# 3. Choose:
#    - Subscription + Resource Group  
#    - Region (e.g., West Europe)  
#    - VM image (e.g., Ubuntu 22.04 LTS)  
#    - Size (number of vCPUs / RAM)  
# 4. Set authentication:
#    - SSH key (recommended) or password.  
# 5. Configure:
#    - Disk size  
#    - Networking (public IP, security group allowing SSH)  
# 6. Review + create.  
# 7. Connect via SSH:
#
# ```bash
# ssh username@YOUR_VM_IP_ADDRESS
# ```
#
# From there, you can:
#
# - install Python / R  
# - clone your scraping repo  
# - use `cron` to schedule scraping jobs.

# %% [markdown]
# ## 2. Scheduling with `cron`
#
# We show:
# - a simple Python script that does something (e.g., prints timestamp)  
# - an example `crontab` entry to run it periodically.

# %% [markdown]
# ### Example Python script: `run_scraper.py`

# %%
import datetime

def main():
    now = datetime.datetime.now().isoformat()
    print(f"[{now}] Running scraper... (placeholder)")
    # Here you would call your actual scraping functions

if __name__ == "__main__":
    main()

# %% [markdown]
# ### Example `crontab` entry
#
# On the Azure VM (or any Linux server), run:
#
# ```bash
# crontab -e
# ```
#
# Add a line like:
#
# ```bash
# # Run scraper every day at 02:00
# 0 2 * * * /usr/bin/python3 /home/username/run_scraper.py >> /home/username/scraper.log 2>&1
# ```
#
# This:
# - runs the script daily at 02:00  
# - appends output + errors to `scraper.log`  

# %% [markdown]
# ## 3. Storing Full HTML
#
# We send a request to a page and store the **raw HTML** to disk.
# In practice, you’d loop over many URLs.

# %%
import os
import requests

os.makedirs("data/html", exist_ok=True)

url = "https://example.com"
response = requests.get(url)
response.raise_for_status()  # raise error if not 200

html_path = "data/html/example_com.html"
with open(html_path, "w", encoding="utf-8") as f:
    f.write(response.text)

print(f"Saved HTML from {url} to {html_path}")

# %% [markdown]
# ## 4. Storing as CSV or JSON
#
# Assume we parsed some data (e.g., a list of products).  
# Here we simulate that with a small dictionary.

# %%
import pandas as pd

data = [
    {"product_id": 1, "name": "Widget", "price": 9.99},
    {"product_id": 2, "name": "Gadget", "price": 14.99},
]

df = pd.DataFrame(data)

os.makedirs("data/processed", exist_ok=True)

csv_path = "data/processed/products.csv"
json_path = "data/processed/products.json"

df.to_csv(csv_path, index=False)
df.to_json(json_path, orient="records", lines=True)

print(f"Saved CSV to {csv_path}")
print(f"Saved JSON to {json_path}")

# %% [markdown]
# ## 5. Setting Up SQLite and Storing Data
#
# SQLite is:
# - file-based  
# - ships with Python (module `sqlite3`)  
# - good for small/medium projects.

# %%
import sqlite3

db_path = "data/scraping.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create a simple table (if it doesn't yet exist)
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY,
        name TEXT,
        price REAL
    )
    """
)

# Insert our data (ignore conflicts for simplicity)
for row in data:
    cursor.execute(
        """
        INSERT OR REPLACE INTO products (product_id, name, price)
        VALUES (?, ?, ?)
        """,
        (row["product_id"], row["name"], row["price"]),
    )

conn.commit()

# Fetch back
cursor.execute("SELECT * FROM products")
rows = cursor.fetchall()
conn.close()

print(f"Database path: {db_path}")
print("Rows in 'products' table:", rows)

# %% [markdown]
# ## 6. Using Azure Blob Storage
#
# To use Azure Blob Storage:
# - create a Storage Account + Blob Container  
# - get the **connection string** or **SAS token**  
# - store credentials in `.env` (see secrets section)  
# - use `azure-storage-blob` in Python.

# %% [markdown]
# ### Example: Upload a File to Azure Blob

# %%
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

# Load secrets from .env
load_dotenv()  # looks for a `.env` file in current directory

connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container_name = os.getenv("AZURE_BLOB_CONTAINER", "scraping-data")

if connection_string:
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)

    # Create container if it does not exist
    try:
        container_client.create_container()
    except Exception:
        pass  # likely already exists

    # Upload our HTML file as an example
    blob_name = "html/example_com.html"
    with open(html_path, "rb") as data_stream:
        container_client.upload_blob(name=blob_name, data=data_stream, overwrite=True)

    print(f"Uploaded {html_path} to Azure Blob as {blob_name}")
else:
    print("AZURE_STORAGE_CONNECTION_STRING not set. Skipping Azure demo.")

# %% [markdown]
# ## 7. Metadata Tracking
#
# We track:
# - number of records  
# - file size  
# - HTTP status codes  
# - changes in volume over time  
#
# This is useful for **monitoring** scrapers and detecting breakage.

# %% [markdown]
# ### Example: Simple metadata for a scraped CSV

# %%
import os

file_stats = os.stat(csv_path)
file_size_bytes = file_stats.st_size
record_count = len(df)

metadata = {
    "filename": csv_path,
    "record_count": record_count,
    "file_size_bytes": file_size_bytes,
}

print(metadata)

# %% [markdown]
# In a real project you would:
#
# - append one such metadata record per scraping run to a log file or database  
# - plot `record_count` over time to detect sudden drops/spikes  
# - track average price, number of missing values, etc.

# %% [markdown]
# ### Example: Tracking HTTP Status Codes

# %%
urls = [
    "https://example.com/",
    "https://example.com/non-existent-page",
]

status_log = []
for u in urls:
    r = requests.get(u)
    status_log.append({"url": u, "status_code": r.status_code})

status_log_df = pd.DataFrame(status_log)
status_log_df

# %% [markdown]
# ## 8. Sending Notifications
#
# There are many options (email, Slack, Pushover, MS Teams, etc.).  
# Here we show a simple example using **email via SMTP** (conceptually).

# %%
import smtplib
from email.message import EmailMessage

def send_notification_email(subject: str, body: str, to_address: str):
    """
    Example email notification.
    Normally you would configure SMTP server details in your .env.
    """
    smtp_host = os.getenv("SMTP_HOST")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    smtp_user = os.getenv("SMTP_USER")
    smtp_pass = os.getenv("SMTP_PASS")

    if not all([smtp_host, smtp_user, smtp_pass]):
        print("SMTP settings missing; not sending email.")
        return

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = smtp_user
    msg["To"] = to_address
    msg.set_content(body)

    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)

    print(f"Notification email sent to {to_address}")

# Example usage (will only work if SMTP_* env variables are set):
send_notification_email(
    subject="[Demo] Scraper completed",
    body="The scraping job finished successfully.",
    to_address=os.getenv("NOTIFY_EMAIL", "you@example.com"),
)

# %% [markdown]
# In practice, you might:
#
# - send an email when the scraper fails  
# - send an email when record counts drop to zero  
# - send an email when a new dataset is ready for analysis.

# %% [markdown]
# ## 9. Using `virtualenv`, `renv`, and Docker (conceptual)
#
# These tools help ensure **reproducible environments**.
# We mainly show commands here; you demonstrate live in class.

# %% [markdown]
# ### Python: `virtualenv` (or `venv`)
#
# ```bash
# # create virtual environment
# python3 -m venv .venv
#
# # activate (macOS/Linux)
# source .venv/bin/activate
#
# # activate (Windows PowerShell)
# .venv\Scripts\Activate.ps1
#
# # install dependencies
# pip install -r requirements.txt
#
# # freeze current environment
# pip freeze > requirements.txt
# ```
#
# Students should understand:  
# → same `requirements.txt` = same environment.

# %% [markdown]
# ### R: `renv` (brief mention)
#
# In an R project:
#
# ```r
# install.packages("renv")
# renv::init()
# renv::snapshot()
# renv::restore()
# ```
#
# This pins package versions and makes the R environment reproducible.

# %% [markdown]
# ### Docker (very short)
#
# You may **show** (not deeply teach) the idea of a Dockerfile:
#
# ```dockerfile
# FROM python:3.11-slim
#
# WORKDIR /app
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
#
# COPY . .
# CMD ["python", "run_scraper.py"]
# ```
#
# Build and run:
#
# ```bash
# docker build -t my-scraper .
# docker run --rm my-scraper
# ```
#
# Message:  
# → same container = same environment everywhere (local, server, cloud).

# %% [markdown]
# ## 10. Managing Secrets with `.env`
#
# We **never** want secrets (API keys, passwords) hard-coded in code or committed to Git.
# Instead, we use a `.env` file and load it at runtime.

# %% [markdown]
# ### Example `.env` file
#
# ```text
# # .env (do NOT commit this to Git)
# AZURE_STORAGE_CONNECTION_STRING=DefaultEndpointsProtocol=...
# AZURE_BLOB_CONTAINER=scraping-data
# SMTP_HOST=smtp.example.com
# SMTP_PORT=587
# SMTP_USER=your_email@example.com
# SMTP_PASS=super-secret-password
# NOTIFY_EMAIL=team@example.com
# ```
#
# Add `.env` to your `.gitignore`:
#
# ```text
# # .gitignore
# .env
# ```

# %% [markdown]
# ### Loading secrets with `python-dotenv`

# %%
from dotenv import dotenv_values

config = dotenv_values(".env")  # returns dict of variables
print("Loaded keys from .env:", list(config.keys()))

# %% [markdown]
# You can use `os.getenv("VAR_NAME")` after calling `load_dotenv()` (as we did above for Azure + SMTP).
#
# This keeps:
#
# - configuration separate from code  
# - secrets out of your repository  
# - different settings for development vs production

# %% [markdown]
# # Summary
#
# In this notebook we illustrated:
#
# - Renting a VM on Azure (conceptual steps)  
# - Scheduling scraping jobs with `cron`  
# - Storing full HTML for reproducibility  
# - Saving data as CSV and JSON  
# - Using SQLite for structured storage  
# - Uploading files to Azure Blob Storage  
# - Tracking metadata (record count, file size, HTTP status codes)  
# - Sending notifications on completion/failure  
# - Using `virtualenv` / `renv` / Docker for reproducible environments  
# - Managing secrets safely with `.env` files  
#
# You can adapt this notebook to your own scraping projects and extend it with your real code.
