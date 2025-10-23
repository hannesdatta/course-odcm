# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.3
#   kernelspec:
#     display_name: Python (Regular)
#     language: python
#     name: regularpython
# ---

# %% [markdown]
# # 1. Web Scraping 101
#
# Welcome back!  
#
# In the **Python Bootcamp**, you already learned how to open a web page with `requests`,
# read a few bits of data using `BeautifulSoup`, and save the result in a file.
# That was your first small taste of **web scraping**.
#
# In this tutorial, we’ll take the next step: you’ll build your first
# **complete web scraper** — a short program that automatically collects
# information from a website and saves it for later analysis.
#
# ---
#
# ## 1.1 Recap
#
# ### What does “web scraping” mean?
#
# - Every website you visit (Spotify, IMDb, a news site…) is built with **HTML**.
# HTML is just a structured text file that tells your browser what to show:
# where the titles go, which images to load, and so on.
# - A **web scraper** is a piece of Python code that reads this HTML directly,
# finds the parts we care about — like artist names or song titles —
# and stores them neatly in a table or CSV file.
#
# ### Why scrape websites?
#
# Sometimes the data you need isn’t available as a CSV or via an API. Instead of copying it by hand, you can let Python do it for you.
#
# A few quick examples:
# - Collect product prices from a webshop  
# - Gather job openings from a company page  
# - Extract song data from a music website  
#
# Once you get the hang of it, scraping small datasets like these
# is surprisingly useful — and kind of fun.
#
# <div style="border-left: 4px solid #2e7d32; background-color: #e8f5e9; padding: 0.8em 1em; border-radius: 6px;">
#   <p>💡 <strong>Why Scrape?</strong></p>
#   <p>Imagine you find a webpage with a list of songs:</p>
#   <pre style="margin: 0.5em 0; padding: 0.6em; background: #f7f7f7; border: 1px solid #ddd; border-radius: 4px;">Song 1 – Artist A
# Song 2 – Artist B
# Song 3 – Artist C</pre>
#   <p>You could copy-paste by hand—but what if there are 100 songs or 100 pages?</p>
#   <ul>
#     <li>Visit each page automatically</li>
#     <li>Grab all titles and artists</li>
#     <li>Save them neatly into one file</li>
#   </ul>
#   <p>That’s what we’ll build step by step.</p>
# </div>
#
#
# ---
#
# ## 1.2 Today's focus: a "static" web scraper
#
# Some websites are simple: when you open the page, **all the data is already there**
# in the HTML. These are called **static websites**.
#
# For example, a page showing “Top 10 songs of the week” might list all ten songs
# right away.   For pages like that, we can simply:
#
# 1. **Download** the page’s HTML using `requests`, and  
# 2. **Extract** what we want using `BeautifulSoup`.
#
# Later in the course, we’ll meet **dynamic websites** — pages that load content
# *after* you scroll or click (for example, many shops or streaming sites). For those, we’ll use special tools like Selenium. But before that, let’s master the simple — and much faster — static kind first.
#
# __What you’ll learn in this tutorial__
#
# In this tutorial, you’ll learn how to:
#
# - Understand how a web page is structured and where to find your data  
# - Write a script that downloads several pages automatically  
# - Handle small issues like missing data  
# - Be polite to websites by adding short pauses  
# - Save everything you collected in a clean, reusable format  
#
# Each step builds on the previous one, always starting from working code.
#
# <div style="border-left: 4px solid #2e7d32; background-color: #e8f5e9; padding: 0.8em 1em; border-radius: 6px;">
#   <p>💡 <strong>Ethical and Legal Use</strong></p>
#   <ul>
#     <li>Add short pauses between requests (so you don’t overload the site)</li>
#     <li>Don’t scrape information behind login screens</li>
#     <li>Never collect personal or private data</li>
#     <li>Check the site’s <code>robots.txt</code> file to see what’s allowed</li>
#   </ul>
#   <p>We’ll talk more about these topics in the web-data ethics lecture later in the course. For now, just keep these good habits in mind.</p>
# </div>
#
# ## 1.3 Checking that your setup works
#
# Before we start scraping, let’s make sure everything is ready.
# You’ll need three Python packages:
#
# - `requests` — downloads web pages  
# - `BeautifulSoup` — reads and parses the HTML  
# - `time` — lets you pause between requests so you don’t get blocked  
#
# __Run the next cell to test your setup.__
# %%
import requests
from bs4 import BeautifulSoup
import time

