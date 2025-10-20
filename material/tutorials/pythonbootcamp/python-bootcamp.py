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
# # 1. Getting Started with Python and Web Scraping/APIs
#
# Welcome to your first Python session for Web Data, which consists of three sections.
#
# - In __section 1__, we’ll make sure you can run Python both locally and in the cloud, understand how Jupyter works, and get a first feel for the environment you’ll use throughout this course. 
# - In __section 2__, we go over basic programming concepts in Python. If you’ve used R or RStudio before, many things will feel familiar — just with slightly different syntax and a few new tricks. 
# - Finally, in __section 3__, we introduce you to web scraping and APIs, and applying some of the concepts covered in earlier sections.
#
# Let's get started!

# %% [markdown]
# ## 1.1 Why Python (and How to Run It)
#
# Python is one of the most widely used programming languages in data science.  
# We use it for everything from **web scraping** and **automation** to **machine learning** and **data visualization**.
#
# A few reasons why Python is such a good choice for us:
# - It’s open-source and completely free.
# - It’s used both in academia and industry.
# - It has fantastic documentation and community support.
# - It runs on Windows, Mac, and Linux — so everyone’s included.
#
# ---
#
# ### Working locally
#
# If you like having everything on your computer, the easiest way to install Python is through **Anaconda**.  
# It comes with both **Jupyter Notebook** and **Visual Studio Code (VS Code)**, which are the two main tools we’ll use.
#
# - Download Anaconda here: [anaconda.com/products/distribution](https://www.anaconda.com/products/distribution)  
# - Install it using the default settings.  
# - After installation, open either:
#   - **Jupyter Notebook** → great for step-by-step exploration.
#   - **VS Code** → great for bigger projects.
#
# ---
#
# ### Working in the cloud
#
# If you don’t want to install anything yet, that’s totally fine!  
# Just head over to [**Google Colab**](https://colab.research.google.com).  
# It runs notebooks directly in your browser and automatically saves them in your Google Drive.  
# You can follow all exercises there without setting up anything locally.

# %% [markdown]
# ## 1.2 Navigating the Command Line
#
# Before you open Jupyter, let’s quickly talk about the terminal (also called **command prompt**).  
# Think of it as a “text-based door” to your computer.  
# You’ll occasionally use it — for example, when installing packages or launching Jupyter.
#
# Here are a few basic commands:
#
# | Action | Windows | Mac/Linux |
# |:--|:--|:--|
# | Show current folder | `cd` | `pwd` |
# | Change directory | `cd folder_name` | `cd folder_name` |
# | Move up one level | `cd ..` | `cd ..` |
# | List files | `dir` | `ls` |
# | Clear the screen | `cls` | `clear` |
#
# These will come in handy later when we save our scraped data or navigate between project folders.

# %% [markdown]
# ## 1.3 Launching Jupyter Notebook or VS Code
#
# Once Anaconda is installed, you can start **Jupyter Notebook** in one of two ways:
#
# - Through the **Anaconda Navigator** app — click “Launch” next to Jupyter Notebook.  
# - Or by typing `jupyter notebook` in your terminal and pressing Enter.  
#
# Jupyter will open a new browser window showing your folders. From there, you can open existing notebooks or create new ones.  
# Each notebook is made up of “cells,” which can contain either **code** or **text**.
#
# ---
#
# Alternatively, if you’re using **VS Code**, simply open a folder and click **New File → Jupyter Notebook**.  
# It behaves the same way, but it’s a bit more powerful for larger projects.
#
# ---
#
# ### Exercise 1
#
# Let’s make sure everything runs properly.  
# Run the cell below — it should print a short message.  

# %%
# starter code (runs)
print("Hello, Python!")

# %% [markdown]
# **Explanation**  
# If you see “Hello, Python!” appear below the cell, everything works.  
# Each time you press **Shift + Enter**, Jupyter runs the active cell and shows the result below.  
# We’ll build on this in the next exercises.

# %% [markdown]
# ## 1.4 Installing and Importing Packages
#
# Python becomes truly powerful once you start using **packages** — small add-ons that provide extra functionality.
#
# For example:
# - `json` helps us work with web data and APIs.  
# - `csv` lets us read and write spreadsheets.  
# - `requests` lets us download web pages.
# - `pandas` lets you work with tables ("data frames" in `R`)
# - `beautifulsoup4` helps you structure website content for use with web scraping.
#
# You only need to *install* a package once (with `pip install ...`),  
# but you have to *import* it every time you start a new session.
#
# ---
#
# <div class="alert alert-block alert-info">
# <b>For R users:</b><br>
# Think of <code>install.packages()</code> as Python’s <code>pip install</code>, 
# and <code>library()</code> as Python’s <code>import</code>.
# </div>
#
#
# ---
#
# Let’s try it.

