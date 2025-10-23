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
# # Web data for dummies (in-class)
#
# *(updated on 31 January 2025)*
#
#
# *The internet offers abundant possibilities to collect data for use in empirical research projects. This tutorial is a gentle introduction on how web scraping and APIs to collect such data in Python. Get inspired now!*
#
# ## Learning Objectives
#
# After completion of this tutorial, students will be able to:
#
# * Explain the differences between retrieving data from websites vs. APIs
# * Retrieve web data in Python using the `requests` library, and store retrieved data in HTML or JSON/TXT files for further inspection.
# * Use browser control tools ("inspect") to develop strategies how to select and capture information from websites (e.g., text, numbers, pictures, etc.)
# * Select elements from websites using BeautifulSoup (e.g., class names, attribute or tag names)
# * Select elements from JSON dictionaries obtained through APIs (attribute-value pairs)
# * Apply programming concepts (e.g., loops, functions) to the collection of web data, and convert dictionaries to JSON files.
# * Understand the difference between Jupyter Notebooks and “raw” Python files, and run collection via the command line/terminal
#
# <div class="alert alert-block alert-info"><b>Support Needed?</b> 
#     For technical issues outside of scheduled classes, please check the <a href="https://odcm.hannesdatta.com/docs/course/support" target="_blank">support section</a> on the course website.
# </div>
#
# ## What to expect in this tutorial
#
# The two main methods for retrieving web data are **web scraping** and **APIs**. This tutorial covers both approaches, and concludes with exercises.
#
# ### Web Scraping &rarr; Part 1
# Web scraping involves extracting information from __publicly available websites__ by analyzing their HTML structure. It is useful when:
#
# - No API is available for the data you need.
# - The website provides information in a structured format (tables, lists, etc.).
# - You want to extract elements like text, numbers, images, or links.
#
# ### APIs (Application Programming Interfaces) &rarr; Part 2
# APIs provide a structured way to retrieve data directly from a website's backend. Instead of scraping HTML, APIs return data in machine-readable formats (e.g., JSON, XML). APIs are preferable when:
#
# - The website offers a well-documented API.
# - You need structured data that is easier to process.
# - The website enforces rate limits or terms that prohibit scraping.
#
# ### Exercises &rarr; Part 3
#
# This tutorial concludes with an exercise in which you can put your newly gained skills into practice.
#
#
# ------

# %% [markdown]
# ---
#
# ## Part 1: Web Scraping
#
# ### 1.1 What is web scraping?
#
# Say that you want to capture and analyze data from a website. Of course, you could simply copy-paste the data from each page. But, of course, this manually executed job would have severe limitations. What if the data on the page gets updated (i.e., would you have time available to copy-paste the new data, too)? Or what if there are simply so many pages that you can't possibly do it all by hand (i.e., thousands of product pages)? 
#
# Web scraping can help you overcome these issues __by programmatically extracting data from the web__. Before we can extract/grab/capture/scrape information from a website, we need a bit of background on how websites work technically, so let's focus on that first.
#

# %% [markdown]
# __The web data workflow__
#
# Usually, web scrapers consist of four "shells", that are gradually developed to complete a webscraping project (Guyt et al. 2024). 
#
# <img src="framework_guyt2024.png" width="40%">
#
# These shells consist of:
#
# 1. *extract*: Build computer code to extract the data from the website
# 2. *loop*: Build a loop to extract data for multiple products, users, etc.
# 3. *schedule*: schedule the data collection, e.g., to run every day or week
# 4. *infrastructure*: run scrapers on local (i.e., your own) or remote (e.g., in the cloud) infrastructure.
#
# Along with these steps, researchers also __select data sources__, an often underappreciated step in collecting web data (Boegershausen et al. 2022).
#
# <div class="alert alert-block alert-info"><b>Tip:</b>
# Curious about the "real" web data workflow (which is much more comprehensive then what is here? Start getting familiar with it early on by reading <a href="https://journals.sagepub.com/doi/10.1177/00222429221100750">"Fields of Gold"</a> (you've got to know this paper inside out by the end of this course...).
# </div>

# %% [markdown]
# ### 1.2 How websites work
#
# #### Importance
#
# It's vital to take some time to get familiar with HTML - the primary programming language used when building websites. Once we're familiar with HTML (and the structure of websites), we can rapidly navigate complex websites to extract the information we're interested in (e.g., prices, names of product categories, ...). In other words: to reach our end goal, we do have to give you some technical details first.
#
# So, here we go: A web page consists of various text files, each one with its style, formatting, and syntax. These files each serve a specific purpose:
#
# - `.html` (HyperText Markup Language) files give structure to a page (e.g., where's the menu?, which content to show (e.g., text, tables)?)
# - `.css` (Cascading Style Sheet) files determine how the page looks (e.g., which color do headers have? what's the font used for text in a paragraph?)
# - `.js` (JavaScript) files add interactivity (e.g., button animations)
#
# #### Let's try it out
# Check out this simple [example](https://codepen.io/rcyou/pen/QEObEk/). The site shows the source code of a site (`.html`, `.css`, and `.js`) in an online editor, along with a rendered ("viewable") version of the site. Once you make changes to the code, the site gets automatically updated.
#
# <img src="https://raw.githubusercontent.com/hannesdatta/course-odcm/master/content/docs/modules/week2/webdata-for-dummies/images/codepen.png" align="left" width=60%/>
#

# %% [markdown]
# #### Exercise 1.1 
# Just to get a feeling for how things work, let's make the following changes in the [CodePen snippet](https://codepen.io/rcyou/pen/QEObEk/): 
# 1. Change the text between the `<h1>` tags to `I am a purple of size 3em`. 
# 2. Change the `h1` font-size to `3em` and the color to purple (add `color: purple;` below `margin-bottom`).  
# 3. Remove the JavaScript code. What happens now when you click the blue button?
#
#
# #### Solutions
# Clicking the button should no longer trigger the script to hide the paragraph text.
#
# <img src="https://raw.githubusercontent.com/hannesdatta/course-odcm/master/content/docs/modules/week2/webdata-for-dummies/images/purple_headline.png" align="left" width=60%/>
#
#