print("✅ All good! Requests, BeautifulSoup, and time are ready to use.")

# %% [markdown]
# __Encountering issues?__ Then please install the necessary packages by running the command below on your command line/terminal.
#
# ```bash
# pip install requests beautifulsoup4
# ```
#
# Once that works, you’re ready to start exploring real websites!


# %% [markdown]
# # 2. Finding Information on a Web Page
#
# Now that your setup works, let’s explore how to actually **find** information
# on a web page.
#
# When you open a website in your browser, you see titles, images, links,
# and descriptions. Underneath all that lies **HTML**, which organizes everything.
#
# In this section, we’ll learn how to read that structure, find the right pieces,
# and extract exactly the data we want.  
# You’ll also learn how to debug small issues when something doesn’t behave as expected.
#
# ---

# %% [markdown]
# ## 2.1 Understanding the structure of a web page
#
# Every website is built with HTML — the same language you briefly saw in the Bootcamp.
# Here’s what one small part of a page might look like:
#
# ```html
# <div class="list-group-item"</div>
# ```
#
# or
#
# ```html
# <a href="song?song-id=SOJKNYV12A8C133E9C">Gabriel Yared</a>
# ```
#
# Let’s break this down:
#
# - The **tag** (e.g., `<div`, `<a>`) tells us what kind of element it is. For example, `<div>` is a section "divider", and `<a>` is a link. In case you're interested, [here's a full list of tag words](https://www.w3schools.com/tags/).
# - The **attribute** (`class`) and **value** (`list-group-item`) gives extra information, e.g., an element we can select for scraping, typically used to group of similar elements. The attribute "class" is probably the one you are going to encounter a lot.
# - The **text** (`Gabriel Yared`) is what we actually see on the page. It 'sits' inbetween `>` and `<`.
#
# These pattern appears everywhere. When we scrape, we’ll use it as a "navigation guide" to capture what we're interested in:
# **Tag → Attribute → Value → Text (or attribute content)**.
#
# Let’s look at an example from our demo website.

# %%
import requests
from bs4 import BeautifulSoup

url = "https://music-to-scrape.org"   # demo site
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

# show the first few links so we can explore them
links = soup.find_all("a")[:5]
for l in links:
    print(l)

# %% [markdown]
# ### Exercise 1
#
# Modify the snippet above, to __print the LINK__ (rather than the full HTML), for __all__ links contained on the website.
#
# __Tip:__ use `l.get('href')` to extract the link addresses.

# %%
# starter code
import requests
from bs4 import BeautifulSoup

url = "https://music-to-scrape.org"   # demo site
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

# show the first few links so we can explore them
links = soup.find_all("a")[:5]
for l in links:
    print(l)

# %% [markdown]
# ### ✅ Solution - Exercise 1

# %%
import requests
from bs4 import BeautifulSoup

url = "https://music-to-scrape.org"   # demo site
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

links = soup.find_all("a")
for l in links:
    print(l.get('href'))

# %% [markdown]
# ## 2.2 Using `.find()` and `.find_all()` — your main tools
#
# BeautifulSoup gives you two simple but powerful commands:
#
# - `.find()` → returns **the first** matching element  
# - `.find_all()` → returns **all** matching elements as a list  
#
# Both take two main arguments:
# 1. The **tag name** (like `"a"` or `"div"`)  
# 2. **Attribute-value pairs**. (`attrs = {'attribute': 'value'})`. If the special case of classes, you can directly add the class to the `.find()` or `.find_all()` command (`class_="recently_played"`).
#
# Let’s try it next.

# %%
# Starter code (works as is)
first_section = soup.find("section", attrs = {"name": "recently_played"})
all_links_in_section  = first_section.find_all("a")

print("\nNumber of links found:", len(all_links_in_section))

# %% [markdown]
# ### Exercise 2 – Modify the search
#
# The code above finds links in the first section on the website ("recently played")
#
# Your task:
#
# 1. Change the code to extract the number of links from the "Top 15 weekly tracks" section.
# 2. Change the code to also print all the identified links to the screen using f-strings.
#
# Don’t worry — the worst that happens is you get an empty list.
#
# **Tip:** If you get `None` or `[]`, check the tag and class name again
# using your browser’s *Inspect* tool.
#