# %% [markdown]
# ### Exercise 2 – Importing Packages
#
# 1. Use `pip install` to install the library `beautifulsoup4`. 
# 2. Load the `bs4` package for use in Python -- see example for the `csv` package below.
# 3. Use the `help()` function to inspect what the `bs4` and `csv` packages can do.
#

# %%
# starter code (runs)
import csv

# TODO: pip install to install beautifulsoup4; extend import statements to bs4 (also call it like that!) and CSV, 
# then call help for bs4 and CSV

# %% [markdown]
# ### ✅ Solution – Exercise 2

# %%
# !pip install beautifulsoup4
import csv
import bs4

help(csv)
help(bs4)

# %% [markdown]
# **Explanation**  
# - `import csv` loads tools for handling comma-separated files, which we’ll use later to store scraped data.  
# - `import bs4` loads tools for working with web data obtained through web scraping. 
# - `help()` gives you quick documentation right inside Jupyter.  
# You don’t need to read it all now — just know that you can always look things up later. Oh, and __did you know you can use Jupyter also to delete the output of cells you've run? Handy for cleaning up your notebook.__
#
# ---
#
# <div class="alert alert-block alert-info">
# <b>Need help?</b><br>
# You can always ask our <b>Tilly Chatbot</b> on Canvas for course-specific questions.  
# </div>

# %% [markdown]
# ## 1.5 Summary
#
# You’ve now:
# - Launched Python successfully.  
# - Learned how to open Jupyter Notebook or VS Code.  
# - Imported your first packages (`json` and `csv`).  
#
# We’ll use these same tools throughout the course to work with real web data.  
# In the next session, we’ll move into **Python Basics**, where we’ll start writing small bits of code to process data ourselves.

# %% [markdown]
# # 2. Python Basics – from R to Python
#
# In this part, we’ll connect what you already know from R or RStudio to Python.  
# You’ll learn how to work with variables, loops, lists, and dictionaries — all the small building blocks we’ll later need to collect and store web data.
#
# Don’t worry if it feels like a lot at once — we’ll move slowly, and every step connects to something we’ll actually do later when scraping websites or using APIs.

# %% [markdown]
# ## 2.1 Variables and f-strings
#
# In Python, we use **variables** to store information, just like you do in R.  
# You assign them using an equals sign `=` instead of the arrow `<-`.
#
# Let’s look at a simple example.

# %% [markdown]
# ### Exercise 3 – Creating Variables
#
# The cell below already defines a variable called `name`.  
# Run it once, and then extend it by:
# 1. Adding another variable `age`, and  
# 2. Extending the *f-string* so it prints both your name and your age.
#
# *(If you’ve never seen an f-string before, it’s a way to mix text and variables in one sentence.)*

# %%
# starter code (works)
name = "Ada"
print(f"My name is {name}.")  # TODO: also show your age

# %% [markdown]
# ### ✅ Solution – Exercise 3

# %%
name = "Ada"
age = 30
print(f"My name is {name} and I am {age} years old.")

# %% [markdown]
# **Explanation**  
# - The `f` before the string lets you place variables inside `{}`.  
# - Try changing `name` or `age` and run the cell again.  
# - Later, we’ll use f-strings to build URLs dynamically — for instance:  
#   ```python
#   url = f"https://api.example.com/users/{user_id}"
#   ```
#
#

# %% [markdown]
# ## 2.2 Lists and Dictionaries – Flexible Data Structures
#
# Web data rarely comes in neat tables.  
# Often, each record (a product, a tweet, a post) contains multiple pieces of information.  
# In Python, we can store such data using **lists** and **dictionaries**.
#
# - A **list** is like an ordered collection — similar to a vector in R.  
# - A **dictionary** is like a named list or a tiny spreadsheet row: it stores *key-value pairs*.
#
# Let’s see what that looks like.

# %% [markdown]
# ### Exercise 4 – Exploring a List of Dictionaries
#
# Here’s an example list of artists.  
# Run the cell below and look carefully at what prints out.

