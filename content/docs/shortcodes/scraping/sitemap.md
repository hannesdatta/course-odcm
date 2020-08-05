---
title: Sitemap
weight: 1
---

- Sampling
  - Random sampling
    - Sample from population via search
    - Sample from population via most recent pages
  - Finding external seeds
  - Explore networks
  - Stratified sampling


## Stage 0: Planning

- Determine depth of data collection
  - 1: Have list of seeds, scrape
  - 2: For each seed in 1: get links, go down one level deeper
  - 3: ... (typically: two stages deep)
  - Can go in parallel:
  - 1a: Have seeds, scrape here | 1b: Get API, too
  - It's like a tree! / write up like a DAG?
  - Dependencies between stages
- Familiarize with site(s)
- Determine fair-use retrieval limits
- Plan "endpoints"
  - What is the URL scheme?
  - How to insert the seeds?

## 1: Getting the raw data

- Initiation / triggers + technical implementation
- Use server / location dependencies? geo requirements? / run locally?
- Refetch upon error?
- Store __raw__ data
- Enriching raw data with time stamps of data retrieval
- Documenting errors + monitoring: Retrieval errors (e.g., blocking)


## 2: Storing the raw data

- What?
  - HTML --> S3, disk
  - Automatic zipping/packaging
  - HTML
  - Is it dynamic? --> database-approach
- Monitoring: Server capacity, billing, diskspace
- Storage may be transitory (e.g., database to support extraction); or permanent (CSV) -> if permanent, choose files

## Stage 3: Extract/structure the data

- How? to csv.


## Validate

e.g., plots of errors

## Stage 4: Documenting and releasing

- What decisions are important to say? e.g., seeding, precleaning, when where they executed
- Reporting in paper
- scope: mobile apps / simulating paths. --> include? possible?
- web scraping is the process of designing and deploying code that automatically extracts and parses information from websites/APIs.

WORKING WITH web scarped data
COLLECTING web scraped data

Data sources:
- blogs / [....]
-

- structured workflow

- starting up the JOB / JOB scheduling
- kililng other processes of CHrome
- killing chromedriver


NOtes Johannes:
- does web scraping encompass APIs?
  - APIs share concepts: endpoints; but extraction is more automatic
  - Figure 3: "innovation"/"gut feeling of good idea"
  - SERVICES provide websites or APIs; it's nt that websites provide apis. APIs / like websites, offer recent data. so that's general.
- minor comments:
  - include "booleans" in overview

- provide a structured workflow
  - explore and prototype
  - design
  - companion

- i don't see overlap w/ text analysis
- do we have a figure for the type of data used from sites?
- sample size implications of scraping
- internal sites versus publicly accessible sites
- clearly separate out processing from getting/parsing
- unit of analysis: user - time; page.
- panel data


- understand infrastructure of site
- store meta data when the site was extracted, monitor the firms' blogs, and put it in the paper. @Hannes paper.
- keep screenshots
- regular CSV capture
- validity of data (e.g., only recent data).

- increasing limits (&limit=100), or elements on pages.
- display options (not recommended; or sorted by date)
- check flags - antyhing excluded?

- capture recommendations

- web scrapers can be used to monitor experiments, too!
