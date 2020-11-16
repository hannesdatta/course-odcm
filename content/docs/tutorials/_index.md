---
bookFlatSection: true
title: "Tutorials"
bookHidden: false
weight: 2
bookCollapseSection: true

---

# Tutorials
__draft__

1. Web data retrieval for dummies
  - Do
    - Scraping: Run selenium/chromium on socialblade.com and iterate through predefined list of seeds which you have loaded from a text file or from an array inside Jupyter Notebook
    - API: Collect from publicly available API endpoints and parse
  - Practice
    - Swapping CSS selectors; changing inputs for seeds
    - API: Parsing multiple endpoints

2. Web scraping 101
  - Do
    - Applications: spotifcharts.com (headless; download CSV), socialblade.com (selenium; simulated browser)
    - Building and iterating through seeds (predefined, on the basis of an external list, on the basis of a web-scraped list)
    - Avoiding simple errors (`time.sleep`)
  - Practice
    - Extend to other site that downloads stuff (which site?)
    - Extend to long list of seeds (self-obtain)

    - Learn how to make headless HTTP requests using Python's `requests` library
    - Understand the implications of using various user agents in request headers
    - Save content of HTTP request to a file, and explore content (and compare content to one that you see in a browser)
    - Learn about the structure of websites using Chrome's developer tools, and identify elements using "anchors" (e.g., CSS selectors, XPATHs)
    - Extract values (e.g., text, attributes) from web site elements as identified by their CSS selectors
    - Write extracted values to flat txt/csv files
    - Load IDs of seeds from external txt/csv files
    - Modularize code, by using functions and loops
    - Handle retrieval errors using try and except statements
    - Make use of timers to emulate user behavior (e.g., `time.sleep(1)`)

    ## Prerequisites
    - Download this notebook and open it in Jupyter Notebook

    ## Details
    -


3. APIs 101
  - Do
    - Applications: Twitter API (with authentication)
    - Ideally not with a pre-made package: requests.
    - Ideally data from different endpoints
    - JSON file structures
  - Practice
    - Extend to other end points?
    - Extensive parsing exercises

4. Web Scraping Advanced
  - Site interaction with Netflix.com (?) + scrolling

5. APIs Advanced
  - ??

6. Data packaging
  - Work out data publication workflow

<!--

## Principles/points of discussion

- Ideally, notebooks themselves present *usuable* marketing cases already
- Tutorials
  - ...
- cases and examples [Case ideas for marketers; extend, put student examples here?]
  - scrape prices
  - collect buienradar data
  - collect social media
  - collect reviews data
  - collect twitter data
  - deploy dashboard
  - automate emails
  - collect from Twitter
  - ...other examples?
  - "big picture" cases
- The tutorials should pick up some of the concepts from the workflow
- Challenge is to build both concepts and skills, and to learn about the basic concepts of scraping
-->

<!--
# Tutorials

{{<section>}}
-->