# %%
artists = [
    {"name": "Adele", "genre": "Pop"},
    {"name": "Kendrick Lamar", "genre": "Hip-Hop"}
]
print(artists)

# %% [markdown]
# **Explanation**  
# The square brackets `[]` mean “this is a list”,  
# and the curly brackets `{}` show “this is one dictionary (record)”.  
# Each dictionary has two keys: `name` and `genre`.

# %% [markdown]
# __Now, let's extend the list.__
#
# Add a third artist to the list (remember commas between entries) and then re-run the cell.

# %%
# starter code (works)
artists = [
    {"name": "Adele", "genre": "Pop"},
    {"name": "Kendrick Lamar", "genre": "Hip-Hop"}
    # TODO: add another artist here
]
print(artists)

# %% [markdown]
# ### ✅ Solution – Exercise 4

# %%
artists = [
    {"name": "Adele", "genre": "Pop"},
    {"name": "Kendrick Lamar", "genre": "Hip-Hop"},
    {"name": "Taylor Swift", "genre": "Pop"}
]
print(artists)

# %% [markdown]
# **Why this matters for web data**  
# When we later scrape sites like Spotify or IMDb, each API response is basically a big dictionary or a list of dictionaries.  
# For example:  
# ```python
# track = {"title": "Hello", "artist": "Adele", "streams": 520000000}
# ```
# Tables can’t easily handle this nested structure — dictionaries can.
#
#

# %% [markdown]
# ## 2.3 Control Flow – Repeating Web Actions
#
# When you collect data, you’ll often repeat the same action for many pages or items.  
# That’s where **loops** come in.
#
# - **for loops** repeat actions for a known list of items.  
# - **while loops** repeat until a condition is no longer true — handy when you don’t know how many pages there are.

# %% [markdown]
# ### Exercise 5 – for loops
#
# The code below prints each artist’s name.  
# Modify it so it also prints the artist’s genre next to their name.

# %%
# starter code (runs)
for artist in artists:
    print(artist["name"])  # TODO: include genre too

# %% [markdown]
# ### ✅ Solution – Exercise 5

# %%
for artist in artists:
    print(f"{artist['name']} – {artist['genre']}")

# %% [markdown]
# **Explanation**  
# - `for artist in artists:` goes through the list one record at a time.  
# - Inside the loop, we use dictionary keys (`['name']`, `['genre']`) to access each field.  
# - In real scraping, each iteration could download a different webpage or API response.
#
#

# %% [markdown]
# ### Exercise 6 – while loops
#
# Sometimes we don’t know how many pages exist — imagine a “next page” button at the bottom of a site.  
# The `while` loop keeps running as long as a certain condition is true.
#
# Try running this example.  
#
# It simulates visiting a (random) number of pages, until the "simulated" number of pages is exceeded.
#

# %%
# starter code (runs)
import random

page = 1
has_more_pages = True

while has_more_pages:
    print(f"Scraping page {page} …")
    page += 1

    if (random.uniform(0,100)>90): # simulate last page
        has_more_pages = False

print("No more pages left.")


# %% [markdown]
# **Explanation**  
# The loop keeps going until the condition `has_more_pages` turns False.  
# This is a common pattern when scraping — you can keep clicking “next” until there is none.
#
#

# %% [markdown]
# ## 2.4 Functions – Reusing Code
#
# As you start writing longer scripts, you’ll notice you often copy the same few lines of code.  
# Instead of repeating them, we can bundle them into a **function**.
#
# Functions help you stay organized and make your code easier to read and debug.

# %% [markdown]
# ### Exercise 7 – Writing a Simple Function
#
# Write a function called `fetch_data(url)` that prints  
# “Fetching data from &lt;url&gt;…”.  
# Then call it for each URL in the list below.

# %%
# starter code (runs)
def fetch_data(url):
    # TODO: print message that includes the URL
    pass

urls = ["page1.html", "page2.html", "page3.html"]
for u in urls:
    fetch_data(u)

# %% [markdown]
# ### ✅ Solution – Exercise 7

# %%
def fetch_data(url):
    print(f"Fetching data from {url} …")

urls = ["page1.html", "page2.html", "page3.html"]
for u in urls:
    fetch_data(u)

# %% [markdown]
# **Explanation**  
# - We define functions with `def function_name(parameters):`.  
# - Indentation matters — everything inside the function is indented.  
# - Functions let us reuse logic (like downloading data from a URL) without copy-pasting it each time.
#
#

