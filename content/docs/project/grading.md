---
weight: 5
bookFlatSection: true
title: "Grading"
bookHidden: false
description: "This section goes over the necessary components of the team project and its grading details, along with an overview of the self- and peer assessment."
---


# Project Grading

## Overview
The goal of this team project is to collect and document data through web scraping and/or APIs within a self-chosen research context or business idea. The primary focus is on data generation rather than conducting in-depth analyses related to the research question.

The team project is submitted as a so-called “data package”, consisting of the following two elements:

1. Source code and accompanying files (50% of the final grade)
2. Documentation of the data collection (50% of the final grade)

Students' team project grades will be corrected upwards or downwards, depending on students' individual contribution to the overall team effort. [Learn more here](resources/peerassessment).


{{< hint info>}}

**Be ready for publication**

Please submit the data package in such way that it can be made publicly available on the internet.

- For example, you need to fully anonymize information that could be considered sensitive or personal, such as names or other personal information. 
- Also, you must not store any of your personal passwords in code. 
- Do you want to keep your names on a public data package or would you rather prefer to blank out your names (in that case, just take them out - I'll be able to match your grade using your team number).
- Finally, do a check on whether the statements made in your documentation are realistic.

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


### **1. Source Code and Accompanying Files**

- *Quality of the technical implementation (30%)*
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


- *Quality of the submitted data package and source code (20%)*  
  - Source code present and clearly readable (e.g., variable names that are meaningful)
  - Inline markdown formatting (e.g., headers, dividers, paragraphs, etc.)
  - Well-structured and modular source code (e.g., use of functions)
  - Adhere to DRY principles (e.g., for-loops and functions)
  - Concise code (e.g., list and dictionary comprehensions)
  - With comments and docstrings
  - Code blocks run in a linear fashion (i.e., top to bottom execution runs without issues); removal of unnecessary source code and packages that are not needed
  - File paths are specified relative to the current script, no absolute paths used
  -  Error-handling incorporated (e.g., does the scraper still run if the API or website changes?)
  - Data package submitted as a zip file with an accessible and appropriate directory structure
  - Any unnecessary files (e.g., temporary files) have been removed.


{{< hint info >}}
__Test your extraction code before submission__

Before submitting, test your extraction code on a different computer (e.g., by a team member), with a different operating system (e.g., Windows, Mac, Linux). This ensures that others can run your code, too! Ideally, you work on a computer that you haven't run your code on ever before, so you also detect whether any packages still need to be installed!

{{< /hint >}}

{{< hint info >}}
__Directory and file structure__


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

{{< /hint >}}


### **2. Documentation**

You must use this [template](/docs/project/Datasheets_for_DataSets.zip) to create your documentation and fill in __all (sub-)questions in sections 1-6__. 

Please refer to the [grading rubric](../../other/odcm-project-rubric.pdf) for further details on the assessment criteria for the data documentation.

{{< hint info>}}
***Disclaimer:***
The same grading rubric will be used to provide preliminary feedback during the coaching sessions. For these sessions, the sub-criteria are simplified to "Very good", "Sufficient", and "Needs improvement" serving as preliminary feedback to indicate whether the project is on track. The detailed sub-criteria outlined above, however, will be applied for the final grade calculation.


{{< /hint>}}

## Tips for filling in the documentation

- Please include screenshots and/or an additional recording in your documentation. Not only will this improve interpretability, it also contributes to the accuracy and reproducability of the project!

-	Try to answer all questions to the best of your ability.
    - Imagine you would have to work with this data in the future – how would you write up the documentation so that you (and your future self) may understand it?
    - In your writing, be as concise as possible. 
    - The [original paper](https://arxiv.org/pdf/1803.09010.pdf) on which the readme template is based on provides a few helpful (filled in) examples that may provide some inspiration.
    - If you are familiar with R, you can write your documentation in RMarkdown, which nicely intertwines answers to the questions (e.g., conceptual answers) with details/statistics from the data (i.e., by including code snippets that directly generate overview tables).

- Please pick a good name for your dataset. This name will be the first thing potential users of your data will see. Use it as the *title* of your documentation (don't call your dataset "Datasheets for Datasets"!). 
- Don't forget to include a title page for your documentation.