# %%
# starter code
first_section = soup.find("section", attrs = {"name": "recently_played"})
all_links_in_section  = first_section.find_all("a")

print("\nNumber of links found:", len(all_links_in_section))

# %% [markdown]
# ### ✅ Solution - Exercise 2

# %%
# starter code
first_section = soup.find("section", attrs = {"name": "weekly_15"})
all_links_in_section  = first_section.find_all("a")

print("\nNumber of links found:", len(all_links_in_section))

for l in all_links_in_section:
    print(f'Link: {l.get('href')}')

# %% [markdown]
# ## 2.3 Extracting the text or the link itself
#
# Once you’ve found the right element, you can choose what to extract:
#
# - `[ ... ]` or `.get(...)` lets you access an attribute (like a link or image source) - we've done this before.
# - `.get_text()` gives you what’s visible on the page (the text between the tags).  
#
# Example:
# ```python
# element.get_text()     # visible text
# element["href"]        # link stored inside the tag
# element.get("href")    # link stored inside the tag
#
# ```
#
# Let’s practice.

# %%
# this code builds on solution 2, and spits out the name of each song in the weekly top 15.
first_section = soup.find("section", attrs = {"name": "weekly_15"})
items  = first_section.find_all('a')

for i in items:
    print(f'Song: {i.find(class_ = 'center-text').get_text().strip()}')
    print('\n') # new line

# %% [markdown]
# ### Exercise 3 – Adjust the extraction
#
# 1. Modify the code snippet (below) to also spit out the LINK to each song in the loop.
#
# **Goal:** see that `.get_text()` extracts what’s visible (you already used it here), while `[...]` or `.get()` pulls information stored inside the tag.
#
#

# %%
# starter code
first_section = soup.find("section", attrs = {"name": "weekly_15"})
items  = first_section.find_all('a')

for i in items:
    print(f'Song: {i.find(class_ = 'center-text').get_text().strip()}')
    print('\n') # new line

# %% [markdown]
# ### ✅ Solution - Exercise 3

# %%
# starter code
first_section = soup.find("section", attrs = {"name": "weekly_15"})
items  = first_section.find_all('a')

for i in items:
    print(f'Song: {i.find(class_ = 'center-text').get_text().strip()}')
    print(f'Link: {i.get('href')}')
    print('\n') # new line

# %% [markdown]
# ## 2.4 Quick recap
#
# - Use your browser’s *Inspect* tool to see how the page is structured.  
# - Use `.find()` and `.find_all()` to pick out tags or groups of tags.  
# - Extract either the visible **text** or an **attribute** like `href`.  
# - When things don’t work, print what you have and go one step back.  
#
# ---
#
# Great job — you now know how to explore and extract information
# from a single web page.
#
# In the next section, we’ll build on this by looping over multiple pages,
# adding short delays so we don’t overload servers,
# and handling small errors automatically.
#
#

# %% [markdown]
# ## 3. From One Page to Many
#
# So far, you’ve learned how to scrape information from **one single page**.  
# But most projects need data from **many pages** — for example, one page per artist,
# product, or job listing.
#
# In this section, you’ll learn how to:
#
# - Loop through multiple pages automatically  
# - Record *when* each page was collected  
# - Keep your scraper running even when data is missing  
# - Add short pauses so you don’t overload servers  
# - Turn your scraping code into a reusable function  
#
# By the end, you’ll have a complete static web scraper that can
# gather structured data across multiple pages — responsibly.
#

# %% [markdown]
# ## 3.1 Extracting User Profile Data  
#
# [`music-to-scrape.org`](https://music-to-scrape.org) holds user consumption data across multiple pages (one per week). Our goal is to navigate each user’s profile and save the names of all songs, artists, and timestamps (date/time) by visiting these pages one by one.  

# %% [markdown]
# __Let's try it out__
#
# Open [the website](https://music-to-scrape.org/user?username=StarCoder49&week=36), and click on the "previous" button at the top of the page. Do you understand how you will be able to "loop" through the site?
#
# <img src="https://raw.githubusercontent.com/hannesdatta/course-odcm/master/content/docs/modules/week3/webscraping101/images/mts-user-page.png" align="left" width=90%/>

# %% [markdown]
# It’s helpful to prototype before assembling a full working script.  
#
# Let’s start by downloading the first page of a user and storing it in a variable called `soup`. Here, we make use of a header, such that the website "knows" which browser we are using (or, pretend to be using).