# %% [markdown]
# ### 1.3 Advancing HTML skills
#
# #### Importance
#
# Most HTML elements are represented by a pair of tags - an opening tag and a closing tag. 
#
# For example, a table starts with `<table>` and ends with `</table>`. The first tag tells the browser: "Hey! I got a table here! Render it as a table, so it displays nicely on the site." The closing tag (note the forward-slash!) tells the browser: "Hey! I'm all done with that table, thanks." Inside the table are nested more HTML tags representing rows (`<tr>`) and cells (`<td>`).
#

# %% [markdown]
# ```html
# <html>
#     <table id="example-table" class="striped-table" style="width: 95%">
#         <tr> <!-- Header row, starting with <tr> -->
#             <td>Column A</td> <!-- Columns, starting with <td> -->
#             <td>Column B</td>
#         </tr> <!-- observe that we always "close a row" to indicate we're done -->
#         <tr> <!-- Row 1 --->
#             <td>Row 1, Column A</td>
#             <td>Row 1, Column B</td>
#         </tr>
#         <tr> <!-- Row 2 --->
#             <td>Row 2, Column A</td>
#             <td>Row 2, Column B</td>
#         </tr>
#     </table>
# </html>
# ```

# %% [markdown]
# This what the rendered HTML table looks like:

# %% [markdown]
# <html>
#     <table id="example-table" class="striped-table" style="width: 95%">
#         <tr> <!-- Header -->
#             <td>Column A</td>
#             <td>Column B</td>
#         </tr>
#         <tr> <!-- Row 1 --->
#             <td>Row 1, Column A</td>
#             <td>Row 1, Column B</td>
#         </tr>
#         <tr> <!-- Row 2 --->
#             <td>Row 2, Column A</td>
#             <td>Row 2, Column B</td>
#         </tr>
#     </table>
# </html>

# %% [markdown]
#
# HTML elements can have any number of
#
# - __attributes__, such as IDs, which sometimes (but not always) *uniquely* identify elements
#
# ```html
# <table id="example-table">
# ```
#
# - __classes__, which identify a *type* of an element (but barely uniquely identify a unique element -- i.e., they are mostly used more than once)
#
# ```html
# <table class="striped-table">
# ```
#
# - and __styles__, which define how specific elements *appear* (e.g. the width of the table)
#
# ```html
# <table style="width:95%;">
# ```
#
# As you may already have noticed, we use spaces (or tabs) to separate the elements from one another (the geeks among us will call this "indentation") to provide structure and improve readability. Yes, that's right. *Improve readability*.
#
# Code may look complex to read at first, but when you take a closer look at it, it boils down to simple English, following a particular structure (also known as syntax). For example, the `<table>` tag is placed farther to the right than the `<html>` tag indicates that the table is nested within the HTML block.
#
# This may be a lot to take in if you're entirely new to HTML, but don't worry, as the goal of this section is not to teach you how to code from scratch but rather to teach you what HTML is and why it is relevant for web scraping.
#
# <div class="alert alert-block alert-info"><b>Why are attributes and classes important?</b> 
# Recall that we use webscraping to "capture" content from websites. But - not all of the content will be relevant. We require attributes and classes to "select" content that we want to save. 
# </div>
#

# %% [markdown]
# __Let's try it out__
#
# Double-click on the rendered table below to edit its HTML structure. Try to change some simple things, e.g., the text. Rerun the cell (Shift + Enter, or click the Run button in Juypyter Notebook). Watch your changes come alive!
#

# %% [markdown]
# #### Exercise 1.2
#
# Please finish the exercises below. After each change, rerun the cell.
#
# 1. Add another row in the table above to become a 2 (columns) x 4 (rows) table. That is 3 regular rows and 1 table header row.
# 2. Fill the cells with the corresponding text labels (e.g., Row 3, Column A). 
# 3. Change the table width to `50%` so that the table becomes narrower.
#
#
# <div class="alert alert-block alert-info"><b>Proceed in small steps!</b> 
# Try not to make too many changes at once. Always proceed in small steps to see whether your code still works!
# </div>
#

# %% [markdown]
# *Make your changes here:*

# %% [markdown]
# <html>
#     <table id="example-table" class="striped-table" style="width: 95%">
#         <tr> <!-- Header -->
#             <td>Column A</td>
#             <td>Column B</td>
#         </tr>
#         <tr> <!-- Row 1 --->
#             <td>Row 1, Column A</td>
#             <td>Row 1, Column B</td>
#         </tr>
#         <tr> <!-- Row 2 --->
#             <td>Row 2, Column A</td>
#             <td>Row 2, Column B</td>
#         </tr>
#     </table>
# </html>

# %% [markdown]
# **Solutions**
# <html>
#     <table id="example-table" class="striped-table" style="width: 50%">
#         <tr> <!-- Header -->
#             <td>Column A</td>
#             <td>Column B</td>
#         </tr>
#         <tr> <!-- Row 1 --->
#             <td>Row 1, Column A</td>
#             <td>Row 1, Column B</td>
#         </tr>
#         <tr> <!-- Row 2 --->
#             <td>Row 2, Column A</td>
#             <td>Row 2, Column B</td>
#         </tr>
#         <tr> <!-- Row 3 --->
#             <td>Row 3, Column A</td>
#             <td>Row 3, Column B</td>
#         </tr>
#     </table>
# </html>

