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
# This notebook demonstrates **key infrastructure patterns** for web scraping/API projects, including:
#
# - renting a cloud machine on Azure (run long scrapers without keeping your laptop on)  
# - scheduling scrapers with `cron` (automate daily/hourly data collection)  
# - saving full HTML responses (debug broken parsers and verify past results)  
# - writing cleaned data to CSV / JSONL (easy to inspect, share, and load)  
# - using SQLite for structured storage (query whether data was already collected)  
# - pushing files to Azure Blob Storage (centralized, durable storage for large outputs)  
# - tracking metadata (detect file growth, duplicate records, failed requests)  
# - sending notifications (get alerts when scrapes succeed or fail)  
# - managing environments with `virtualenv` / Docker (ensure reproducible code execution)  
# - keeping secrets in `.env` files (avoid leaking API keys in code or repos)  
#

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
# %pip install requests pandas python-dotenv 

# %% [markdown]
# ## 1. Renting a Virtual Machine on Azure
#
# Curious to run a scraping project on a virtual machine in the cloud? Try out any of the cloud providers (e.g., AWS, GCP, Azure). Below, we illustrate a workflow on Microsoft Azure (may require you to link your credit card).

# %% [markdown]
# ### How to Rent a Computer on Azure (Virtual Machine)
#
# 1. Log in to the [Azure Portal](https://portal.azure.com).  
# 2. Click **"Create a resource" → "Virtual Machine"**.  
# 3. Choose:
#    - Subscription + Resource Group  
#    - Region (e.g., West Europe)  
#    - VM image (e.g., Ubuntu 22.04 LTS if you're comfortable with the command line; if you're more used to Windows, choose Ubuntu Desktop)
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
# - clone your scraping repository
# - run your scraper, or use `cron` to schedule scraping jobs (see next)

# %% [markdown]
# ## 2. Scheduling with `cron`
#
# We show:
# - a simple Python script that does something (e.g., prints timestamp)  
# - an example `crontab` entry to run it periodically.

# %% [markdown]
# ### Example Python script
#
# Please save the snippet below as `run_scraper.py`.

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
# On your computer (e.g., VM, Mac/Linux; Windows users cannot use this implementation of Cron), run: 
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
# ### Overview about Cron syntax
#
# ```
# * * * * * command_to_run
# │ │ │ │ │
# │ │ │ │ └── Day of week (0–7)
# │ │ │ └──── Month (1–12)
# │ │ └────── Day of month (1–31)
# │ └──────── Hour (0–23)
# └────────── Minute (0–59)
# ```
#
# __Examples__
#
# * Run a script every day at 08:30
#   `30 8 * * * /usr/bin/python3 /path/script.py`
# * Run every 5 minutes
#   `*/5 * * * * /path/job.sh`
# * Run every Monday at midnight
#   `0 0 * * 1 /path/backup.sh`
# * `>> /home/username/scraper.log 2>&1` ensures that any (printed) output of your scripts is written to a file called `scraper.log`
#
# ### View your scheduled jobs
#
# ```bash
# crontab -l
# ```
#
# **Tip:** Always use **absolute paths** to files, commands, and environments when scheduling.
#

# %% [markdown]
# ## 3. Storing as CSV or JSON
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
# ## 4. Storing Full HTML
#
# We send a request to a page and store the **raw HTML** to disk.
# In practice, you’d loop over many URLs.

# %%
import os
import requests

os.makedirs("data/html", exist_ok=True)

url = "https://music-to-scrape.org"
response = requests.get(url)
response.raise_for_status()  # raise error if not 200

html_path = "data/html/example_com.html"
with open(html_path, "w", encoding="utf-8") as f:
    f.write(response.text)

print(f"Saved HTML from {url} to {html_path}")

# %% [markdown]
# ## 5. SQL with SQLite
#
# SQLite is:
# - file-based  
# - ships with Python (module `sqlite3`)  
# - good for small projects.