# %%
import requests
from bs4 import BeautifulSoup

url = 'https://music-to-scrape.org/user?username=StarCoder49&week=6'
header = {'User-agent': 'Mozilla/5.0'}
res = requests.get(url, headers = header)
res.encoding = res.apparent_encoding
soup = BeautifulSoup(res.text)


# %% [markdown]
# We can now try a few commands to access information on the site. Of course, the browser inspect tool is important to have opened on the side. You probably notice that the table is quite easy to capture - it has it's own tag, called `table`.

# %% [markdown]
#
# <img src="https://raw.githubusercontent.com/hannesdatta/course-odcm/master/content/docs/modules/week3/webscraping101/images/mts-table.png" align="left" width=90%/>

# %%
table = soup.find('table')
table

# %% [markdown]
# See? This one worked quite well! Inspecting the table a bit more, you can get at the individual rows using the `tr` tag. Again, use your browser's inspect tool to spot it!

# %%
table.find('tr')

# %% [markdown]
# This is just the first row. Using `.find_all()`, instead, will give you a list of all rows.

# %%
rows = table.find_all('tr')
rows

# %% [markdown]
# We can also check whether the number of rows is equal to what we would expect from looking at the website. Using the `len` function for this yields...

# %%
len(rows)

# %% [markdown]
# Looks about right? Yes! So, let's now try to extract, for one row, the name of the song and artist, corresponding to the first and second column of the table.
#
# Let's first select one row for prototyping. We take row 2 (which is the first row after the table header).

# %%
one_row = rows[1]

# %%
one_row

# %%
one_row.find_all('td')[0].get_text() # for song name

# %%
one_row.find_all('td')[1].get_text() # for artist name, corresponding to the second "column"

# %% [markdown]
#
# We can now put everything together in one script.

# %%
url = 'https://music-to-scrape.org/user?username=StarCoder49&week=6'

header = {'User-agent': 'Mozilla/5.0'}
res = requests.get(url, headers = header)
res.encoding = res.apparent_encoding
soup = BeautifulSoup(res.text)

table = soup.find('table')

rows = table.find_all('tr')

for row in rows:
    data = row.find_all('td')
    
    if len(data)>0:
        song_name=data[0].get_text()
        artist_name=data[1].get_text()
        
        print(f'Song "{song_name}" by "{artist_name}"')

# %% [markdown]
# ### Exercise 4
#
# 1. Rather than printing the data to the screen, store it in a list of dictionaries, containing the following data points:
#     - song
#     - artist
#     - date
#     - username
#     - and time of data extraction.
# 2. Wrap your code in a function, that returns the dictionary from 1).

# %% [markdown]
# ### ✅ Solution - Exercise 4

# %% [markdown]
# Question 4.1

# %%
import time
from bs4 import BeautifulSoup
import requests

url = 'https://music-to-scrape.org/user?username=StarCoder49&week=36'

header = {'User-agent': 'Mozilla/5.0'}
res = requests.get(url, headers = header)
res.encoding = res.apparent_encoding
soup = BeautifulSoup(res.text)

table = soup.find('table')

rows = table.find_all('tr')

json_data=[]

for row in rows:
    data = row.find_all('td')

    if len(data)>0:
        song_name=data[0].get_text()
        artist_name=data[1].get_text()
        date=data[2].get_text()
        timestamp=data[3].get_text()
        json_data.append({'song_name': song_name,
                          'artist_name': artist_name,
                          'date': date,
                          'time': timestamp,
                          'timestamp_of_extraction': int(time.time()),
                          'username': url.split('=')[1]})
json_data


# %% [markdown]
# Question 4.2

# %%
def get_consumption_history(url):
    header = {'User-agent': 'Mozilla/5.0'}
    res = requests.get(url, headers = header)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text)
    
    table = soup.find('table')
    
    rows = table.find_all('tr')
    
    json_data=[]
    for row in rows:
        data = row.find_all('td')
    
        if len(data)>0:
            song_name=data[0].get_text()
            artist_name=data[1].get_text()
            date=data[2].get_text()
            timestamp=data[3].get_text()
            json_data.append({'song_name': song_name,
                              'artist_name': artist_name,
                              'date': date,
                              'time': timestamp,
                              'timestamp_of_extraction': int(time.time()),
                              'username': url.split('=')[1]})
    return(json_data)