# %% [markdown]
# --- 
# ### 1.4 Finding content in a website's source code
#
# #### Importance
#
# Alright, we've now covered tables (`<table>`). However, there are hundreds of different tag words in HTML, and it's impossible to memorize all of them. That's why developers use a pretty handy tool to *inspect the source* of a website directly in the browser. From now onwards, we recommend you to use Chrome (in Safari and Firefox, things look slightly different, and we can't cover those, unfortunately.)
#
# Suppose you have identified an element you want to capture (e.g., a price or the name of a product). You can "ask" your browser for the specific HTML tag of that object (so it becomes easier to capture that element later). 
#
# #### Let's try it out 
#
#
# How does it work? Start by inspecting specific elements on the page by *right-clicking on the page* and selecting __"Inspect"__ from the context menu that pops up. Then, hover over elements in the "Elements" tab to highlight them on the page. This can be super helpful when you're trying to figure out how to (uniquely) identify the element you want to scrape.
#
# Check out the HTML structure of this fictitious [music streaming platform](https://music-to-scrape.org). The site displays the most frequently listened to songs, featured artists, and a selection of the platform's most recently active users. You can click through to subsections of the site, learning more about artists, songs, and users. Note that the data has been randomly generated, so the figures on your screen may deviate from the ones below.
#

# %% [markdown]
# <img src="https://raw.githubusercontent.com/hannesdatta/course-odcm/master/content/docs/modules/week2/webdata-for-dummies/images/music-to-scrape-inspect.png" align="left" width=80%/>

# %% [markdown]
# In the screenshot above, we've selected the artist "Russell Malone," right-clicked on it, and chose "Inspect." The same text is highlighted in blue in the HTML code below. 
#
# __Try it out yourself!__
#
# The `<h2>` and `</h2>` tags surrounding the artist's name indicate that this text is a (sub)header on the web page. Move your pointer down to the line below (`<div class="about_artist">`), and you'll see that on the top screen, it now highlights the artist's location and number of plays (rather than the name). This way, you can quickly investigate any webpage. 
#
# __Also try this out...!__
#
# As we discussed earlier, tags can be nested within other tags. This also becomes clear from the screenshot below, in which the small gray triangles (▶) indicate that there is code hidden within these blocks. Click on them to expand the code, see what's inside, and click again to collapse them.
#

# %% [markdown]
# <img src="https://raw.githubusercontent.com/hannesdatta/course-odcm/master/content/docs/modules/week2/webdata-for-dummies/images/music-to-scrape-tags.png" align="left" width=50%/>

# %% [markdown]
# #### Exercise 1.3
# 1. Use the inspect tool to find the HTML element that constitutes the table header "**Top 10 songs of all time**" at the bottom of [this page](https://music-to-scrape.org/artist?artist-id=AR7KKE01187FB3D87B).
# 2. Look up how many elements in that table start with a new row, using the HTML tag word `tr` (within the Inspector screen, use `Ctrl+F` on a PC or `⌘+F` on Mac to search)
# 3. You can make local (only on your computer) changes to the web page by double-clicking in the inspector and swapping the code for something else (yes, you can overwrite what's already written there!). Change the name of the artist or the number of plays.
# 4. After making the changes in 3.), refresh the page (reload it). What happens (and why)?
#
# *"Faked" location and plays.*
#
# <img src="https://raw.githubusercontent.com/hannesdatta/course-odcm/master/content/docs/modules/week2/webdata-for-dummies/images/music-to-scrape-fake.png" width=40% align="left"  style="border: 1px solid black"/>
#

# %%
# your answer goes here!

# %% [markdown]
# #### Solutions
# 1. The `<table>` (table header) tags with the class `top-songs`.
# 2. At the time of writing, two elements point to rows (`tr`) – one being the header, another one being the actual data.
# 3. See screenshot. 
# 4. Once you refresh the page, the original (unedited price and star rating) appears again.
# ---
#

# %% [markdown]
# ### 1.5 Loading a website's source code into Python
#
# #### Importance
#
# Alright. Up to this moment, we've learned about HTML and fiddled around with a website's source code. But we finally want to understand how we can load a website's source code into Python.
#
# Rather than (manually) using the Inspector, we now automate these tasks using Python's `requests` library. Libraries are "extensions" to Python, but most of them are not loaded by default. So let's import the library using `import requests`.

# %% [markdown]
# #### Let's try it out

# %% [markdown]
# Please (re)run the code cell below.

# %%
import requests

# make a get request to the web site
url = 'https://music-to-scrape.org/artist?artist-id=AR7KKE01187FB3D87B'
header = {'User-agent': 'Mozilla/5.0'} # with the user agent, we let Python know for which browser version to retrieve the website
web_request = requests.get(url, headers = header)
web_request.encoding = web_request.apparent_encoding # set encoding to UTF-8 -- ensuring non-English characters can be read well

# return the source code from the request object
web_request_source_code = web_request.text

# print out the source code to verify you have loaded the correct page
print(web_request_source_code)

# %% [markdown]
# <div class="alert alert-block alert-info"><b>Why are we using "user agents" when making website requests?</b>
#     <br>
#
# - User agents tell a browser which website version to return. For example, your smartphone's browser will request mobile versions of websites, whereas your laptop will request versions suited to larger screens.
#     
# - Changing the user agent is also your "first wall of defense" when being blocked during data collections. Later, we will learn about other ways to prevent being blocked from automatically extracting information from the web. 
#     
# - Interested in the ethical aspects of retrieving publicly available web data? Check the relevant sections in ["Fields of Gold"](https://journals.sagepub.com/doi/abs/10.1177/00222429221100750?journalCode=jmxa).
#  
# </div>
#