# %% [markdown]
# ### Setup
#
# Starting to use any database for a scraping project typically requires you to first define the type of database you would like to use. In essence, this boils down to
#
# - choosing a path where the SQLite database is to be located (here: `scraping.db`.
# - defining the tables that the data base should have (think of them like different Excel "sheets" in a workbook of multiple Excel sheets). Each table has
#     - a name (e.g., products)
#     - variables (e.g., `product_id`, `name`, `price`) and associated data types (`integer` for product IDs, `text` for product names, and floats (i.e., numbers with decimals) for prices, here encoded as `real`). SQL also supports "JSON" data that can be inserted in a column - here called `attributes`, and set to type `JSON`. The timestamp is encoding in `unixempoch`.
#     - primary keys (an "index" to each table, which will allow you rapidly search and combine different tables) - also "defines a unique row in this table" (therefore, it is mandatory). Here, the primary key is a so-called composite key, consisting of the product ID and the timestamp of when the data was collected (obviously, information for one product could be collected multiple times).
#     - (optional) foreign keys (similar to primary keys, to be used for optional merges

# %% [markdown]
# __Creating the database__

# %%
import sqlite3

db_path = "scraping.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create a simple table (if it doesn't yet exist)
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER,
        timestamp unixepoch,
        name TEXT,
        price REAL,
        attributes JSON,
        PRIMARY KEY (product_id, timestamp)
    )
    """
)
conn.commit()
conn.close()


# %% [markdown]
# __Using the database (store data)__
#
# During a scraping project, you then use the created database to insert data. The code below has a "dummy" function (`insert_one_product()`) that simulates "scraping" product information and inserting it into your database.

# %%
import sqlite3
import json
import time
import random

# Deterministic product catalog
PRODUCT_CATALOG = {
    1: "Apple AirPods",
    2: "Sony WH-1000XM4",
    3: "Samsung Galaxy Buds",
    4: "Bose QuietComfort",
    5: "JBL Live Pro"
}

def insert_one_product(db_path="scraping.db"):
    """Insert ONE deterministic product into the database."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Pick a product deterministically
    product_id = random.choice(list(PRODUCT_CATALOG.keys()))
    name = PRODUCT_CATALOG[product_id]

    # Dummy price + attributes
    price = round(random.uniform(50, 300), 2)
    attributes = {
        "battery_life": random.choice([10, 20, 30]),
        "color": random.choice(["black", "white", "silver"]),
        "wireless": True
    }

    timestamp = int(time.time())

    cursor.execute(
        """
        INSERT INTO products (product_id, timestamp, name, price, attributes)
        VALUES (?, ?, ?, ?, ?)
        """,
        (product_id, timestamp, name, price, json.dumps(attributes))
    )

    conn.commit()
    conn.close()

    print(f"Inserted product {product_id} – {name} at {timestamp}")



# %% [markdown]
# Now let's run your function!

# %%
duration = 10 # seconds
interval = 1 # pause between requests
db_path="scraping.db"

start = time.time()
while time.time() - start < duration:
    insert_one_product(db_path)
    time.sleep(interval)


# %% [markdown]
# __Fetching the data / exporting__
#
# After the job is "done", we can also export the data from SQLite back to JSON or CSV.

# %%
import json
import csv

db_path = "scraping.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Fetch back
cursor.execute("SELECT * FROM products")
rows = cursor.fetchall()

# Get column names (useful for JSON + CSV)
colnames = [desc[0] for desc in cursor.description]

conn.close()

print(f"Database path: {db_path}")
print("Rows in 'products' table:", rows)

# %% [markdown]
# __Write to JSON__

# %%
jsonl_path = "products.jsonl"
with open(jsonl_path, "w", encoding="utf-8") as f:
    for row in rows:
        row_dict = dict(zip(colnames, row))
        f.write(json.dumps(row_dict) + "\n")

print(f"Wrote JSONL to: {jsonl_path}")


# %% [markdown]
# __Write to CSV__

# %%
csv_path = "products.csv"
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(colnames)   # header
    writer.writerows(rows)

print(f"Wrote CSV to: {csv_path}")


# %% [markdown]
# ### Checking Whether Data Has Already Been Collected
#
# Before scraping or inserting new records, it’s useful to check whether a 
# product (or specific timestamp) is *already* stored in the database.  
# This prevents duplicate work and keeps the dataset clean.
#
# In the example below, we query the database to see whether a given 
# `product_id` already exists. If it does, we skip inserting it; if not, 
# we can safely proceed. This pattern is useful for incremental scraping, 
# daily updates, and idempotent data pipelines.

