---
bookFlatSection: true
title: "Introduction"
bookHidden: false
weight: 1
---

# Workflow for collecting online data

## Introduction

Gathering data from the web requires careful planning and execution, to a similar degree that econometricians calibrate statistical models, or consumer psychologists opt for a particular design for their experimental study.

The numerous decisions you will have to make when collecting data from the web have a crucial impact on your study's *relevance* and *rigor*. *Relevance* means that managers or public policymakers can make more informed and better decisions based on your study's findings. *Rigor*, in turn, implies whether your research has been correctly executed, such that the research community will trust your conclusions.

To guide you in making the right decisions when embarking on your scraping project, we provide you with a toolkit that helps you *think conceptually* about how to gather data from the web. We call this toolkit the "workflow for collecting web data", and I'll walk you through it right now.

### 1. Opportunity Identification

The workflow starts by identifying an opportunity for gathering data from the web. Such an opportunity could arise from a research project you're already working on but where you've just not managed to find useful field data yet. In other circumstances, you may only have this vague gut feeling that a particular data context may soon become important and hence interesting to study.

Once you've identified an opportunity, start searching the web and make a list of potential websites to scrape or APIs to retrieve data from.

### 2. Data Availability and Research Fit Assessment

From your list of websites and APIs, pick one that you think is the best candidate for gathering data, and assess what data can be extracted from it.

When visiting a typical e-commerce website, for example, you would notice that you can extract information on products and its reviews. Yet, such sites may also allow you to extract information on other, less obvious entities, such as the *users* that have written product reviews, or the *sellers* of products. Also check for what time data is available on the site or via the API, and try to understand how algorithms - such as ranking or recommendation algorithms - may affect which data you will capture.

Then, assess whether the available data fits your research purpose. For example, you may realize that the website or API does not provide historical data, which would require you to scrape data in real-time. Suppose your study's minimum data requirement is two years, implying your data collection also has to run for two years. Is that realistic? Also, think about sampling: if your study's goal is to generalize to a population, then obtaining a *random* sample from the site or API is a requirement. How can that be achieved?

Once you've assessed data availability and research fit, you have to make a decision to either proceed with your data collection from the site or API you've just reviewed, or explore alternative data sources instead. Situations in which you consider alternative data sources may not only arise from a lack of research fit, but also involve projected resource use such as development time and costs for scrapers, or license fees for commercial APIs. When looking for alternative data sources, try to also consider
- data aggregators rather then only primary data providers,
- APIs of services where you've just found a website, or
- published and publicly accessible data sets.

Re-conduct your data availability and research fit assessment for your second-best candidate, which may give you the data you need.

### 3. Extraction Plan

Once you've picked a website or API to extract data from, you need to make a plan to define for which entities you would like to gather data, and in what frequency to retrieve such data. Also, you need to map out the exact navigation path you would like your scraper to follow - such as opening specific website URLs, simulating user behavior such as logging in, clicking or scrolling, or looping through the results of an API call. Finally, you need to decide which specific data you could like to record from the website, and how to store it - for example in database in the cloud, or simply as files in your local computer.

Next, you pick the software toolkit to program your scraper. If you're using an API, does this API have a package available in Python you could use? Or is it more advisable to self-program an interface? For websites, can you read the website's content without actually seeing them (e.g., via BeautifulSoup), or do you need to open a browser and "simulate" user behavior, such as clicking? Or are there commercial packages available you could use?

Then, you pick the hardware infrastructure for the deployment of your scraper. Your local PC may be cheap (you already own it), but how do you get that done, given you will have to restart your computer once in a while or put it in your bag while traveling? A remote system, such as on a computer in the cloud, maybe more durable.

Finally, you decide how to monitor the data collection while it is running. That's particularly important for data collections that gather real-time data, but may also be useful for data one-shot data collections to verify that all of the requested data, in fact, has been obtained.

On a final note, I would like to remark that making your data extraction plan is nothing you simply do on paper. In fact, I always prototype a data collection during this phase, e.g., by trying out how easy it is to extract particular data, or get certain packages to work.

When you're done, you're entering another feedback loop, i.e., to assess your data extraction plan's legal compliance. Sometimes websites prohibit the use of scrapers, but with a good research purpose, you may be able to overwrite that and still do it. Some data may be considered personal data under the GDPR, which may prevent you from storing it in the first place, so you would have to anonymize data on-the-fly.

### 4. Collection

After planning your data collection, it's finally time to start collecting the data. In this phase of your research. Make sure to regularly monitor the data collection while it is running. For long data collections - some for which I haven't even determined an endpoint yet - I make use of daily mobile push messages that inform me about whether the data collection is still running. That way, I can quickly intervene should my extraction code become buggy.

I also recommend you keep an eye on the focal firm's blog for any important service announcements, such as server downtimes, updates to algorithms, etc.

### 5. Preprocessing and documentation

After you've collected your data, it's time to preprocess and document it. When working on a live data collection, it makes a lot of sense to preprocessing and documenting the data already while it is being collected.

Preprocessing entails the cleaning of your data, so it can be used in your project. For example, you may have to remove unnecessary HTML tags from text you've extracted. In other circumstances, you may want to anonymizing specific data points to make its storage GDPR-compliant. Also, you have to choose the final data format for your data.

After preprocessing, you validate the data. Check the log files of your scraper: were there any interruptions while the data collection was running? What does that mean for the quality of your data? Also, check the raw data if you stored it: are there any new variables that popped up, and that may also be relevant for your study? Finally, check the preprocessed data: are all variables GDPR-compliant? Are there any weird characters, which may point to encoding issues?

Finally, document the data set for both internal and external use. If you plan using the data set only with your direct colleagues, share information on the composition of the data set (i.e., the entities and timeframe), collection process (any errors)?, the amount of preprocessing you've done, and start gathering information on the institutional background of your data collection with screenshots, a PDF version of the API documentation, or some PDF-ed blog articles from the site. Note that working on an academic study takes a long time, and the chance is the site will change substantially in a while, so you have to make copies. If you plan on distributing the site externally, also include a statement of the motivation of why you've collected the data. This will help people make more informed choices when they think about reusing your data. Also, tell them what you think the data is useful for and what not. Mostly in the latter category, you'd be surprised how many times data gets used for impossible purposes because that hasn't been saying. Finally, decide for a license for the data.

Note that your dataset won't be perfect instantenously. While you're working on your research, revisit the data preprocessing and documentation steps, and keep it up-to-date.

### 6. Use

The last step is why you've gone down the route of collecting data in the first place: to *put it into productive use* - probably for an academic paper. This stage involves disseminating data to your collaborators and team members, using the data in your analysis, and reporting the results.


To sum up - scraping involves numerous decisions along the way. Carefully review those when you embark on a scraping project so that you can work on your best possible study.