# %% [markdown]
# #### Exercise 1.4
# 1. Using the code snippet above, write a function (starting with `def download_website(url):`) that downloads the raw website data for [this artist](https://music-to-scrape.org/artist?artist-id=AR7KKE01187FB3D87B), printing it to the screen. Remember to use the same number of spaces or tabs ("indents") when writing your function!
# 2. Adapt the function (copy-paste first, relabel as `def save_website(url, filename):`), storing the website's raw code __in a file__ (that you can specify in the second parameter, `filename`). Recall that you can use previously learned concepts, in specific `f=open(<filename>, 'w', encoding='utf-8')`, `f.write()`, and `f.close()`. Rerun the function on the URL above. Does it work?
# 3. Write a loop to store the raw HTML source code for all featured artists on the platform's homepage (listed under "Featured artists" at [https://music-to-scrape.org](). Before starting, create an array/list of *dictionaries* (`artists`) with URLs and filenames to store the websites. Use the previously written function `store_website(url, filename`) for this exercise.
#
# ```
# artists = [{'url': 'first_url',
#          'filename': 'filename1.html'},
#         {'url': 'second_url',
#          'filename': 'filename2.html'}]
# ```
#          
#          
#

# %%
# start with your code here

# %% [markdown]
# #### Solutions 

# %%
# Q1
import requests

def download_website(url):
    header = {'User-agent': 'Mozilla/5.0'} # with the user agent, we let Python know for which browser version to retrieve the website
    request = requests.get(url, headers = header)
    request.encoding = request.apparent_encoding # set encoding to UTF-8
    source_code = request.text
    print(source_code)

download_website('https://music-to-scrape.org/artist?artist-id=AR7KKE01187FB3D87B')

# %%
# Q2
import requests

def save_website(url, filename):
    header = {'User-agent': 'Mozilla/5.0'} # with the user agent, we let Python know for which browser version to retrieve the website
    request = requests.get(url, headers = header)
    request.encoding = request.apparent_encoding # set encoding to UTF-8
    source_code = request.text
    f=open(filename, 'w', encoding='utf-8')
    f.write(source_code)
    f.close()
    print(f'Done retrieving {url} and saving as {filename}')

save_website('https://music-to-scrape.org/artist?artist-id=AR7KKE01187FB3D87B', 'website.html')

# %%
# Q3
artists = [{'url': 'https://music-to-scrape.org/artist?artist-id=AR7KKE01187FB3D87B',
         'filename': 'filename1.html'},
        {'url': 'https://music-to-scrape.org/artist?artist-id=ARGNGRI11E2835D567',
         'filename': 'filename2.html'},
        {'url': 'https://music-to-scrape.org/artist?artist-id=ARAVPU21187B993957',
         'filename': 'filename3.html'},
        {'url': 'https://music-to-scrape.org/artist?artist-id=ARJ66JQ1187B99D2FF',
         'filename': 'filename4.html'}
       ]

for artist in artists:
    save_website(artist['url'], artist['filename'])

# %% [markdown]
# ---
# ### 1.6 Extracting information from a website's source code using `BeautifulSoup` 
#
# #### Importance
#
# It's useful to store raw data from websites (we will make use of this a lot). But &#150; how can extract specific information from a website, such as a product's title or price? 
#
# Fortunately, we can make use of the *structured* nature of HTML, by selecting information on the basis of:
#  
# - tags (e.g., `<h1>`, `<table>`),
# - attributes 
#     - such as IDs (e.g., `<table id="example-table">`), 
#     - class names (e.g., `<table class="striped-table">`), or
#     - or (generic) attribute-value pairs (e.g., `<table data-gr-ext-installed="test">`).
#     
# For now, we'll show you how to apply these concepts using *BeautifulSoup*, a fantastic Python library that allows you to navigate and extract data from HTML files. BeautifulSoup does NOT gather information from the web itself (for this, we still use `requests`, as above). 
#
# #### Let's try it out
# First, we import the package `BeautifulSoup` and turn the `web_request_source_code` (the HTML code from the website) into BeautifulSoup object. Once converted, we can easily navigate the code by *tag names*, *attribute names*, or *class names*. This process is called __parsing__, and is one of the central tasks in web scraping.
#
# Since we know that the artist name is surrounded by `<h2>` tags (see Google Inspector screenshot above), we use `soup.find('h2')` to parse the name of the artist.
#
# Please run the following cells to see things in action!
#

# %%
from bs4 import BeautifulSoup

soup = BeautifulSoup(web_request_source_code)

print(soup.find('h2'))

# %% [markdown]
# The `.find()` method will always print out the first matching element it finds. In the case of an artist's location, though, all we get when looking for `h5` is this:

# %%
print(soup.find('h5'))

# %% [markdown]
# ...while the location we're interest in is sitting in the "next" `p` element:
# ```
# <h5>Location:</h5>
# <p>Albany GA</p>
# ```

# %% [markdown]
# We can "jump" to the next element using the `.findNext()` function. Check this out:

# %%
print(soup.find('h5').findNext('p'))

# %% [markdown]
# Great, right? We can now locate information easily on the site. But... wait a second. Inspecting the site a little closer reveals that the web page has multiple `<h5>` elements, which contain the "Location" and "Number of plays." But only the first one will be returned by `.find()`:

# %% [markdown]
# To capture __all__ matching `<h5>` elements you use the `find_all()` method like this:

# %%
print(soup.find_all('h5'))

# %% [markdown]
# Note that it now returns a list of elements (`[element1, element2]`), so to access individual elements you need to apply indexing (which starts with [0] for the first elements, [1] for the second and so on...).

# %%
# obtain first h2 element 
print(soup.find_all('h5')[0].findNext('p'))

# obtain second h2 element
print(soup.find_all('h5')[1].findNext('p'))

# we can also count the number of elements returned, using the len() function
print(len(soup.find_all('h5'))) # will return 5 - as the 'h5' is also used for the styling of other sections of the website

# %% [markdown]
# Both subheaders are still surrounded by `<hp>` and `</p>` tags. To get rid of them, append `.get_text()` to your code:

# %%
# sub header without HTML tags
print(soup.find_all('h5')[0].findNext('p').get_text())