# %%
import sqlite3

def product_exists(product_id, db_path="scraping.db"):
    """Return True if the product_id already exists in the DB."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT 1 FROM products WHERE product_id = ? LIMIT 1",
        (product_id,)
    )
    exists = cursor.fetchone() is not None

    conn.close()
    return exists


# --- Example usage 1 ---
test_id = 3  # try any ID from your catalog

if product_exists(test_id): 
    print(f"Product {test_id} already exists → skip inserting.")
else:
    print(f"Product {test_id} not in DB → safe to insert.")


# --- Example usage 2 ---
test_id = 99  # try any ID not part of your catalog

if product_exists(test_id): 
    print(f"Product {test_id} already exists → skip inserting.")
else:
    print(f"Product {test_id} not in DB → safe to insert.")


# %% [markdown]
# ## 6. Using Azure Blob Storage
#
# To use Azure Blob Storage:
# - create a Storage Account + Blob Container  
# - get the **connection string** or **SAS token**  
# - store credentials in `.env` (see secrets section)  
# - use `azure-storage-blob` in Python.
#
# First, make sure you have the package installed.

# %%
# %pip install azure-storage-blob

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
#
# Before you can run the examples, let's just create a sample CSV file on our disk.

# %%
import random
import csv

csv_path = "random.csv"

with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "value"])                # header
    for _ in range(0,random.randint(1, 50)):
        writer.writerow([random.randint(1, 1000),       # one random row
                         random.choice(["foo", "bar", "baz"])])
        
print('Done writing!')

# %% [markdown]
# ### Example: Simple metadata for a scraped CSV

# %%
import os
import pandas as pd

file_stats = os.stat(csv_path)
file_size_bytes = file_stats.st_size

df = pd.read_csv(csv_path)
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
    "https://music-to-scrape.org/",
    "https://music-to-scrape.org/non-existent-page",
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
# Here we show a simple example using **Pushover**, see https://pushover.com. There are also open source variants, such as ntfy.sh.

# %% [markdown]
# ```bash
# # Code for illustration only
#
# import requests
#
# def notify(msg):
#     requests.post(
#         "https://api.pushover.net/1/messages.json",
#         data={
#             "token": "YOUR_APP_TOKEN",
#             "user": "YOUR_USER_KEY",
#             "message": msg
#         }
#     )
#
# notify("Scraper finished successfully!")
# ```

# %% [markdown]
# In practice, you might:
#
# - send a message when the scraper fails  
# - send a message when record counts drop to zero  
# - send a message when a new dataset is ready for analysis.

# %% [markdown]
# ## 9. Using `virtualenv` and Docker
#
# These tools help ensure **reproducible environments**.

# %% [markdown]
# ### Python: `virtualenv` (or `venv`)
#
# - Creates an isolated **Python package environment**
# - Ensures the same Python libraries are installed (e.g., `requests`, `pandas`)
# - Great for local development, teaching, and small scraping projects
# - But:
#   - Depends on your host system (OS, Python version)
#   - Can still break if someone has different system libraries
#
# **Good for:** simple, local reproducible scraping pipelines.
#
#
# __Example scripts to be executed on your command line/terminal__
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
# → same `requirements.txt` = same environment.

# %% [markdown]
# __Once your virtual environment is activated__ (`source .venv/bin/activate`), you can run your project.

# %% [markdown]
# __Other users__ can "install" the same environment on their machines:
#
# ```bash
# python3 -m venv .venv
# source .venv/bin/activate
# pip install -r requirements.txt
# ```

# %% [markdown]
# ### Docker 
#
# - Packages *everything* your scraper needs (inside a `Dockerfile`):
#   - Python version  
#   - System libraries (e.g., `libxml2`, SSL)  
#   - Python dependencies  
#   - Your scraping code  
# - Runs identically everywhere:
#   - macOS, Windows, Linux, servers, GitHub Actions, cloud
# - Eliminates “works on my machine”
# - Perfect for automation, cron jobs, and long-term reproducibility
#
# **Good for:** deployment, production, shared pipelines, research workflows that must be stable over time.
#
# #### Try it out
#
# 1. Install Docker  
# 2. Save the scraper below as `run_scraper.py`  
# 3. Use the Dockerfile to build a container  
# 4. Mount a host folder so scraped data appears **outside** the container
#
# __Example scraper (save as `run_scraper.py`)__
#
# ```python
# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime
# import os
#
# # Make sure output folder exists (inside the container)
# os.makedirs("output", exist_ok=True)
#
# html = requests.get("https://music-to-scrape.org").text
# soup = BeautifulSoup(html, "lxml")
# title = soup.title.string
#
# # Write results to a file
# timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
# filename = f"output/scrape_{timestamp}.txt"
#
# with open(filename, "w") as f:
#     f.write(f"Title: {title}\n")
#
# print("Wrote:", filename)
# ```
#
# __Dockerfile (save as `dockerfile`, without any extension)__
#
# ```bas
# FROM python:3.11-slim
#
# WORKDIR /app
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
#
# COPY . .
# CMD ["python", "run_scraper.py"]
#
# ```
#
# __Requirements with instructions which packages need to be installed (save as `requirements.txt`)__
#
# ```bash
# requests
# beautifulsoup4
# lxml
# ```
#
# __When done, you need to have the following project structure implemented__
#
# ```bash
# my-scraper/
# ├── Dockerfile
# ├── requirements.txt
# └── run_scraper.py
# ```
#
# You can then "compile" your Docker package and run it:
#
# ```bash
# docker build -t my-scraper .
# ```
#

# %% [markdown]
# #### Running the Scraper in Docker (with Mounted Output Folder)
#
# To run the scraper so that **all output files appear on your computer**, follow these steps:
#
# 1. Make sure your project contains:
# ```
# Dockerfile
# requirements.txt
# run_scraper.py
# ```
#
# 2. Build the Docker image:
# ```bash
# docker build -t my-scraper .
# ````
#
# 3. Create an output folder on your machine:
#    ```bash
#    mkdir -p scraper_output
#    ```
#    
# 4. Run the container and **mount** the folder:
#    ```bash
#    docker run --rm \
#      -v $(pwd)/scraper_output:/app/output \
#      my-scraper
#    ```
#
#    *(Windows PowerShell)*
#
#    ```powershell
#    docker run --rm `
#      -v ${PWD}/scraper_output:/app/output `
#      my-scraper
#    ```
#    
# 5. Result:
#    Scraped files appear on your machine in:
#
#    ```
#    scraper_output/
#    ```
#
# Mounting lets the scraper write results to your computer while still running inside a reproducible Docker container.
#

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
# Add `.env` to your `.gitignore` to avoid any of your secrets are committed to Git/GitHub:
#
# ```text
# # .gitignore
# .env
# ```

# %%
# create a dummy .env file
f = open('.env', 'w')
f.write('TEST_KEY=123456')
f.close()

# %% [markdown]
# ### Loading secrets with `python-dotenv`

# %%
from dotenv import dotenv_values

config = dotenv_values(".env")  # returns dict of variables
print("Loaded keys from .env:", list(config.keys()))

# %% [markdown]
# You can use `os.getenv("VAR_NAME")` after calling `load_dotenv()`.
#

# %%
load_dotenv()
os.getenv("TEST_KEY")

# %% [markdown]
#
# This keeps:
#
# - configuration separate from code  
# - secrets out of your repository  
# - different settings for development vs production

# %% [markdown]
# __How to use secrets with Docker?__
#
# Simply pass the `.env` file to docker when running a project. Your container then reads the secret with `os.getenv()` in Python, while the value itself never gets stored in the Docker image. Never hard-code any of your secret keys in your code.
#
# ```bash
# docker run --rm --env-file .env my-scraper
# ```
#
#

# %% [markdown]
# # Summary
#
# In this notebook we illustrated:
#
# - Renting a VM on Azure
# - Scheduling scraping jobs with `cron`  
# - Storing full HTML for reproducibility  
# - Saving data as CSV and JSON  
# - Using SQLite for structured storage  
# - Uploading files to Azure Blob Storage  
# - Tracking metadata (record count, file size, HTTP status codes)  
# - Sending notifications on completion/failure  
# - Using `virtualenv` / Docker for reproducible environments  
# - Managing secrets safely with `.env` files  
#
# You can use the code snippets in this notebook for your own scraping projects.
