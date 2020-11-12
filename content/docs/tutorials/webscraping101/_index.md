---
weight: 10
title: Web scraping 101
description: Learn how to make a simple (headless) HTTP connection to a site and parse content to a CSV file
bookCollapseSection: true
draft: true
---

# Web scraping 101

## Learning goals

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



#####


  ## Exercises and activities
  - Part 1
    - Tutorial: webscraping 101
    - Exercises: navigation path, CSS selectors, choice for headless versus browser emulation
  - Part 2
    - Tutorial: API 101
    - Exercises: endpoint navigation, authentication, parsing, modularization
