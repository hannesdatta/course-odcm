---
bookFlatSection: true
title: "Grading details"
bookHidden: false
weight: 4
---

# Grading details

## Overview
The team project is submitted as a so-called “data package”, consisting of the following three elements: 

1. Documentation (60% of the final grade)
2. Source code for the scraper(s) (30% of the final grade)
3. Overall quality of the data package (10% of the final grade)

Please follow [Datasheets for Datasets](https://arxiv.org/pdf/1803.09010.pdf) (2018) in writing your documentation. An [empty template](../Datasheets_for_DataSets.zip) is available on the course website. In the grading details below, numbers (#1, #1.4, etc.) refer to sections in the final documentation.


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

#### 1.1 Motivation (10%)
- *Motivation for data context (5%)*  
Clear explanation of the value in collecting the data (“task in mind”), either in the context of a specific research question or business problem. The data collection potentially generates insights into new phenomena. There is clearly value to the larger research community in using the data. Comparable data sets are not available at all, or not publicly available.

- *Motivation for choice of website/API (5%)*  
A range of relevant websites and APIs pertaining to the data context is assessed in terms of data availability, research fit & resource use. It is clear why the data was ultimately collected from the focal website/API, and not from others (i.e., the website/API emerges as the one that fits best in terms of research fit and resource use; #1.4).

#### 1.2 Composition (20%)  
- *Entities, linkages, timeframe and algorithmic biases (5%)*    
The composition of the data is described in detail and accessible to novel users of the data. Potential users learn about which entities are available in the data set, for what time period, and how they are linked to each other. Potential linkages to external data sets are made explicit (e.g., by means of links to external websites or sources that explain more about the used identifiers). Potential algorithmic biases have been identified and clearly explained.

- *Sampling, construct measurement and data structure (5%)*  
For each entity, it is explained how the data was sampled, and how variables are measured. Details are given how the data is available (e.g., by means of CSV files per entity, as a combined data set, etc.). 

- *Data inspection per entity (10%)*  
Each set of entities is accompanied by meaningful summary statistics (e.g., the number of units per entity, means/SD for continuous variables, and frequency distributions per variable, for each entity). Missingness has been investigated (e.g., for individual entities, but also for the collected variables). Any redundancies, errors, or sources of noise have been clearly described. Identified subpopulations are labeled, so that users of the data can more easily get started using the data.


#### 1.3 Collection process (15%)
- *Technical extraction plan (10%)*   
The technical extraction plan has been described in a way that the data collection could be replicated. This encompasses providing a solid argumentation on why a particular data extraction technology used (e.g., selenium versus Beautifulsoup for websites, a package versus self-coded requests for APIs). It is clear how entities were sampled from the site, and how the navigation scheme was implemented. In particular, users of the data learn about the technical hurdles that needed to be overcome, and which monitoring was in place to guarantee (and validate) data quality. Finally, details are given on how (deployment infrastructure) and when the data collection was executed (e.g., by meaningful summaries of the timestamps in log files), and where the final data set was stored during the collection.
Legal and ethical concerns (5%): For #3.6, the potential legal and/or ethical concerns that may be relevant for the collected data are carefully described. 


#### 1.4 Preprocessing (10%)
- *Preprocessing (5%)*  
Any pre-processing on the fly has been motivated and explained, using a few specific examples. Any further pre-processing after the collection has been described (e.g., such as to anonymize users for privacy concerns, to identify and clean out implausible observations, or to improve data structure for long-term storage, such as rearranging the data structure, relabeling columns into more meaningful and clear variable names).

- *Accessibility and structure of final data files (5%)*  
The files have a correct data structure, and variables are of the correct type (e.g., numbers as integers or floats, not as strings; time stamps properly formatted, or Unixtime used). Application of data enrichment and feature engineering strategies (e.g., to derive new variables from the data, where necessary). Data has been normalized (i.e., preferably multiple tables that can be joined together, rather than a wide table that contains many duplicates on some of the variables). If imputation is used, it is indicated which values have been imputed (e.g., interpolated; for example: followers (without missing), and followers_inputed as a TRUE/FALSE variable, indicating which ones were imputed). Finally, the data set is provided in CSV files, including column names, proper use of delimiters (e.g., a “,” may be inappropriate for textual data involving commas). No row names/index column.

#### 1.5 Uses (5%)  
* *Users of the data learn about tasks the data set could be used for (5%)*  
From the description, it is clear how the composition of the data set or the way it was preprocessed might affect future use. A clear indication is given for what the data should not be used for, e.g., relating to any of the legal or ethical concerns identified before.

  
 ### **2. Source Code**
- *Quality of the submitted source code (10%)*  
  - Present and clearly readable (e.g., variable names that are meaningful)
  - Inline markdown formatting (e.g., headers, dividers, paragraphs, etc.)
  - Well structured code (e.g., functions)
  - Adhere to DRY principles (e.g., for-loops and functions)
  - Concise code (e.g., list and dictionary comprehensions)
  - With comments and docstrings 
  - Code blocks run in a linear fashion (i.e., top to bottom execution runs without issues)
  - File paths are specified relative to the current script, no absolute paths used
  -  Error-handling incorporated (e.g., does the scraper still run if the API changes)

- *Quality of the technical implementation (15%)* 
  - The quality of the technical implementation is judged for web scraping and APIs, as per some of the following dimensions.
  
  - **Web scraping**
    - A single vs multiple entities / web pages
    - Degree of complexity required to obtain data (e.g., static websites with a fixed class name vs social media which requires more dynamic approaches such as clicking on buttons and navigating across pages)
    - Stability of the solution (i.e., navigation path should not be subjective to day-to-day page changes). Can the code be run after submission?
    - Usage of timers to avoid overloading the server and getting blocked and writing efficient code (create a single BeautifulSoup object per page; so avoid making redundant requests)
    - Uniqueness (e.g., a combination of data collected through an API and web scraping)

  - **APIs**
    - A single vs multiple API endpoints 
    - Making complex API queries (e.g., chaining a multitude of parameters)
    - Applying pagination strategies (e.g., API results are spread across multiple pages)
    - Just using a package (“plugging in API key, that’s it”), versus actually written code
    - Efficient usage of endpoints (e.g., use search API rather than storing all data and manually looking for a field)
    - Documentation on how to configure API keys, access tokens, and secrets, etc.
    - Reliance on packages vs. self-coded (appropriateness)
    - Uniqueness (e.g., a combination of data collected through an API and web scraping)



### **3. Submission Format & Style**
* Submitted in the right way (zip file)
* Correct / accessible directory structure
* No unnecessary files
* Inclusion of meaningful supportive files (e.g., API documentation, screenshots, a video of the scraper in action)
* Raw data files all present
* Documentation properly formatted 

