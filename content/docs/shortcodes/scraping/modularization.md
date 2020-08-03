---
title: Modularization
weight: 2
---

# Phases in Online Data Extraction

Get
Monitor
Document

## Stage 0: Planning

- Determine depth of data collection
  - 1: Have list of seeds, scrape
  - 2: For each seed in 1: get links, go down one level deeper
  - 3: ... (typically: two stages deep)
  - Can go in parallel:
  - 1a: Have seeds, scrape here | 1b: Get API, too
  - It's like a tree! / write up like a DAG?
  - Dependencies between stages
- Familiarize with site
- Retrieval limits

## Stage 1: Getting the raw data

- Initiation / triggers
- Use server / location dependencies? geo requirements?
- Timing
- Monitoring: Retrieval errors (e.g., blocking)

## Stage 2: Storing the raw data

- What?
  - HTML --> S3, disk
  - Automatic zipping/packaging
  - HTML
  - Is it dynamic? --> database-approach
- Monitoring: Server capacity, billing, diskspace
- Storage may be transitory (e.g., database to support extraction); or permanent (CSV) -> if permanent, choose files

## Stage 3: Extract/structure the data

- How? to csv.

## Stage 4: Documenting and releasing

- What decisions are important to say? e.g., seeding