# %%
# try running the function
get_consumption_history('https://music-to-scrape.org/user?username=StarCoder49&week=6')


# %%
# Check whether it also works for different weeks
get_consumption_history('https://music-to-scrape.org/user?username=StarCoder49&week=4')

# %% [markdown]
# ## 3.2. Loop through all weeks for each user
#

# %% [markdown]
# Alright - what have we achieve so far?
#
# - We've built a way to extract user names from the homepage of music-to-scrape.org ("seeds").
# - We just managed to extract a user's consumption history from a table displayed on the user's profile page.
#
# What's missing, though, is __ALL of a user's consumption data__, i.e., from __ALL possible weeks__.
#
# For this, we're making use of the "previous page" button.
#
# <img src="https://raw.githubusercontent.com/hannesdatta/course-odcm/master/content/docs/modules/week3/webscraping101/images/mits-previous-button.png" align="left" width=30%/>

# %% [markdown]
# __Let's try it out__
#
# Open the user's profile page at https://music-to-scrape.org/user?username=StarCoder49. __Click on the previous button__ a few times, and observe how the URL in your browser bar is changing. 

# %% [markdown]
# For example:
#
# - `https://music-to-scrape.org/user?username=StarCoder49`
# - `https://music-to-scrape.org/user?username=StarCoder49&week=37`
# - `https://music-to-scrape.org/user?username=StarCoder49&week=36`
# - `https://music-to-scrape.org/user?username=StarCoder49&week=35`
# - ...
#
# Can you guess the next one...?
#
# A general solution is to look up whether there is a `previous` button on the page (see HTML code below). We can then either "grab" the URL and visit it, or - instead - "click" on the button.
#

# %% [markdown]
# <img src="https://raw.githubusercontent.com/hannesdatta/course-odcm/master/content/docs/modules/week3/webscraping101/images/mts-previous-page.png" align="left" width=60% style="border: 1px solid black" />

# %% [markdown]
# So, let's write a snippet that "captures" the link of the previous page button! We always proceed in small steps.

# %%
# Step 1: Load the website's source code and convert to BeautifulSoup object
url = 'https://music-to-scrape.org/user?username=StarCoder49'

header = {'User-agent': 'Mozilla/5.0'}
res = requests.get(url, headers = header)
res.encoding = res.apparent_encoding
soup = BeautifulSoup(res.text)

# %%
# Step 2: Trying to locate the previous button, using a combination of class names and attribute-value pairs.
soup.find(class_='page-link', attrs={'type':'previous_page'})

# %%
# Step 3: Trying to extract the `href` attribute
soup.find(class_='page-link', attrs={'type':'previous_page'}).attrs['href']

# %%
# Step 4: Storing "previous page" link
previous_page_link = soup.find(class_='page-link', attrs={'type':'previous_page'}).attrs['href']
previous_page_link # print it

# %% [markdown]
# At each iteration, we can observe how we're getting closer to the information we need.
#
# Now, we only need to combine the base URL (`https://music-to-scrape.org/`) with the page number.

# %%
previous_page_link = soup.find(class_='page-link', attrs={'type':'previous_page'}).attrs['href']
f'https://music-to-scrape.org/{previous_page_link}'


# %% [markdown]
# ### Exercise 5
#
# __Setup__
#
# Please first load the snippet below, which has wrapped the "previous page" capturing in a function. Observe the use of `try` and `except`, which accounts for the last page NOT having a next page button.

# %%
def previous_page(soup):
    try:
        previous_page_link = soup.find(class_='page-link', attrs={'type':'previous_page'}).attrs['href']
        return(f'https://music-to-scrape.org/{previous_page_link}')
    except:
        return('no previous page')


# %% [markdown]
# Let's try out this function on the source code of the website.

# %%
soup = BeautifulSoup(requests.get('https://music-to-scrape.org/user?username=StarCoder49').text)
previous_page(soup)

# %% [markdown]
# See, it worked! Now, proceed with the exercises.
#
# __Questions__

# %% [markdown]
#
# 1. Make a web requests to 'https://music-to-scrape.org/user?username=StarCoder49&week=36', and pass on the (souped) object to the `previous_page()` function and observe the output. Then, use 'https://music-to-scrape.org/user?username=StarCoder49&week=0'. Is that what you expected? 
#
# 2. Write a while loop that continuously visits all pages for the user `StarCoder49`, by extracting previous page URLs from each page and continuing the data collection until there is no previous page to fetch. Start with week 10 to minimize server load.

