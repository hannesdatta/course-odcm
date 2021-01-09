---
bookFlatSection: true
title: "Technical Extraction Plan and Prototyping"
description:
bookHidden: false
weight: 30
description: "Make a technical plan for data extraction and storage, and prototype your data collection."
---


# Technical Extraction Plan and Prototyping

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

{{< button relref="./legalfit.md" >}}Next{{< /button >}}



<!--

a.	Step 1. Determine sample units and time frame
i.	For which seeds to collect data? If seeds are not available, provide a navigation path to get to the seeds.
ii.	For which time frame to collect (e.g., time period for archival data, or frequency of data collection for “live” data; if live, monitoring becomes essential)
b.	Step 2. Map navigation path
i.	Where is the data located (e.g., page, endpoint), and how can the location be reached (e.g., URL vs. click/scroll, user-interaction)
ii.	If not all units are shown at once, how can you reach the remaining units (e.g., via looping)?
c.	Step 3. Decide whether to store raw data
i.	Future gains from raw data (new variables, replication)
ii.	Legal considerations (e.g., privacy)
iii.	Infrastructure considerations (e.g., storage capacity, storage format, auxiliary operations)
d.	Step 4. Select data for extraction
i.	Identify the location of the required content (e.g., CSS, XPATH, regular expressions)
ii.	Decide which specific data to extract (e.g., text on the page, attributes from source code, images or file names to download)
iii.	Convert data in appropriate form (e.g., removing ,000 separators, swapping . with ,. This can be achieved by cleaning or extracting substrings, searching and replacing, etc.)
iv.	Enrich with meta data (e.g., time stamp of scrape, timestamp of job initiation, IP address or derivatives like location details)
e.	Step 5. Determine storage of extracted data
i.	Data structure (structured/flat, versus unstructured JSON)
ii.	Files versus databases
iii.	Location (local versus remote)

-->
