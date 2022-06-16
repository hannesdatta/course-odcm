---
bookFlatSection: true
title: "Project ideas"
bookHidden: false
weight: 3
---

# 1. Projects from previous editions
To give you an idea of what a good project could look like, we published some of the projects from the previous course editions. Feel free to check these out and get inspired by them for your own team project!

### Web scraping
- Scraping reviews about KLM (airlines) - [Click here!](https://zenodo.org/record/5902839/files/Airline%20reviews.zip?download=1)
- Scraping data about popular beers from the Untappd website - [Click here!](https://zenodo.org/record/5902839/files/Beer%20craft.zip?download=1)
- Scraping user data from the Goodreads website - [Click here!](https://zenodo.org/record/5902839/files/Goodreads.zip?download=1)
- Scraping data about second-hand clothing from Zalando  - [Click here!](https://zenodo.org/record/6641811/files/zalando.zip?download=1)
### APIs
- Using the Reddit and WallStreetBets APIs to collect data that can be used to measure its impact on stock prices - [Click here!](https://zenodo.org/record/5902839/files/Reddit%20api.zip?download=1)
- Collecting software available for sale using Steam's API - [Click here!](https://zenodo.org/record/6641811/files/steam_api.zip?download=1)

In addition to these projects, other good examples from previous editions can be found on Zenodo by [clicking here](https://zenodo.org/record/5902839#.YfAO02DTX0o) and [here](https://doi.org/10.5281/zenodo.6641811) (Fall 2021 and Spring 2022 edition, respectively).

# 2. Project ideas

*Note: The final team projects (and team allocations) are available on the course's (non-public) Canvas page.*

Here's a list with a couple of project ideas. __Don't feel restricted by these options, though!__ There are plenty of other great ideas (e.g., see the examples in section 3 below), and we encourage you to think of applications in which you use two or more APIs, or in which you combine web scraping with relevant APIs.

When using a proprietary data sources requiring login (e.g., Netflix) or API credentials (e.g., Twitter API), make sure you can *actually* get access to the accounts (and potentially share those with team members).



<!--Research Context

Skilling up in web scraping and APIs requires practice, and conducting a group project is a great way to learn more about any facet of data- or computer science. Choose one of the following questions to explore further or pitch your own one during one of the live meetings in the course!
-->

### Online music streaming and podcasts
- [spotifycharts](https://spotifycharts.com/regional)
- [Spotify Web API](https://developer.spotify.com/documentation/web-api/)
- [Last.fm](https://last.fm)
- [Listennotes](https://listennotes.com) and [Listennotes Realtime](https://listennotes.com/realtime)

<!--
- Potential research questions
  - Compare the rankings across countries throughout time (2017-2021)
      - How long do tracks typically stay in the top 200?
      - Are the Spotify top 200 charts similar to [YouTube Music charts](https://charts.youtube.com)?
      - What is the relative market share of music streaming in comparison to global figures?
      - Can tracks that fell off the track, bounce back and climb up the rankings again?
      - Do the total number of streams significantly fluctuate throughout time?
    - Can you find clusters of countries that share the same music taste?
-->

### Concerts and events
- [Songkick](https://www.songkick.com/developer)

### E-commerce
- [bol.com](bol.com)
- [Coolblue](coolblue.nl)
<!--
- Potential business questions
   - Are our tech products priced lower than our competitors?
   - Are the same products on sale at the same time?
   - Are customer reviews comparable across platforms?
   - How are products ordered by default?
-->

### Social media
- [Instagram](https://www.instagram.com)
- [Twitter](https://www.twitter.com) (you can also use their streaming [API](https://developer.twitter.com/en/docs)!)
- [Reddit](https://www.reddit.com/dev/api/)
- [TikTok](https://www.tiktok.com)

### Movies
- [Netflix](https://www.netflix.com/browse)
- [IMDb](https://www.imdb.com)
- [The Numbers](https://www.the-numbers.com/) (check here for daily top 10 lists for home video and Netflix, going back about 1.5 years)
<!--
- Potential research questions
  - Which movie genres are most popular, and are most likely to be trending?
  - Are Netflix originals promoted more often on the homescreen than other movies?
  - Are the highest rated movies also the ones most popular on Netflix?
-->

### Online videos, user-generated content
- [YouTube API](https://developers.google.com/youtube/v3)
- [Twitch API](https://dev.twitch.tv/docs/api)

<!--
- Potential research questions
  - What are the most popular types of YouTube channels in terms of views?
  - Did watchtime and views go up for these channels since the COVID-19 outbreak?
  - Do the channels with the most subscribers also earn the most? (e.g., see [Socialblade](https://socialblade.com/youtube/))
  - What factors play a role in determining the "Socialblade" channel grade?
  - How can you identify upcoming Youtubers that show great potential for an advertising partnership?
  - How does Twitch help creators earn money and build their fandom?
-->


# 3. More examples and extra material

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

### Podcasts and Tutorials
- [Listen to a podcast with Kimberly Fessel](https://realpython.com/podcasts/rpp/12/) who shares some best practices on scraping the web. She also has shared a [fantastic tutorial on YouTube](https://www.youtube.com/watch?v=RUQWPJ1T6Zc&t=190s)

# 4. Tips & Tricks

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