# %%
# write your code here

# %% [markdown]
# ### ✅ Solution - Exercise 5
#
# Question 5.1

# %%
soup = BeautifulSoup(requests.get('https://music-to-scrape.org/user?username=StarCoder49&week=6').text)
previous_page(soup)


# %%
soup = BeautifulSoup(requests.get('https://music-to-scrape.org/user?username=StarCoder49&week=0').text)
previous_page(soup)
# returns "no previous page"

# %% [markdown]
# Question 5.2

# %%
# Question 2
urls = []

# define first URL to start from
url = 'https://music-to-scrape.org/user?username=StarCoder49&week=6'

while True:
    print(f'Opening {url} and checking for next page...')
    soup = BeautifulSoup(requests.get(url).text)
    previous_url = previous_page(soup)
    if 'no previous page' in previous_url: break
    url = previous_url


# %% [markdown]
# ------------
# So... seems like we're almost there!
#
# The only thing that's missing is to actually also extract the song consumption data from each of the user profile pages.
#
# We turn towards this issue next.

# %% [markdown]
# ## 3.3 Improving Extraction Design  
#
# ### 3.3.1 Timers  
#
# Sending too many requests at once can overload a server and get your IP blocked. Pausing between requests is essential to avoid this. We achieve this using the `time.sleep` function from the `time` package.
#
# __Try it out__  
#
# In Python, use the `time` module to pause execution. For example, after `time.sleep(2)`, the print statement runs only after a 2-second delay:  

# %%
# run this cell again to see the timer in action yourself!
import time
pause = 2
time.sleep(pause)
print(f"I'll be printed to the console after {pause} seconds!")

# %% [markdown]
# ### Exercise 6
#
# Modify the code above to sleep for 2 minutes. Go grab a coffee in-between. Did it take you longer than 2 minutes?
#
# (if you want to abort the running code, just select the cell and push the "stop" button!)

# %%
# your answer goes here!

# %% [markdown]
# ### ✅ Solution - Exercise 6
#

# %%
time.sleep(2*60)
print("Done!")

# %% [markdown]
# ### 3.3.2 Modularization  
#
# In scraping, many tasks must be repeated—like extracting all book links each time we open a new user page on *music-to-scrape.org*.  
#
# To make this easier, we’ll modularize our code into functions. This improves readability, reusability, and allows us to call the same code whenever needed. Need a refresher? Please revisit the Python Bootcamp!
#
# **Try it out**  
#
# Let’s complete our scraper by combining everything we’ve learned.  
#
# First, run the cell below to load the `get_users` function -- it extracts all currently visible user names from music-to-scrape.org's homepage. Then, continue with the exercises.  

# %%
import requests
from bs4 import BeautifulSoup

def get_users():
    url = 'https://music-to-scrape.org/'
  
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    
    soup = BeautifulSoup(res.text)
    
    relevant_section = soup.find('section',attrs={'name':'recent_users'})

    links = []
    for link in relevant_section.find_all("a"):
        if 'href' in link.attrs: 
            extracted_link = link.attrs['href']
            links.append(f'https://music-to-scrape.org/{extracted_link}')
    return(links) # to return all links

get_users()

# %% [markdown]
# ### Exercise 7
#
# Execute the function `get_users()` for a few minutes to collect a list of usernames. Store the user names in a JSON file (new-line separated), along with the timestamp of data retrieval `int(time.time())`.
#

# %%
# your answer here

# %% [markdown]
# ### ✅ Solution - Exercise 7
#

# %%
import time
import json

duration = 15 # for testing, just 15 seconds

# Calculate the end time
end_time = time.time() + duration

f = open('seeds.json','w') # start a new file with seeds, so, use `w` (write new file) instead of `a` (append to existing file)

# Run the loop until the current time reaches the end time
while time.time() < end_time:
    print(f'Scraping user names...')
    for user in get_users():
        new_user = {'url': user,
                    'timestamp': int(time.time())}
        f.write(json.dumps(new_user)+'\n')
    time.sleep(2)  # Sleep for a few seconds between each execution
f.close()
print('Done.')

# %%
# verify whether you can open the data

import json
f = open('seeds.json','r',encoding = 'utf-8')
data = f.readlines()
for item in data:
    print(json.loads(item))