# %% [markdown]
# #### Exercise 1.5
#
# 1. Retrieve the website's source code, and parse the following information (and print them out):
#     - artist name
#     - artist location,
#     - total number of plays, and
#     - the number of songs in the "top 10" table
#     
#
# <div class="alert alert-block alert-info"><b>Tips</b>
#     <br>
# <ul>
#     <li>To extract information using <b>class names</b>, use the <code>class_</code> argument in the <code>find()</code> function.<br>
#         <b>Example:</b> <code>soup.find(class_ = 'class_name_to_find)</code>
#     </li><br>
#     <li>Information can also be captured using using <b>attribute-value pairs</b>. Simply use the <code>attrs</code> argument in the <code>find()</code> function.<br>
#         <b>Example:</b> <code>soup.find(attrs = {'class': 'class_name_to_find'})</code>
#     </li><br>
#     <li>Sometimes, you would like to extract the <b>value of a particular attribute</b>. You can do so using the <code>attrs</code> attribute of the <code>find()</code> function.<br>
#         <b>Example:</b> <code>soup.find(class_ = 'class_name_to_find').attrs['attribute_to_extract']</code>
#     </li><br>
#     <li>You can also extract information by <b>counting</b> the number of classes. For example, <code>len(soup.find('h2'))</code> returns the number of <code>h2</code> elements on a site.
#     </li><br>
#     <li>
#         Too much whitespace surrounding your parsed information? Use Python's <code>strip()</code> function, e.g., <code>'   too much whitespace    '.strip()</code>.
#     </li>
# </ul>
#  
# </div>

# %%
# your answer goes here!

# %% [markdown]
# #### Solutions

# %%
# artist name
print(soup.find('h5').get_text())
# location
print(soup.find(class_ = 'about_artist').findNext('p').get_text())
# plays
print(soup.find(class_ = 'about_artist').find_all('h5')[1].findNext('p').get_text())
# number of songs
song_table = soup.find(class_ = 'top-songs')
print(len(song_table.find_all('tr'))-1)


# %% [markdown]
# Remember that it is really important that you build your code from the END to the BEGINNING (think of it like an onion). 
# For example, to arrive at the solution above for the __number of plays__, I would gradually build my code like this - and check, at every iteration, whether my code still runs.

# %%
# attempt 1: 
soup.find(class_='about_artist')

# %%
# attempt 2: trying to get the second element
soup.find(class_='about_artist').find_all('h5')

# %%
# attempt 3: entering the "second" (Python = 1st) element
soup.find(class_='about_artist').find_all('h5')[1]

# %%
# attempt 4: using the "find next" function to get to the next "p"
soup.find(class_='about_artist').find_all('h5')[1].findNext('p')

# %%
# attempt 5: extracting the text and printing it
print(soup.find(class_='about_artist').find_all('h5')[1].findNext('p').get_text())

# %% [markdown]
# Please always adhere to this step-by-step ("onion-style") approach to writing code. That way, at each "attempt", you can check whether your code still runs. Writing code from scratch (e.g., what I have written above) is impossible for beginners.

# %% [markdown]
# ### 1.7 Writing your complete first web scraper

# %% [markdown]
# __Exercise 1.6__
#
# Now it's time to put in action everything we have learnt so far.
#
# - Use the list of four URLs specified above to start your data collection,
# ```
#   artists = [{'url': 'https://music-to-scrape.org/artist?artist-id=AR7KKE01187FB3D87B',
#          'filename': 'filename1.html'},
#         {'url': 'https://music-to-scrape.org/artist?artist-id=ARGNGRI11E2835D567',
#          'filename': 'filename2.html'},
#         {'url': 'https://music-to-scrape.org/artist?artist-id=ARAVPU21187B993957',
#          'filename': 'filename3.html'},
#         {'url': 'https://music-to-scrape.org/artist?artist-id=ARJ66JQ1187B99D2FF',
#          'filename': 'filename4.html'}]
#        
#   ```
# - Write a loop that stores the raw website data in separate HTML files (storing raw data for diagnostic purposes is very helpful!), 
# - Store the extracted information (artist name, location, number of plays, number of songs) in a dictionary, that is stored in new-line separated JSON files.
#
# <div class="alert alert-block alert-info"><b>Tips</b>
#     <br>
#     <ul>
#         <li>
#     Copy-paste and then modify the <code>store_website()</code> function from above to handle the two tasks of storing AND extracting information ("parsing"). </li>
#             <li>Make use of the <code>return()</code> argument in a function to return the parsed data in a dictionary. </li>
#         <li>
#             You can import the json package (<code>import json</code>) and use the <code>json.dumps()</code> function to convert the dictionary to writable output data.
#         </li>
#  
# </div>
#

# %%
# write your code here

# %% [markdown]
# __Solution__

# %%
import requests
from bs4 import BeautifulSoup
import json

artists = [{'url': 'https://music-to-scrape.org/artist?artist-id=AR7KKE01187FB3D87B',
         'filename': 'filename1.html'},
        {'url': 'https://music-to-scrape.org/artist?artist-id=ARGNGRI11E2835D567',
         'filename': 'filename2.html'},
        {'url': 'https://music-to-scrape.org/artist?artist-id=ARAVPU21187B993957',
         'filename': 'filename3.html'},
        {'url': 'https://music-to-scrape.org/artist?artist-id=ARJ66JQ1187B99D2FF',
         'filename': 'filename4.html'}]
       

def parse_website(url, filename):
    header = {'User-agent': 'Mozilla/5.0'} 
    request = requests.get(url, headers = header)
    request.encoding = request.apparent_encoding # set encoding to UTF-8
    source_code = request.text
    f=open(filename, 'w', encoding='utf-8')
    f.write(source_code)
    f.close()
    
    # make information "extractable" using BeautifulSoup
    soup = BeautifulSoup(source_code)
    
    artist_name = soup.find('h2').get_text()
    location = soup.find(class_ = 'about_artist').find_all('p')[0].get_text()
    plays = soup.find(class_ = 'about_artist').find_all('p')[1].get_text()
    
    song_table = soup.find(class_ = 'top-songs')
    number_of_songs = len(song_table.find_all('tr'))-1

    data = {'artist': artist_name,
            'location': location,
            'plays': int(plays),
            'number_of_songs': int(number_of_songs)} # convert plays to a numeric
    
    print(f'Done retrieving {url} and saving as {filename}')
    
    return(data)


