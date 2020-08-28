---
title: Introduction2
type: docs
---

# Data preparation and Workflow Management (dPrep)

**Manage data- and computation-intensive research projects efficiently**

_Tilburg University, Block 3, 2020/2021 (January - March 2021)_

_Instructor: [dr. Hannes Datta](https://hannesdatta.com)_

<!--
## Glossary search

Already know what you're looking for? Search the __Glossary__ here.

-->

## Learning objectives

- Learn how to read in, clean, and engineer data sets for empirical marketing research projects
  - Advanced file I/O: Data formats (e.g., CSV, JSON), systems (e.g., file-based, structured and unstructured database), and local vs. remote architectures
  - Common data manipulation techniques in R using `data.table` and `tidyverse`
    - Aggregation, transformation
    - Writing functions in R
    - Merging data sets
    - Looping (e.g., over variables, over data splits)
- Audit data / validity checks

- Deploy data preparation techniques locally or remotely
  - Disitrbuted computing
  - Internally (R, parallel)
  - Externally (EC2, launching instances, manage HPC code)
- Workflow management
  - Data pipelines
  - Automation using makefiles
  - Command-line scripting
  - Project management on GitHub (versioning, issue management, collaboration)
- Logging/monitoring
  - Logging into audit txt files
  - Generation of Latex and Word output
  - Report preparation in latex/Overleaf
  - Dynamic output:
    - Shiny
    - NodeJS/dynamic graphs

- Familiarize yourself with data workflows, encompassing data pipelines, automation, command line scripting
- Familiarize yourself with data preparation techniques in `R` using `tidyverse` and `data.table`
- Read in various data formats
- Learn about data transformation techniques
- Familiarize yourself with basis programming principles
- Write functions in R
- Deploy your code internally (e.g., single-core, multiple-core), or externally (EC2, cluster computation)
- Automate your workflows using `make`
- Project management
- Familiarize yourself with GitHub and code versioning

- Transform semi-structured JSON data to structured data sets for statistical analysis ("parsing") [???]


- Store and manage data using file-based systems and databases

- Gain practical experience using R, MySQL, MongoDB and Amazon Web Services (AWS) with regard to data engineering
- Enable you to draft, execute, monitor and audit automate data preparations, and learn from templates you can use to kickstart your own academic or commercial projects
- Document and archive your data, and make them available for public (re)use
- Track and share your own progress on the course's learning goals
- Critically evaluate your contribution and the contribution of team members to group projects ("peer assessment")

## Grading

- Group project (4-5 team members) with peer assessment (40%)
<!-- submitted as a GitHub repository (during the course); building a dataset-->
- Computer exam (60%) [or, take-home exam?]


- Share progress and learnings (e.g., open science contributions in the form of course-relevant contributions in the form of pull requests to GitHub, maintaining a public FAQ/blog, sharing one's progress with the group) (20%) [[[???]]]

<!--; can consist out of in-class contributions (e.g., presentation, pitch), code (e.g., data collection code), or reports -->

Students pass this course if the final course grade (i.e., the weighted average of the components above) is at least 5.5/10.


<!-- take home exercise: just submit; you get "DONE" on it as per the deadline -- make sure students stay up-to-date w/ the content

-->

<!--
Elke toetsvorm (bijv. paper, exam, midterm) dient apart in Osiris te worden ingevoerd, met vermelding van minimum cijfer en wegingsfactor.

-->


## Format

- Taught fully online on Zoom, with the option for lab sessions on campus
- Hybrid format: Interactive notebooks or pre-recorded web clips for preparation and self-paced lab sessions; live streams for feedback and joint coding sessions (recordings will be made available)
- Modern content: copy-paste code snippets and demos from the course page, access code on GitHub, start projects with Jupyter Notebook templates, sharing screens
- Interactive, immersive and student-centred: live coding, debates, open-source content contributions, working with real data sets

<!--, simulations, hackathon-->
<!-- work on VMs on AWS, code in SQL and R, compete on Kaggle, or work on own computer--; Coding Dojo student-=led analysis; while sharing screens-->

## Student profile / prerequisites

- The course is intended for both novices and those students with a technical background
  - We recommend novices to familiarize themselves with R before the start of the course. Material (e.g., courses at datacamp.com) will be shared with students well in advance.
  - Alternatively, novices may benefit from following other courses at Tilburg University in which R is used, for example, *XXX*.
- The course is instructed to MSc students in the Marketing Analytics (TiSEM) program.
- A high level of commitment, both in terms of time and effort, is expected

## Enrollment and Obtaining Course Credits

- The course (3 ECTS) will be taught in the Marketing Analytics Program at Tilburg University (please check Osiris for the specifics).
- Interested Research Master or PhD students who interested in best practices for working with and building complex data sets can audit this course upon the approval of [the instructor](mailto:h.datta@tilburguniversity.edu).

## License

This course is licensed under a [Creative Commons Attribution-NonCommercial 4.0 International License](http://creativecommons.org/licenses/by-nc/4.0/). In other words, you're invited to contribute to it, or even copy and modify it to suit your needs.

Spread the word about this open education initiative!

![Creative Commons Licence](https://i.creativecommons.org/l/by-nc/4.0/88x31.png)
