---
weight: 3
title: "Team Project"
bookCollapseSection: true
description: " "
---

# Team Project

## Goal

Collecting data via web scraping and APIs requires practice. Together with your team members, you plan and execute an online data collection throughout the course, and submit your collected (and documented) data at the end of the course. [Check out our tips for interesting research contexts](projectideas.md).

The focus lies on *completing the complete [workflow for collection online data](../../tutorials/workflow)*. Therefore, keep each stage of your project *manageable* and *feasible*.

## Team composition

- between four to five students per team
- you need to subscribe to a team yourself (be present in the live streams for that; registration on Canvas!)
- we recommend teams to have at least one-two students with coding expertise in Python on their team

## Planning

- Week 1: Seek inspiration for data sources and interesting ideas to conduct academic research or invest into new business opportunities
<!--; the result of that session is a list of project ideas (i.e., with NEW ideas) that students can potentially work on; updates-->
- Week 2: Finalize team compositions, assess data availability and evaluate research fit & resource use
- Weeks 3-5: Build skills (APIs, web scraping), prototype data collection
- Weeks 6-8: Collect your data, and document it for reuse

<!--

- Week 2: Share data sources with the whole group; based upon common interest, form teams
          - Conduct your own data availability assessment using a template with your team.
- Week 3-4: Start working as a team
    - Build a prototype of the scraper
    - Run various test runs and check for stability
- Week 5-6:
  - Run the actual data collection (iterate if necesarry!)
  - Transform data into a format ready for analysis
  - Double check whether you have collected all data to answer your reserach question
- Week 7:
  - Document your data set starting from the template
  - Publish your raw and cleaned datasets on [DataverseNL](https://dataverse.nl)
-->



<!--
## Tasks


#### 1. Research Context

Pick a [research context](researchcontext.md) and find a website or API you would like to collect data from. Explain why performing this research can be of additional value to managers (e.g. the (social media) manager of the event or a digital advertising company). Provide clear managerial implications and back up your arguments with facts and figures.

#### 2. Data Collection

In this part of the assignment, you will use either an API or website to gather the data for your team project. Revisit the code snippets of the tutorials and see whether you can make them work for your chosen research context. Think about whether you collect a "snapshot" in time (statically) or whether your problem is better suited for a more dynamic approach (e.g., collecting data every other day). Keep in mind that that the underlying HTML or API structure may change over time, so always check whether your scraper works as expected. We recommend first making a test run prior to starting your actual data collection. Moreover, you may consider doing the data collection on two computers concurrently to prevent data loss.

#### 3. Data Transformation

In this part of the assignment you have to take a close look at the  data you collected. For APIs you may want to use a [JSON viewer](jsonviewer.stack.hu) to visualize the tree structure of a JSON object. Select which elements of you have to parse, but do not overcomplicate it (stick to the goal of your research!).

Even though we do not ask you to analyze the data in this course, the outcome of the data transformation step should be a data frame that is ready for analysis. Thus, depending on your research question, you may need to clean up the data (e.g., remove trailing and leading spaces), convert the data type (e.g., date time), derive features (e.g., length of the text), or aggregate numeric data (e.g., mean or sum).

Pursue to hand in a high-quality Notebook (e.g.: have a clear structure, annotate it using Markdown cells, try to formulate every command well and make sure it contributes to the actual outcome – your parsed data). Aim to make your script free of mistakes, so that it directly runs on our computers, too. Use efficient error handlings (i.e,. don’t wrap everything in a big try/except), and clearly name your input and output files.

#### 4. Data Documentation
Describe your raw data by filling out the Datasheets for datasets [template](http://tilburgsciencehub.com/workflow/documenting-data/). We have provided some extra tips and tricks for filling in the documentation over [here](doc.md).

#### 5. Data Distribution
Since the amount of data may well exceed file size limits of email, we ask you to distribute your data using [DataverseNL](https://dataverse.nl). This is an platform for storing, sharing, and publishing research data sets. You should login with your Tilburg University credentials, create an account (if you have never done so before), and add your data to your account. Please upload both the raw and cleaned data files there.


-->

## Deadline and submission
- 26 March 2021, 6pm
- Please prepare a [data package](grading_details), consisting of
  - the raw data files,
  - the code you used to collect the raw data (i.e., your scraper/API collection script)
  - the documentation,
  - and any source code files required to report statistics/preliminary insights in the documentation.

  ```
  readme.txt <-- your documentation,
                 either in the form of a plain txt file,
                 or a formatted PDF document

  docs\api_documentation.pdf <-- any supporting files
  docs\screenshot.pdf            for the documentation
                                 (e.g., API documentation,
                                 screenshots from the website,
                                 relevant blog articles)

  data\file1.csv <-- your raw data files
  data\file2.csv
  data\file3.csv

  src\collection\collect.py <-- final source code used
                                for collecting the data

  src\reporting\analysis.R <-- final source code used
                       to generate statistics/insights documented
                       in the readme.

  ```
- Submission via [Surf Filesender](https://filesender.surf.nl); send to h.datta@tilburguniversity.edu in one zip file (one email per team).
- Check out the [grading details before starting to work on your project](grading_details).

- If you are also taking ["Data Preparation and Workflow Management" (dPrep)](https://dprep.hannesdatta.com)...
  - You can use the data collected in this course for the team project in dPrep. The team project in dPrep runs in weeks 6-8, but you definitely need your raw data in week 5 at the latest (to prep well for week 6). In other words: generating some synergies between dPrep and oDCM comes at the cost of working on this project soon enough!
  - Please submit your entire workflow ("the same submissions") for each of the two courses, consisting of
    - your data collection, the raw data, and its documentation (focus of oDCM), and
    - the entire project pipeline (focus of dPrep, consisting of data exploration, data preparation, automation and deployment).
  - For oDCM, please *zip* your entire pipeline (so we're sure to get all the files for grading).
  - For dPrep, please only provide us with the link to your GitHub repository.


<!--
## Deliverables
- Please send one email per team to the course coordinator, containing
  - Link to published data at [DataverseNL](https://dataverse.nl)
  - Documentation, attached as a PDF file

<!--
o	Pursue to hand in a high-quality code (e.g., have a clear structure, annotate it using Markdown cells, try to formulate every command well, and make sure it contributes to the actual outcome – your parsed data). Aim to make your script free of mistakes, so that it directly runs on our computers, too. Use efficient error handlings (i.e., don’t wrap everything in a big try/except), and name your input and output files. We have made available coding tips on http://tilburgsciencehub.com/tips/coding/.
o	We invite you to share snippets of your parsing scripts via Gists on GitHub with other teams. You can post URLs to these Gists for others to view/use/reuse on Canvas.
-->