f=open('artist_data.json', 'w', encoding='utf-8')
for artist in artists:
    data = parse_website(artist['url'], artist['filename'])
    f.write(json.dumps(data))
    f.write('\n') # new line to separate objects
f.close()
    

# %% [markdown]
# ### 1.8 Wrapping up

# %% [markdown]
# Congrats! You've just learned the first steps in collecting online data from websites! Along with boosting your "geek"-factor (wait till you show this to your friends!), you've gained an intuition on how websites are built up (HTML, CSS, JS), how source code translates into a rendered (visual) website (or, in other words, you know how to spoof websites - now, take screenshots and show *that* to your friends...), how websites can be loaded into Python, and how you can use `BeautifulSoup` to extract information using tag or attribute names and classes. Good job!

# %% [markdown]
# --- 
#
# ## 2. Application Programming Interfaces (APIs)
#
#
# ### 2.1 What is an API?
#
# An equally important data collection method is called Application Programming Interface (API). That's a mouthful, but in essence, it is nothing more than a version of a _website intended for computers, rather than humans, to talk to one another_. 
#
# APIs are everywhere, and most are used to provide...
# - data (e.g., retrieve a user name and demographics), 
# - functions (e.g., start playing music from Spotify, turn on your lamps in your "smart home"), or 
# - algorithms (e.g., submit an image, retrieve a written text for what's *on* the image).
#
# ---
#
# *Background: Free versus paid APIs*
#
# Paid APIs require their users to authenticate themselves. Think of an authentication key as a "key to unlock the service." Web services use such authentication keys to track whether you're allowed to use the API and how much you use it. This offers numerous opportunities for API business models, in which, for example, the service employs a pay-by-request (or by 1,000 requests) model. For example, check how to pay for the API of Chat GPT -- see https://platform.openai.com/docs/introduction.
#
# ---
#
# In what follows, we'll introduce you to the API of [music-to-scrape.org](), our fictitious "streaming service". Just with any API, it has documentation that shows you what "endpoints" exist (think of them as websites) and what data they return (think of it like the information you've scraped earlier).
#
# Check out the [documentation of the API](https://api.music-to-scrape.org/docs) now!
#
# <img src="https://raw.githubusercontent.com/hannesdatta/course-odcm/master/content/docs/modules/week2/webdata-for-dummies/images/music-to-scrape-api.png" width=60% align="left"  style="border: 1px solid black"/>
#
#

# %% [markdown]
# ### 2.2 How APIs work

# %% [markdown]
# __Importance__
#
# APIs work very similar to websites. At the core, instead of obtaining the source code of a (rendered) web site, you obtain code that computers can easily understand to process the content of a website. APIs provide you with simpler and more scalable ways to obtain data, so you really have to understand how they work.
#
# __Let's try it out__
#
# Consider the screenshot below (a view of the music-to-scrape website). 
#
# <img src="https://raw.githubusercontent.com/hannesdatta/course-odcm/master/content/docs/modules/week2/webdata-for-dummies/images/featured_artists.png" width=60% align="left"  style="border: 1px solid black"/>
#

# %% [markdown]
# Here's an example of the output of the music-to-scrape API (click on it to view it in your browser):
#
# https://api.music-to-scrape.org/artists/featured
#
# <img src="https://raw.githubusercontent.com/hannesdatta/course-odcm/master/content/docs/modules/week2/webdata-for-dummies/images/featured_artists_api.png" width=40% align="left"  style="border: 1px solid black"/>

# %% [markdown]
# *A few things stand out right away:*
#
# - the output only contains text, which is structured according to a data structure (e.g., array or list (`[]`) and dictionary (`{}`)), 
# - there's no human interface with buttons, menus, and links, yet...
# - you can access it like any other website by filling out the URL in your browser (`api.music-to-scrape.org/artists/featured`) in this example).
#
# The API output above corresponds to the (visual) website, which you can open at [music-to-scrape.org](), scrolling down to the "featured artists" section. 
#
#

# %% [markdown]
# <div class="alert alert-block alert-info"><b>Tips:</b><br>
# <ul>
#     <li>If you have taken a look at the API output, you may conclude that making sense of raw JavaScript Object Notation (JSON) is easier said than done. Fortunately, this <a href='https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh'>plugin</a> automatically formats and highlights the output such that it's easier to digest. If your browser does not automatically display JSON data in a "nice" way, we recommend installing the Chrome plugin. 
#     </li>
#     <li>
# After installation, view the output again. That's much better, right?
# </li>
#     </ul>
# </div>
#
#
#
#

# %% [markdown]
# #### Exercise 2.1
#
# Navigate through the JSON tree structure of the featured artists data and anwer the following questions:
#
# 1. At the parent level, you find a __list of dictionaries__. Describe in your own words what each dictionary represents. How does it relate to the music-to-scrape website?
# 2. Refresh the API endpoint several times (reload the page in your browser). What happens? 
#
# 3. Suppose you would like to store, along with the information from the API endpoint, the date and time each featured artist was retrieved. How could you do that?
#
# <div class="alert alert-block alert-info"><b>Tips:</b><br>
#    <ul> <li>
# Times are often registered in UTC format, a globally interchangeable time representation (also known as Epoch time). More specifically, it is the number of seconds elapsed since January 1, 1970. It can be used as a universal time scale around the world. 
#     </li>
#     <li>
#     Copy-paste the UTC time to an <a href='https://epochconverter.com' target='_blank'>online epoch converter</a> and check whether it corresponds with the date and time on the webpage.
#     </li>
#     </ul>
# </div>
#
#
#
#
#