f.close()

# %% [markdown]
# ### Exercise 8
#
#
# Now, let's write some code that loads `seeds.json`, and visit each user's __first profile page__ to extract consumption data. Remember to build in a little timer (e.g., waiting for 2 seconds or so). The prototype/starting code below stops automatically after 5 iterations to minimize server load. Try removing the prototyping condition using the comment character `#` when you think you're done!
#

# %%
# start from the code below

import time # we need the time package for implementing a bit of waiting time
import json

content = open('seeds.json', 'r').readlines() # let's read in the seed data

counter = 0 # initialize counter to 0

# loop through all lines of the JSON file
for line in content:
    # increment counter and check whether prototyping condition is met
    counter = counter + 1
    if counter>5: break # deactivate this if you want to loop through the entire file
        
    # convert loaded data to JSON object/dictionary for querying
    obj = json.loads(line)
    
    # show URL for which product information needs to be captured
    print(obj['url'])
    
    # eventually sleep for a second
    time.sleep(2)

print('Done!')

# %% [markdown]
# <div class="alert alert-block alert-info"><b>Tips</b>
#     <br>
#     <ul>
#         <li>
#             Use the function <code>get_consumption_history(url)</code> from exercise 4 above!
#         </li>
#  
# </div>
#

# %% [markdown]
# ### ✅ Solution - Exercise 8
#

# %%
# start from the code below
import time # we need the time package for implementing a bit of waiting time
import json

content = open('seeds.json', 'r').readlines() # let's read in the seed data

counter = 0 # initialize counter to 0

# loop through all lines of the JSON file
for line in content:
    # increment counter and check whether prototyping condition is met
    counter = counter + 1
    if counter>5: break # deactivate this if you want to loop through the entire file
        
    # convert loaded data to JSON object/dictionary for querying
    obj = json.loads(line)
    
    # show URL for which product information needs to be captured
    url = obj['url']

    print(f'Extracting information for {url}...')
    
    output_file = open('output_data.json','a')

    songs = get_consumption_history(url)

    for song in songs:
        output_file.write(json.dumps(song))
        output_file.write('\n')

    output_file.close()
    
    time.sleep(2)

print('Done!')

# %% [markdown]
# <div class="alert alert-block alert-info"><b>Tip: Understanding the Difference Between <code>'a'</code> and <code>'w'</code> When Writing Files in Python</b>
#     <br>
#     
# - When working with files in Python, it's essential to know the difference between <code>'a'</code> and <code>'w'</code>  when opening them.
# - <code>'a'</code> stands for "append" mode. When you open a file with <code>'a'</code> , Python will let you add data to the end of the existing file without erasing its contents. This is useful when you want to add new information to a file without losing what's already there. It's like adding new lines to the end of an ongoing document.
# - <code>'w'</code>  stands for "write" mode. When you open a file with <code>'w'</code> , Python will create a new file or overwrite an existing one. This means that if the file already has data in it, using <code>'w'</code>  will erase all the existing content and start fresh. It's like creating a new document or wiping out the old one.
# - Remember, when scraping data or working with files, it's generally safer to use <code>'a'</code>. This way, you won't accidentally delete valuable data. Using <code>'w'</code>  should be done with caution, and only when you intentionally want to start with a clean slate or create a new file altogether.
# </div>

# %% [markdown]
# Finally, we can re-open the extracted data in Python to see whether what we retrieved seems complete.
#
# Verify you've the `pandas` package installed by running the next cell.

# %%
# !pip install pandas

# %% [markdown]
# Now, we can load the data.

# %%
# inspect data in pandas
import pandas as pd
pd.read_json('output_data.json', lines=True)

# %% [markdown]
# # 4. Wrap-up
#
# Congratulations - You’ve built your first **complete static web scraper**! 🎉  
#
# Starting from a single page, you learned how to:
#
# - Inspect a web page and figure out where the data lives  
# - Extract text and attributes using `BeautifulSoup`  
# - Loop through multiple pages automatically  
# - Add polite pauses to avoid overloading websites  
# - Save your results as JSON and convert to CSV for later use  
#
# These are the same core steps behind almost every real-world scraping project,
# from small personal analyses to larger automated data collections.
#
# In the next tutorial, **Web Scraping Advanced**, we’ll take the next step:
# working with **dynamic websites** — those that only load their content
# after scrolling, clicking, or interacting with the page.
