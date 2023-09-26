---
weight: 5
bookFlatSection: true
title: "Project Grading"
bookHidden: false
description: "Find out which elements must be included in the team project and how these elements are graded."
---


# Project Grading

## Overview
The team project is submitted as a so-called “data package”, consisting of the following three elements:

1. Documentation (60% of the final grade)
2. Source code for the data collection (30% of the final grade)
3. Overall quality of the data package (10% of the final grade)

In preparing your submission, please closely adhere to the following directory structure.

```
readme.pdf <-- your documentation, based on the template and rendered as a PDF document

docs\api_documentation.pdf <-- any supporting files for the documentation (e.g., API documentation,
docs\screenshot.pdf            screenshots from the website, relevant blog articles)

data\file1.json <-- your raw data files, as .json or .csv, depending on the optimal storage format
data\file2.csv
data\file3.csv

src\collection\collect.py <-- final source code used for collecting the data (can be multiple files)

src\reporting\descriptives.R <-- final source code used to generate statistics/insights documented in the readme.
                                 Note: you are not required to provide a full-fledged analysis of the data.
                                 
```


{{< hint info>}}

**Be ready for publication**

Please submit the data package in such way that it can be made publicly available on the internet.

For example, you need to fully anonymize information that could be considered sensitive or personal, such as names or other personal information. Also, you must not store any of your personal passwords in code. Do you want to keep your names on a public data package or would you rather prefer to blank out your names (in that case, just take them out - I'll be able to match your grade using your team number). Finally, do a check on whether the statements made in your documentation are realistic.

{{< /hint>}}
## Calculation of team grades
Weights for each component of the grading rubric below are indicated in brackets (e.g., 5%). In calculating your final grade, percentages are converted to grade points on a ten-point scale (e.g., 5% make up 0.5 grade points on a 10-point scale), weighted by the following percentages:

* *High proficiency* and/or exceeds expectations (grade points x 100%)
* *Adequate proficiency* (grade points x 80%)
* *Some proficiency* (grade points x 60%)
* *Insufficient proficiency* (grade points x 30%)
* *No proficiency* (grade points x 0%)


{{< hint info>}}
***Example***

*A student team has shown adequate proficiency in motivating the context in which the data was collected. The motivation for the data context counts towards 5% of the team project’s final grade. In grade points, this equals .5 points on a 10-point scale. The points are weighted with 80% for adequate proficiency. The grade for this part of the data package equals .5 x 80% = .40.*

{{< /hint>}}


## Details

### **1. Documentation**

Please follow [Datasheets for Datasets](https://arxiv.org/pdf/1803.09010.pdf) (2018) in writing your documentation. Please get started by using the [template](/docs/project/Datasheets_for_DataSets.zip), and fill in __all (sub-)questions in sections 1-6__. If you decide to make the data set publicly available (e.g., on Zenodo or OSF), you also need to fill out sections 7-8.

In the grading details below, numbers (#1, #1.4, etc.) refer to sections in the final documentation.

#### 1.1 Motivation (section 1 of your documentation, 10%)

From your answers to _all questions in section 1 of the documentation template_, the following points need to be addressed:

- *Motivation for research context (5%)*  
Clear explanation of the value in collecting the data (“task in mind”), either in the context of a specific research question or business problem. The data collection potentially generates insights into new phenomena, increases the managerial relevance of empirical work, helps to develop new models, or is an efficient way for collecting valuable information. There is clearly value to the larger research community in using the data.

- *Motivation for selected data source (5%)*  
A wide range of relevant websites and APIs pertaining to the data context are assessed. The use of different extractions methods and alternatives to web scraping are considered and the data context is sufficiently scoped to ensure validity and to identify other relevant information that may be valuable. It is clear why the data was ultimately collected from the focal website/API, and not from others (i.e., the website/API emerges as the one that fits best in terms of research fit and resource use; #1.4).

#### 1.2 Composition (section 2 of your documentation, 25%)  

From your answers to _all questions in section 2 of the documentation template_, the following points need to be addressed:

- *Extraction design (10%)*  
  - The risk of algorithmic interference is taken into account and dealt with accordingly. Furthermore, possible changes to the contents of the website or data aggregator that may influence the results are considered and metadata is collected, if applicable.
  - The seed selection is valid and clearly explained. Potential linkages to external data sets are made explicit (e.g., by means of links to external websites or sources that explain more about the used identifiers).
  - The frequency at which the data is the collected and the limitations to this are made explicit. If it is opted to collect data more than once, teams used automatic scheduling to ensure valid and consistent results.

- *How is research validity is balanced with technical feasibility and legal/ethical risks (5%)*  
The design decision lead to a tradeoff between validity, technical feasibility and exposure legal/ethical risks. The consequences to these are carefully described when making decisions on one of the previous steps (i.e., which information to extract, which seeds to select and at what frequency).

#### 1.3 Data inspection (section 3 of your documentation, 10%)

- The collected data is accompanied by meaningful summary statistics (e.g., the number of units per entity, means/SD for continuous variables, and frequency distributions per variable, for each entity). 
- Missingness has been investigated (e.g., for individual entities, but also for the collected variables). 
- Any redundancies, errors, or sources of noise have been clearly described. Identified subpopulations are labeled, so that users of the data can more easily get started using the data.

#### 1.4 Collection process/data extraction (section 4 of your documentation, 10%)

From your answers to _all questions in section 4 of the documentation template_, the following points need to be addressed:

- The technical extraction plan has been described in a way that the data collection could be replicated. This encompasses providing a solid argumentation on why a particular data extraction technology used (e.g., selenium versus Beautifulsoup for websites, a package versus self-coded requests for APIs). If teams came across technical issues when scaling the data collection, the debugging stage is clearly explained.
- Users of the data learn about the technical hurdles that needed to be overcome, and which monitoring was in place to guarantee (and validate) data quality.
- Details are given on how (deployment infrastructure) and when the data collection was executed (e.g., by meaningful summaries of the timestamps in log files), and where the final data set was stored during the collection.

{{< hint info >}}
__Best practices for documentation__

Please include screenshots and/or an additional recording in your documentation. Not only will this improve interpretability, it also contributes to the accuracy and reproducability of the project!

{{< /hint >}}

#### 1.5 Preprocessing (section 5 of your documentation, 10%)

From your answers to _all questions in section 5 of the documentation template_, the following points need to be addressed:

- *Preprocessing (5%)*  
Any pre-processing on the fly has been motivated and explained, using a few specific examples. Any further pre-processing after the collection has been described (e.g., such as to anonymize users for privacy concerns, to identify and clean out implausible observations, or to improve data structure for long-term storage, such as rearranging the data structure, relabeling columns into more meaningful and clear variable names). Potential threats that may result from this pre-processing are brought up and elaborated on.

- *Accessibility and structure of final data files (5%)*  
The files have a correct data structure, and variables are of the correct type (e.g., numbers as integers or floats, not as strings; time stamps properly formatted, or Unixtime used). Application of data enrichment and feature engineering strategies (e.g., to derive new variables from the data, where necessary). Data has been normalized (i.e., preferably multiple tables that can be joined together, rather than a wide table that contains many duplicates on some of the variables). If imputation is used, it is indicated which values have been imputed (e.g., interpolated; for example: followers (without missing), and followers_inputed as a TRUE/FALSE variable, indicating which ones were imputed). Finally, the data set is provided in CSV files, including column names, proper use of delimiters (e.g., a “,” may be inappropriate for textual data involving commas). No row names/index column.

#### 1.6 Uses (section 6 of your documentation, 5%)  

From your answers to _all questions in section 6 of the documentation template_, the following points need to be addressed:

* *Users of the data learn about tasks the data set could be used for (5%)*  
From the description, it is clear how the composition of the data set or the way it was preprocessed might affect future use. A clear indication is given for what the data should not be used for, e.g., relating to any of the legal or ethical concerns identified before.


### **2. Source Code for the Data Collection**

- *Quality of the submitted source code (15%)*  
  - Present and clearly readable (e.g., variable names that are meaningful)
  - Inline markdown formatting (e.g., headers, dividers, paragraphs, etc.)
  - Well-structured and modular source code (e.g., use of functions)
  - Adhere to DRY principles (e.g., for-loops and functions)
  - Concise code (e.g., list and dictionary comprehensions)
  - With comments and docstrings
  - Code blocks run in a linear fashion (i.e., top to bottom execution runs without issues); removal of unnecessary source code and packages that are not needed
  - File paths are specified relative to the current script, no absolute paths used
  -  Error-handling incorporated (e.g., does the scraper still run if the API or website changes?)

- *Quality of the technical implementation (15%)*
  - The quality of the technical implementation is judged for web scraping and APIs, as per some of the following dimensions.

  {{< hint >}}

  **Web scraping**
  - A single vs. multiple entities / web pages
  - Degree of complexity required to obtain data (e.g., static websites with a fixed class name vs social media which requires more dynamic approaches such as clicking on buttons and navigating across pages; self-coded extraction code versus use of a package which extracts data automatically)
  - Stability of the solution (i.e., navigation path should not be subjective to day-to-day page changes). Can the code be run after submission? Can the code be run on Windows, Mac and Linux?
  - Obeying retrieval limits (usage of timers to avoid overloading the server and getting blocked and writing efficient code; create a single BeautifulSoup object per page; avoid making redundant requests)
  - Uniqueness (e.g., a combination of data collected through an API and web scraping)

  **APIs**
  - A single vs. multiple API endpoints
  - Making complex API queries (e.g., chaining a multitude of parameters)
  - Applying pagination strategies (e.g., API results are spread across multiple pages)
  - Just using a package ("plugging in API key, that’s it"), versus actually written code
  - Efficient usage of endpoints (e.g., use search API rather than storing all data and manually looking for a field)
  - Documentation on how to configure API keys, access tokens, and secrets, etc.
  - Reliance on packages vs. self-coded (appropriateness)
  - Obeying retrieval limits (e.g., by means of timers)
  - Uniqueness (e.g., a combination of data collected through an API and web scraping)

  {{< /hint >}}

{{< hint info >}}
__Test your extraction code before submission__

Before submitting, test your extraction code on a different computer (e.g., by a team member), with a different operating system (e.g., Windows, Mac, Linux). This ensures that others can run your code, too! Ideally, you work on a computer that you haven't run your code on ever before, so you also detect whether any packages still need to be installed!

{{< /hint >}}

Keep in mind that the goal of the project is not so much focused on conducting in-depth analyses related to your research question, but more on generating the data!

### **3. Data Package**

- *Quality of the data package (10%)*  
  - Submitted as a zip file
  - Accessible and appropriate directory structure
  - No unnecessary files
  - Inclusion of meaningful supportive files (e.g., API documentation, screenshots, a video of the scraper in action)
  - Raw data files all present
  - Documentation properly formatted and no template text ("lorem ips...") remaining


### Tips for filling in the documentation
-	Try to answer all questions to the best of your ability.
    - Imagine you would have to work with this data in the future – how would you write up the documentation so that you (and your future self) may understand it?
    - In your writing, be as concise as possible. 
    - The original paper on which the readme template is based on provides a few helpful (filled in) examples that may provide some inspiration.
    - If you are familiar with R, you can write your documentation in RMarkdown, which nicely intertwines answers to the questions (e.g., conceptual answers) with details/statistics from the data (i.e., by including code snippets that directly generate overview tables).

- Please pick a good name for your dataset. This name will be the first thing potential users of your data will see. Use it as the *title* of your documentation (don't call your dataset "Datasheets for Datasets"!). Moreover, don't forget to include a title page for your documentation.