# %% [markdown]
# **Your answer**  

# %% [markdown]
# ...

# %% [markdown]
# #### Solutions
# 1. The "artist" node holds a list of dictionaries (starting with `[` and ending with `]`), holding artist names and artist IDs of artists currently featured on the platform.
# 2. When refreshing the data from the endpoint, new artists appear. It seems the website features multiple artists but only serves a few of them on the landing page. Probably, one would have to call this endpoint many times to arrive at a "complete" list of featured artists.
# 3. The timestamp can be stored using the `time.time()` function from the `time` page. This large number (e.g., 1606274053) can be translated into a date and time (for this example: 25 November 2020 03:14 GMT). 

# %%
import time
current_unix = int(time.time())
print(current_unix)

# %% [markdown]
# We can also convert this back into a readable format, using the `datetime` package.

# %%
from datetime import datetime
print(datetime.fromtimestamp(current_unix).strftime('%Y-%m-%d %H:%M:%S'))

# %% [markdown]
# ### 2.2 Inspect data before collection
#
# __Importance__
#
# Before we proceed to *downloading* data from an API, it is useful first to inspect the corresponding website (if it exists) to get an understanding of what data is available.
#
# Here, we zoom in on a new endpoint that provides us with metadata on artists: `artist/info`.
#

# %% [markdown]
# __Let's try it out__
#
# Check out the documentation of the [endpoint](https://api.music-to-scrape.org/docs#operation/artist_info_artist_info_get). What data do you expect to be able to obtain? What "data" is required to submit before viewing an artist's profile information?
#
# <img src="https://raw.githubusercontent.com/hannesdatta/course-odcm/master/content/docs/modules/week2/webdata-for-dummies/images/artist_info_endpoint.png" width=65% align="left"  style="border: 1px solid black"/>
#
#
#

# %% [markdown]
# #### Exercise 2.2
#
# Let us now try to retrieve data from this endpoint (using your browser). Let's use the artist with the `artistid` `AR5OHUU1187FB55B10`.
#
# 1. What URL do you have to enter in your browser to obtain the required information?
# 2. Reflect upon what you get here (vs. what you could get via the artist's profile page, available [here](https://music-to-scrape.org/artist?artist-id=AR5OHUU1187FB55B10). What are commonalities, and what are the differences?
#

# %%
# your answer goes here!

# %% [markdown]
# #### Solutions
# 1. Unlike the `artist/featured` endpoint, the `artist/info` endpoint requires you to "submit data" - an artist ID. After all, without telling music-to-scrape.org for which artist you require data, it's unlikely the site can give you any useful information. In this case, opening `https://api.music-to-scrape.org/artist/info?artistid=AR5OHUU1187FB55B10` in your browser will get you the desired data.
#
# <img src="https://raw.githubusercontent.com/hannesdatta/course-odcm/master/content/docs/modules/week2/webdata-for-dummies/images/artist_api_output.png" width=30% align="left"  style="border: 1px solid black"/>

# %% [markdown]
# 2. It's so much easier to obtain information via the API - one "call", and all the information gets readily compiled in a JSON object. Scraping is a much more "manual" process (e.g., selecting the right "place" on the website). 

# %% [markdown]
# ### 2.3 Retrieving data from the music-to-scrape API
#
# **Importance**  
#
# Many APIs are provided via paid subscriptions, but the one by `music-to-scrape` is free (like several others, check out Reddit.com for some real-world data!). 
#
# To request data from the music-to-scrape API, we should include `headers` in our HTTP request. Like in web scraping (remember the user agent?), headers contain *meta-data* required for the API call to work (e.g., type of browser, language, expected data format, etc.). 
#
# **Let's try it out**  
#
# Below, we re-request information from the `artist/featured` endpoint, including a header. We make our first actual request to the API in Python and parse the output in the upcoming exercise!
#

# %%
import requests
url = 'https://api.music-to-scrape.org/artists/featured'
header = {'user-agent': 'learning-to-scrape'}
response = requests.get(url, headers=header)
json_response = response.json()
json_response

# %% [markdown]
# #### Exercise 2.3
# 1. First, run the code over and over again. Do you observe changes?
# 2. Write a piece of code that prints only the artist IDs of the currently featured artists.
# 3. Write a while-loop that prints the artist IDs of the currently featured artists (as in 2), but have your code pause every 5 seconds before refreshing. Stop the loop after 3 iterations. For pausing, use the function `time.sleep(5)` (import the time package before using `import time`).
#
# ```
# import time
# i = 0
# while i<=3:
#     print('Starting to collect data, iteration', i+1)
#     #### YOUR API COLLECTION CODE HERE
#     print('   waiting 5 seconds...')
#     time.sleep(5)
#     i = i + 1
#
# ```
#

# %%
# your answer goes here!


# %% [markdown]
# #### Solutions
# 1. Yep! There are a lot of featured artists on the platform, and you only observe a subsample of them (and probably that subsample is not so random...).

# %%
# Question 2 

url = 'https://api.music-to-scrape.org/artists/featured'
response = requests.get(url, headers=header)
json_response = response.json()
    
for id in json_response['artists']:
    print(id['artist_id'])


# %%
# Question 3 
import time

i = 1
while i <= 3:
    url = 'https://api.music-to-scrape.org/artists/featured'
    response = requests.get(url, headers=header)
    json_response = response.json()
    
    for id in json_response['artists']:
        print(id['artist_id'])

    i += 1
    time.sleep(5)

