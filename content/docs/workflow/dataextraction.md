---
bookFlatSection: true
title: "Data Extraction Plan"
description:
bookHidden: false
weight: 3
description: " "
---


1. First, determine which entities you would like to get. If these entities are sampled from the site directly, how do you get to that initial list? Be as specific as possible: go here, obtain the first 1000 products there, then start scraping these pages, etc.
2. Second, determine the frequency of data collection. For historical data, that's typically just once, unless you want to refresh your data towards the end of your project. For information that's only available in real-time, things get more complicated, and you need to balance the number of entities in your data, the extraction frequency, and the limits imposed by the website, such as only five requests per second.
3. Third, map out the exact navigation path on the site. Which page to open, for which entities? This becomes a loop in your data extraction code. What interaction is necessary: is it enough to visit a website with a link, or do you need to simulate clicks and scrolling behavior? Similarly, if not all units are shown at once, how can you reach the remaining units (e.g., via pagination/looping)?
4. Fourth, decide whether to store raw data during the collection procedure. The upside of storing raw data is you could extract data you haven't planned for. The downside is you may breach privacy laws or exceed your disk space.
5. Fifth, select data for extraction and prototype data capture in Python or Juptyer Notebook. Can you make use of HTML tags, or do you need to make use of CSS or XPATH selectors?
6. Sixth, and finally, determine how to store the data. What's the file format: do you make use of flattened CSV files or unstructured JSON files? Do you store it in a database or files? And, finally, do you keep it on a local computer or somewhere in the cloud?
