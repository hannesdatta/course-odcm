---
bookFlatSection: true
title: "Tips and examples"
bookHidden: false
weight: 30
draft: false
description: Apply useful (technical) tips.
---

# Tips and examples

## Tips

### Coding
- Using separate lists vs. lists of dictionaries
  - Don’t break the structure of what belongs to what!
- Looping: while loops are also an option!
- Try & except: just use it for one part each, not for many things at the same time
- Break up code into smaller modules (e.g., first seeds, then getting the data)
- Cleanup code (e.g., comments, etc.)
- Modularizing code (so that it works on multiple categories, pages, etc.)
- Make “class names” flexible so that you don’t have to repeat yourself over and over again
- For anonymization: use a [hash function](https://nitratine.net/blog/post/how-to-hash-passwords-in-python/) (salted!)
- Read paper and align code / update code (e.g., meta data enrichment)

### Data collection
- Store raw data as JSON - parse in a second step
- Separate “seeding” from “collecting information” stage
- Write the data as soon as you can to a file (e.g., JSON) - not only at the end of a long (1.5 days!) scraping session (minimize data loss)
- For extended data collections - consider saving the raw html files first - then only parse!
- How to find max. page numbers? You can do some calculations with information from the site (e.g., for AH.nl —> 1077/36 items on the page = 29.x pages)
- Storing all of the JSON, then only preprocess
- Use selenium for dynamic websites

## Examples and extra material

### Web scrapers
- Great websites to start your first scraping project
  - [Boxofficemojo](https://boxofficemojo.com) is well structured and has stats on movie revenue, release date, and actors
  - [Sports Reference](https://www.sports-reference.com) has stats on players in US sports (baseball, basketball, football, hockey)
  - [Wikipedia](https://wikipedia.com) is also locally available, but keep your maximum retrieval frequency at 1 page per second.
- More advanced use cases
  - Ever tried extracting data from data widgets (e.g., like available at The New York Times)?
  - [Netflix Home Screen Capture](https://github.com/hannesdatta/data-netflix)
  - [Playlist Promotions and New Releases at Spotify](https://github.com/hannesdatta/data-spotify-playlists-releases)

### APIs
- [Documenting data collected via APIs (Chartmetric)](https://github.com/hannesdatta/data-spotify-playlist-ecosystem)

### Tools and frameworks
- [Code to monitor the health of online data collections via Push Messages](https://github.com/hannesdatta/healthmonitor)
- [Scrapy](https://scrapy.com) and [Morph.io](https://morph.io) are comprehensive, code-based frameworks that collect the data for you in the cloud
- Try visualizing your results dynamically/interactively, for example with D3, Plotly, ShinyApps, or Tableau
- [Snscrape]((https://github.com/JustAnotherArchivist/snscrape)) - an amazing Python package to scrape data from social networks like Twitter, Facebook, Instagram, Telegram, VKontakte and Weibo

### Podcasts and tutorials
- [Listen to a podcast with Kimberly Fessel](https://realpython.com/podcasts/rpp/12/) who shares some best practices on scraping the web. She also has shared a [fantastic tutorial on YouTube](https://www.youtube.com/watch?v=RUQWPJ1T6Zc&t=190s)