# %% [markdown]
# ### 2.4 Retrieving meta data for multiple artists
#
# __Importance__
#
# Remember the endpoint `artist/info` used above? At the end of the scraping exercises, we iterated through a list of artists to retrieve data. Here, we do the same for the API endpoint. Iterating through an API endpoint for multiple "seeds" (or sampling units) is at the core of each data extraction task.
#
# __Try it out__
#
# Run the following cell, to see how looping through a set of subreddits works like. Do you see similarities to the scraping example introduced earlier? Exactly: the concept is entirely the same.
#

# %%
artists = ['ARICCN811C8A41750F', 'AR1GW0U1187B9B29FD', 'ARZ3U0K1187B999BF4']

for artist in artists:
    print(artist)

# %% [markdown]
# __Exercise 2.4__
#
# 1. Use your knowledge from the `artist/info` endpoint to retrieve artist metadata for each of the three artists. To avoid bombarding the server with too many requests, have the loop pause for one second at each iteration.
# 2. Append the moment of retrieval - a Unix timestamp - to each retrieved JSON object. Storing the timestamp of retrieval, along with the actual data, will help you later to match the data to other datasets across time.
# ```
# # retrieving current timestamp 
# import time
# time.time()
# ```
# 3. Collect a list of "featured" artists for about 30 seconds (using code written in 2.3). Combine your previously written code from 2.4 to collect artist metadata (using the endpoint `artist/info`) to collect meta data for all of these artists and store them in a new-line separated JSON file.

# %%
# your solutions here

# %% [markdown]
# __Solution__

# %%
# Q1
import requests
import time

artists = ['ARICCN811C8A41750F', 'AR1GW0U1187B9B29FD', 'ARZ3U0K1187B999BF4']

for artist in artists:
    print(artist)
    url = f'https://api.music-to-scrape.org/artist/info?artistid={artist}'
    response = requests.get(url, headers=header)
    json_response = response.json()
    print(json_response)
    time.sleep(1)

# %%
# Q2
import requests
import time

artists = ['ARICCN811C8A41750F', 'AR1GW0U1187B9B29FD', 'ARZ3U0K1187B999BF4']

for artist in artists:
    print(artist)
    url = f'https://api.music-to-scrape.org/artist/info?artistid={artist}'
    response = requests.get(url, headers=header)
    json_response = response.json()
    json_response['retrieval_time']=time.time() # <- this is where the information is "added" to the json response object
    print(json_response)
    time.sleep(1)
    


# %%
#Q3

# Load packages
import time
import requests

# Collect featuring data

featured_artists = [] # define "empty" list of featured artists

# define end time of loop as today's time plus 30 seconds (you can change it to 5 seconds for prototyping)
end_time = time.time() + 30

while time.time() <= end_time:
    print('collecting featuring data... please wait.')
    url = 'https://api.music-to-scrape.org/artists/featured'
    response = requests.get(url, headers=header)
    json_response = response.json()
    
    for id in json_response['artists']:
        featured_artists.append(id['artist_id'])
    time.sleep(1)
    

# %%
# look at the result!
featured_artists

# %%
# Let's collect metadata for each of these artists and store it in a JSON file

import json

f = open('artist_info.json', 'a', encoding = 'utf-8')

for artist in featured_artists:
    print(artist)
    url = f'https://api.music-to-scrape.org/artist/info?artistid={artist}'
    response = requests.get(url, headers=header)
    json_response = response.json()
    json_response['retrieval_unix']=time.time() # <- this is where the information is "added" to the json response object

    f.write(json.dumps(json_response))
    f.write('\n')

    time.sleep(1)

f.close()


# %% [markdown]
# Finally, open the resulting file and view it (e.g., in Visual Studio Code or RStudio). 
#
# __You've just completed your first data collection via an API! Congrats!!!__ 🥳

# %% [markdown]
# ### 2.5 Wrap up: APIs versus web scrapers
#
# Now that you understand what APIs are, you may rightfully wonder: why should I learn APIs when I could scrape the elements from the website instead (like on music-to-scrape.org)?
#
# - One of the major advantages of APIs is that you can directly access the data you need *without all the hassle of selecting the right HTML tags*. 
#
# - Another advantage is that you can often customize your API request (e.g., the first x featured artists), which may not always be possible in the web interface. 
#
# - Using APIs is a legitimate way to access website data (mostly, you will have to pay a license fee to use APIs!). So it's a more stable and legit way to retrieve web data than web scraping. __That's also why we recommend using an API whenever possible.__
#
# - In practice, though, APIs really can't give you all the data you possibly want, and web scraping allows you to access complementary data (e.g., viewable on a website or somewhere hidden in the source code).
#
# More commonalities and differences are also shown in Web Appendix of ["Fields of Gold"](https://doi.org/10.1177%2F00222429221100750), Table W1.
#
# Happy scraping!
#

# %% [markdown]
# ## After-class exercises

# %% [markdown]
# ### Exercise 1

# %% [markdown]
# So far, we have used Jupyter Notebook to execute our code. But, what if you wanted to *schedule and automatically run* your data extraction (e.g., even when you are asleep)?
#
# 1. Copy your code written in (3) of exercise 2.4 in web data for dummies to a `.py` file, and execute it 
# from the terminal (`python myscript.py`). 
#
# 2. Work through the scheduling section in [Guyt et al. (2024)](https://www.sciencedirect.com/science/article/pii/S0022435924000046#sec0013) (step 3, "Scheduling"). There is also a complementary tutorial on [Tilburg Science Hub](https://tilburgsciencehub.com/schedule/task).
#
# 3. Combine 1 & 2 to automatically schedule the extraction of the API data, every 10 minutes, for a duration of 2 hours
#
# 4. Open the downloaded `.json` data using the `pandas` package and provide some summary statistics:
#     
#     - number of unique artists captured
#     - number of duplicate artists captured
#     - start and end timestamp of the scraper
#     - average number of plays for featured artists
#
# ```
# # snippet to load the data into Python
# import pandas as pd
# pd.read_json('artist_info.json', lines = True)
# ```

# %% [markdown]
# __The solution is available on the course website.__
