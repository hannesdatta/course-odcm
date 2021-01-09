---
bookFlatSection: true
title: "Data Extraction Plan"
description:
bookHidden: false
weight: 30
description: "Formulate specific steps on how to go about capturing and storing the data that you need."
---


# Data Extraction Plan

## Select entities

Determine which entities you would like to get. If these entities are sampled from the site directly, how do you get to that initial list? Be as specific as possible: go here, obtain the first 1000 products there, then start scraping these pages, etc.

## Determine frequency of data collection

Determine the frequency of data collection. For historical data, that's typically just once, unless you want to refresh your data towards the end of your project. For information that's only available in real-time, things get more complicated, and you need to balance the number of entities in your data, the extraction frequency, and the limits imposed by the website, such as only five requests per second.

## Map out navigation path

Map out the exact navigation path on the site. Which page to open, for which entities? This becomes a loop in your data extraction code. What interaction is necessary: is it enough to visit a website with a link, or do you need to simulate clicks and scrolling behavior? Similarly, if not all units are shown at once, how can you reach the remaining units (e.g., via pagination/looping)?

## Decide whether to store raw data during the data collection

Decide whether to store raw data during the collection procedure. The upside of storing raw data is you could extract data you haven't planned for. The downside is you may breach privacy laws or exceed your disk space.

## Select data for extraction

Select data for extraction. Can you make use of HTML tags, or do you need to make use of CSS or XPATH selectors?

{{< hint info>}}

Remember to prototype data capture in Python or Juptyer Notebook!
{{< /hint >}}

## Determine format for storage after collection

Determine how to store the data. What's the file format: do you make use of flattened CSV files or unstructured JSON files? Do you store it in a database or files? And, finally, do you keep it on a local computer or somewhere in the cloud?
