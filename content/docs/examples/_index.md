---
bookFlatSection: true
title: "Examples"
bookHidden: false
weight: 50
---

# Examples and extra material

This site collects links to web scrapers and API retrieval projects.

## Web scrapers
- Great websites to start your first scraping project
  - [Boxofficemojo](https://boxofficemojo.com) is well structured and has stats on movie revenue, release date, and actors
  - [Sports Reference](https://www.sports-reference.com) has stats on players in US sports (baseball, basketball, football, hockey)
  - [Wikipedia](https://wikipedia.com) is also locally available, but keep your maximum retrieval frequency at 1 page per second.
- [Netflix Home Screen Capture](https://github.com/hannesdatta/data-netflix)
- [Playlist Promotions and New Releases at Spotify](https://github.com/hannesdatta/data-spotify-playlists-releases)

## APIs
- [Documenting data collected via APIs (Chartmetric)](https://github.com/hannesdatta/data-spotify-playlist-ecosystem)

## Tools
- [Code to monitor the health of online data collections via Push Messages](https://github.com/hannesdatta/healthmonitor)

## Podcasts and Tutorials
- [Listen to a podcast with Kimberly Fessel](https://realpython.com/podcasts/rpp/12/) who shares some best practices on scraping the web. She also has shared a [fantastic tutorial on YouTube](https://www.youtube.com/watch?v=RUQWPJ1T6Zc&t=190s)

Tutorial


Write as a csv or store as pickle files
Start out in Jupyter Notebooks to make sure you have the right syntax to get the data → convert to a Python script → set-up scheduling
Stripping out characters ("$", ",", non-printing characters)
Importance of regular expressions (start out with replace() initially
Convert dates and times to pandas timeseries
Limitations of BeautifulSoup and request
Does not work for sites that are dynamically loading content (hitting a database and pulling in information).
Mostly JavaScript websites (YouTube, Open Table)
Selenium is the solution; launches a Google Chrome driver; sometimes it as simple as launching the site with selenium and then processing the data with request and Beautifulsoup.
Other advantages: clicking on things and filling out fields
Scrapy - cloud deployment and built a "spider" (scraper that keeps on going and look for new links)
Importance of visualising your results dynamically/interactively (D3, Plotly, Tableau)
Data widgets getting more mainstream (e.g., NYT) - people getting more data literate