# %% [markdown]
# ## 2.5 Saving Data – CSV and JSON
#
# Once you’ve collected data, you’ll want to save it — either as a flat CSV file or as a structured JSON file.  
# Both formats are human-readable and easy to share.

# %% [markdown]
# ### Exercise 8 – Writing a CSV File
#
# Let’s save our artists to a file called `artists.csv`.  
# Add a header row and a couple of artist rows.  
# After running it, open the file in Excel or a text editor to see what it looks like.

# %%
# starter code (runs)
import csv
with open("artists.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["artist", "genre"])
    writer.writerow(["Adele", "Pop"])  # TODO: add another row

# %% [markdown]
# ### ✅ Solution – Exercise 8

# %%
import csv
with open("artists.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["artist", "genre"])
    writer.writerow(["Adele", "Pop"])
    writer.writerow(["Kendrick Lamar", "Hip-Hop"])

# %% [markdown]
# **Explanation**  
# Each `writerow()` adds a line to the CSV file.  
# This is exactly how you’ll store scraped data later — one row per record.
#
#

# %% [markdown]
# ### Exercise 9 – Writing a JSON File
#
# Now let’s do the same thing in JSON format — the standard for APIs and web data. Recall: please add another data point to the JSON dictionary, and write it to a file.

# %%
# starter code (runs)
import json
artists_data = [
    {"artist": "Adele", "genre": "Pop"},
    {"artist": "Kendrick Lamar", "genre": "Hip-Hop"}
]

with open("artists.json", "w", newline = '\n', encoding="utf-8") as f:
    f.write(json.dumps(artists_data, ensure_ascii=False, indent=2))

# %% [markdown]
# ### ✅ Solution – Exercise 9

# %%
import json
artists_data = [
    {"artist": "Adele", "genre": "Pop"},
    {"artist": "Kendrick Lamar", "genre": "Hip-Hop"},
    {"artist": "Taylor Swift", "genre": "Pop", "country": "US"}
]

with open("artists.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(artist, ensure_ascii=False, indent=2))

# %% [markdown]
# **Explanation**  
# - `json.dump()` writes structured data in the same format most web APIs use.
# - Observe that for `csv` files, we use `writer` functions from the `csv` page; these are not needed for `json` files, where we immediately use the `.write` function on our "opened" file `f`. TLDR: CSV &rarr; `writer = csv.writer(f)` and `writer.writerow()`, JSON &rarr; `f.write()`
# - Notice how we could add an extra field (`country`) without breaking anything — that’s why JSON is so flexible.
#
# ---
#
# | Feature | CSV | JSON |
# |:--|:--|:--|
# | Structure | Flat (rows + columns) | Nested (key-value) |
# | Good for Excel | ✅ Yes | ⚠️ Limited |
# | Good for APIs | ❌ No | ✅ Yes |
# | Human Readable | ✅ | ✅ |
#
# ---
#
# **Tip:** You’ll often use both — JSON to store raw API responses and CSV to summarize cleaned data. Here, we stored a single JSON objects; in practice, you often encounter one JSON object per line (called "new-line separated JSON" files).

# %% [markdown]
# ## 2.6 Summary
#
# Great work — you’ve covered a lot!  
# By now you can:
# - Create variables and combine them with text using f-strings.  
# - Store information in lists and dictionaries.  
# - Repeat actions with loops and organize code with functions.  
# - Save data in both CSV and JSON formats.  
#
# These are the core skills you’ll need for our next topic: **Understanding Web Data** — where we’ll start talking about what HTML and APIs actually look like.

# %% [markdown]
# # 3  Understanding Web Data
#
# You now know how to code, loop, and store data – time to apply these skills to the *web*!  
# In this part we’ll learn how to:
# - Fetch information from websites and APIs  
# - Extract what we need  
# - Add timestamps  
# - Store everything in files  
# - Repeat the process automatically using loops
#
# You’ll see that the ideas from Section 2 (variables, loops, files) appear again here – just applied to *web data*.

# %% [markdown]
# ## 3.1  Web Scraping vs APIs – How Data Travels on the Web
#
# So far, we’ve worked with data that already lived on our computer — numbers, strings, CSV files.  
# But the real fun begins when we get data **from the web**.
#
# Every time you open a website, two things happen:
#
# 1. Your **browser** sends a *request* to a **server**.
# 2. The **server** replies with a *response* — often a big chunk of text, called **HTML**.
#
# HTML describes what the browser should display — the layout, the colors, the content, everything.  
# But we can also read that text with Python and extract specific information from it, like song titles or artist names.
#
# There’s another way websites provide data: through **APIs** (Application Programming Interfaces).  
# Instead of HTML, an API sends back structured data in a format called **JSON**.  
# JSON is like a digital spreadsheet — organized, consistent, and easy for Python to read.
#
# You can think of the difference like this:
#
# | For humans | For machines |
# |-------------|--------------|
# | 🧍 Websites → HTML pages | 🤖 APIs → JSON data |
#
# Both contain information — but one is formatted for your *eyes*, the other for your *code*.
#
# <img src="images/web_data_workflow.png" alt="The Web Data Workflow" width="400"/>
#
# > *Figure 1.* The Web Data Workflow – four layers that structure how we collect web data.  
# > In this tutorial, we’ll focus on the first two layers: **Extraction** and **Looping**.
#
# **Examples**
#
# - **Web scraping:** collecting hotel prices, comparing booking sites, reading product reviews.  
# - **APIs:** accessing Spotify song data, querying OpenAI for text, or using the Google Maps API for locations.
#
# The good news? You already know most of the programming tools we’ll need:  
# loops to repeat actions, variables to store results, and files to save them.
#
# Now let’s see what these two worlds — HTML and APIs — look like in practice.
#
# ---
#
# ### Exercise 10 – Spot the Difference
#
# 1. Open [`https://music-to-scrape.org`](https://music-to-scrape.org) in your browser.  
#    Right-click and choose **Inspect Element** — this shows you the HTML that the server sent.
# 2. Now open [`https://api.music-to-scrape.org/users/recently-active`](https://api.music-to-scrape.org/users/recently-active).  
#    You’ll see raw JSON — not pretty, but very structured.
# 3. Compare:  
#    - Which version looks nicer for humans?  
#    - Which one is easier for a computer to understand?
# 4. That’s the difference between **web scraping** and **APIs**.  
#    Both give you access to the same kind of information — but in different formats.

# %% [markdown]
# ## 3.2  Web Scraping in Action (HTML Extraction + Storage + Timestamps)
#
# Let’s put our Python skills to work and scrape real data from the web!  
# We’ll use a demo site, [music-to-scrape.org](https://music-to-scrape.org), which lists songs and artists.
#
# Our goal:  
# - Extract the list of songs  
# - Add the time of collection  
# - Store the results in a CSV file  
#
# ---
# ### Concept: How Web Scraping Works
#
# When your browser opens a website, it receives **HTML** — text that describes what’s on the page.  
# We can ask Python to fetch that same HTML, then use a helper library called **BeautifulSoup** to “read” it.
#
# BeautifulSoup turns HTML into something we can search through, like:  
# “Find every `<div>` with the class name `song`.”
#
# Let’s try it together.

# %% [markdown]
# ### Step 1 – Fetch and Parse the Page
#
# First, we’ll fetch the web page and inspect the first song block.

# %%
import requests
from bs4 import BeautifulSoup

url = "https://music-to-scrape.org"
response = requests.get(url)

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find one song element
recently_played = soup.find("section", attrs={"name": "recently_played"})
first_song = recently_played.find('h5')
print("Example song element ⬇️")
print(first_song.get_text(strip=True))

# %% [markdown]
# You’ve just fetched a web page and extracted the first song title. 🎉 In fact, you *first* "zoomed in" on the recently played songs section, and then - within that section - narrowed down to the first most recently played song.
#
# The next step is to get *all* recently played songs on the page.

# %% [markdown]
# ### Exercise 11 – Collect All Recently Played Songs
#
# Your turn!  
# Modify the code above so it collects **all** songs.
#
# **Hints**
# - Use `.find_all()` instead of `.find()`.  
# - Loop through the results and append each song’s text to a list called `songs`.  
# - Print how many songs you found.

# %% [markdown]
# ### ✅ Solution – Exercise 11

# %%
songs = []

# Find one song element
recently_played = soup.find("section", attrs={"name": "recently_played"})

all_songs = recently_played.find_all('h5')

for item in all_songs:
    songs.append(item.get_text(strip=True))

print(f"Found {len(songs)} songs.")
print("First few songs:", songs[:5])

# %% [markdown]
# Well done — you’ve just turned a web page into a Python list!  
# That’s the core idea of **web scraping**.

# %% [markdown]
# ---
# ### Step 2 – Add a Timestamp
#
# In data projects, it’s important to record *when* you collected the data.  
# That helps others (and future you!) reproduce or compare results later.
#
# Python’s `time` module can generate timestamps.

# %%
import time

timestamp = time.time()
print("Current Unix time:", timestamp)

# %% [markdown]
# <div class="alert alert-block alert-info">
# <b>What's Unix time?</b><br>
# It counts the seconds since 1 January 1970 — a universal format computers use to record moments in time.  
# It’s perfect for logging when your data was collected.
# </div>
#
# ---
#
# ### Exercise 12 – Add Timestamps and Save to CSV
#
# Let’s save our scraped songs to a CSV file — but before writing,  
# **add a timestamp** to each record.
#
# **Hints**
# - Use the `csv` library to write a header (`title`, `timestamp`) and the rows.

# %% [markdown]
# ### ✅ Solution – Exercise 12


# %%
import csv
import time

# Add timestamp to each song
timestamp = time.time()

# Write to CSV
with open("songs.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["title", "timestamp"])
    for song in songs: 
        writer.writerow([song, timestamp])

print("✅  Saved songs.csv with titles and timestamps.")

# %% [markdown]
# - A more elegant solution would use list comprehension, tying together all songs in a "one liner" and avoiding the extra loop. 
# - You can create a list like `rows = [[song, timestamp] for song in songs]`.  
#

# %%
import csv

# Add timestamp to each song
timestamp = time.time()
rows = [[song, timestamp] for song in songs]

# Write to CSV
with open("songs.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["title", "timestamp"])
    writer.writerows(rows)

print("✅  Saved songs.csv with titles and timestamps.")

# %% [markdown]
# Excellent!  
# You’ve now completed the **Extraction** part of the Web Data Workflow:
#
# 1️⃣ Fetched a page using `requests`  
# 2️⃣ Parsed the HTML with BeautifulSoup  
# 3️⃣ Added timestamps to record collection time  
# 4️⃣ Stored the data in a CSV file  
#
# Next, we’ll see how to collect structured data more directly — through **APIs**.

# %% [markdown]
# ## 3.3  APIs in Action (Fetching Structured Web Data)
#
# In the previous section, we scraped a web page — we asked Python to read and interpret the HTML of a site.  
# Now we’ll explore an alternative (and often better) way to get web data: **APIs**.
#
# ---
# ### Concept: What is an API?
#
# An **API** (Application Programming Interface) is like a “data menu” for a website.  
# Instead of us digging through HTML, the website provides structured data — usually in **JSON** format — directly ready for analysis.
#
# Think of it this way:
# - A **website** is meant for *humans* (pretty, clickable, visual).  
# - An **API** is meant for *computers* (clean, predictable, machine-readable).
#
# Many companies provide APIs:  
# - OpenAI (for language models)  
# - Spotify (for song metadata)  
# - Twitter/X, Instagram, or Reddit (for social data)  
#
# We’ll again use the `music-to-scrape.org` demo API, which returns information about artists.

# %% [markdown]
# ### Step 1 – Fetch Data from an API
#
# The endpoint below returns JSON data describing featured artists on the site.  
# Let’s make a request and print the first few items.

# %%
import requests

url = "https://api.music-to-scrape.org/artists/featured"
response = requests.get(url)
data = response.json()   # Convert JSON text into a Python dictionary

# Show part of the structure
print("Top-level keys:", data.keys())
print("First artist entry:")
print(data["artists"][0])

# %% [markdown]
# See the difference?  
# With web scraping, we had to search through messy HTML.  
# With an API, the data comes pre-structured in dictionaries and lists — ready for analysis.
#
# ---
# ### Exercise 13 – Extract Artist Names
#
# Look at the variable `data`. It contains a list under `data["artists"]`.  
# Each artist is a dictionary with several attributes (e.g., `artist_name`, `artist_id`).
#
# Your task:  
# - Loop through all artists in `data["artists"]`.  
# - Collect the names into a list called `artist_names`.  
# - Print the number of artists and the first few names.
#
# *(You can reuse ideas from Section 3.2 where you looped through songs.)*

# %% [markdown]
# ### ✅ Solution – Exercise 13

# %%
artist_names = []
for artist in data['artists']:
    artist_names.append(artist["artist"])

print(f"Found {len(artist_names)} artists.")
print("First few:", artist_names[:5])

# %% [markdown]
# Great!  
# You’ve just extracted structured information from an API.
#
# ---
# ### Step 2 – Combine with a Loop and Delay
#
# Sometimes APIs allow you to request different resources by ID.  
# For example, each artist has a unique `artist_id`.  
# We can use these IDs to fetch more detailed information — but we should be polite and wait between requests.
#
# That’s where a small **delay** (`time.sleep()`) comes in.  
# It prevents us from overwhelming the server.

# %%
import time

# Preview one artist ID
print("Example ID:", data["artists"][0]["artist_id"])

# %% [markdown]
# Let’s loop through three artists and fetch their info pages. 
#
# The URL to use for this is `https://api.music-to-scrape.org/artist/info?artistid=<ENTER ID HERE>`
#
# The code runs a few requests and prints the artist IDs found in each response.
# The delay of one second keeps things polite.

# %%
artists = ['ARICCN811C8A41750F', 'AR1GW0U1187B9B29FD', 'ARZ3U0K1187B999BF4']

for artist in artists:
    print(f"Fetching artist {artist} ...")
    url = f"https://api.music-to-scrape.org/artist/info?artistid={artist}"
    response = requests.get(url)
    info = response.json()
    print(info)
    time.sleep(1) # respect retrieval limits

# %% [markdown]
# Notice how similar this looks to our scraping code — but here, we don’t search the page with BeautifulSoup.  
# The API directly gives us the data we need.
#
# ---
# ### Exercise 14 – Add a Timestamp and Store API Results
#
# Your turn!  
# Extend the loop above so that:
#
# - Each artist dictionary also stores a new key `"timestamp"` using `time.time()`.  
# - You collect all enriched artist dictionaries in a list called `records`.  
# - You then write `records` to a JSON file called `artists.json`.
#
# **Hint:** Use `json.dump(records, file)` from the `json` module to store the data.

# %% [markdown]
# ### ✅ Solution – Exercise 14

# %%
import json

records = []

for artist in artists:
    url = f"https://api.music-to-scrape.org/artist/info?artistid={artist}"
    response = requests.get(url)
    info = response.json()
    info["timestamp"] = time.time()
    records.append(info)
    time.sleep(1)

# Save as JSON
with open("artists.json", "w", encoding="utf-8") as f:
    json.dump(records, f, ensure_ascii=False, indent=2)

print("✅ Saved artists.json with timestamps.")

# %% [markdown]
# ---
# ### What You’ve Learned
#
# In this section, you’ve seen how APIs complement web scraping:
#
# | Task | Web Scraping | API |
# |------|---------------|-----|
# | Data format | HTML | JSON |
# | For humans or machines? | Humans | Machines |
# | Libraries used | `requests`, `BeautifulSoup` | `requests`, `json` |
# | Common in | Small websites | Big data platforms (e.g., OpenAI, Spotify) |
#
# ---
# **Recap**
#
# 1️⃣ You fetched data directly from an API endpoint.  
# 2️⃣ You looped through results and added timestamps.  
# 3️⃣ You saved your results as a JSON file.  
#

# %% [markdown]
# ## 4.  Wrap-Up and Reflection
#
# Congratulations — you’ve completed your first full journey from **starting a Python environment** to **collecting and storing real-world data**.  
# Across the three parts of this tutorial, you learned to:
#
# - **Set up and navigate** Python using Jupyter / VS Code / Google Colab.  
# - **Transfer your R knowledge** to Python — understanding variables, loops, and data structures.  
# - **Fetch and parse** information from the web using `requests` and `BeautifulSoup`.  
# - **Retrieve structured data** from APIs and store it as CSV or JSON.  
# - **Enrich results** with timestamps and write clean, reproducible code.
#
# ---
# ### Looking Ahead
#
# In the next tutorials, you’ll **go deeper**:
# - Automating larger scraping tasks and multi-page loops  
# - Handling structured APIs with authentication  
#
# Before that, take a moment to review your own notebook:
# - Are all cells executed top-to-bottom without errors?  
# - Did you comment your code clearly enough that future-you understands it?  
# - Can you explain, in your own words, the difference between scraping and an API?
#
# If yes — you’re ready for the next level.
#
# <div class="alert alert-block alert-info">
# <b>Takeaway</b><br>
# Every dataset on the web — whether hidden in HTML or exposed through an API — can be reached, understood, and stored with a few lines of clean, reproducible Python code.
# </div>
