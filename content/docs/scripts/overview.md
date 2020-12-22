---
bookFlatSection: true
title: "Workflow - Overview"
bookHidden: false
weight: 1
---

# Workflow for collecting online data

## Introduction

Gathering data from the web requires careful planning and execution, to a similar degree that econometricians think about model calibration, or experimentalists opt for a particular study design over another.

In fact, the numerous decisions that you will have to make when collecting web data have a crucial impact on your study's *relevance* and *rigor*. *Relevance* means that managers or policy makers can actually change their decision making, based on your study's findings. *Rigor*, in turn, means on whether the study has been carefully execute, such that the research community will actually believe in the findings that you're reporting.

To guide you in making the right decisions when embarking on your academic scraping project, we provide you with a toolkit that helps you *think conceptually* about how to gather data from the web. We call our toolkit the "workflow for collecting web data", and it's structured in six stages.

## Quick preview

### 1. Opportunity Identification

Everything starts with identifying an opportunity for gathering web data. Such an opportunity could arise from a research project you're already working on but where you've just not managed to find useful field data yet. In other circumstances, you may just have this vague gut feeling that a particular data context may soon become important and hence interesting to study. Once you've identified an opportunity, start searching the web for relevant websites and APIs, and note them down.

### 2. Data Availability and Research Fit Assessment

From your list of websites and APIs, pick the one you think is the best candidate for gathering data, and assess (a) what data is really available on the site, and (b) whether the data actually fits your research purpose.

### Data Availability Assessment

Let's talk briefly about data availability here:

- Familiarize yourself with the structure of the site, and what entities (such as products, users, reviews, firms) are actually available on the site. Check out how these entities could potentially be linked to one another, or to a dataset you're already working on.
- Check for what time period the data is available. Some websites only display data in real-time, while others have historical data. How long can you go back in time?
- Think about why the website displays particular content, and hides other. In other words, are there any algorithms in place that could potentially distort your data collection?

### Research fit

Once you've gotten a better idea on what data is available on the site, you need to assess whether the data that's there actually fits your research purpose.

- First, evaluate how you could obtain a valid sample of entities, for example products, users, or reviews from the site. Can you actually obtain a random sample? If not, is that any problem for your study?
- Second, think about how to actually measure the constructs you're interested in. A website has a whole lot of information - which one do you scrape, and how do you convert them into variables? Do these variables really measure what you're interested in?
- Third, data on a website is typically flat - it's not particularly well arranged to be put into spreadsheets that you need for anlysis. Ask yourself: *Can* the data that's on the site actually be structured in rows and columns, so that you can analyze it?

Once you've assessed data availability and research fit, you have to make a tough call: proceed with the workflow, or explore alternative sources of data, because (a) either the data that you need isn't there or doesn't fit your research purpose, or (b) because the costs to develop a scraper or pay API fees is to high that you can't afford it. You have a bunch of alternative routes to take, such as cooperating with firms directly, subscribing to an API, or find alternative websites with simila funcitonality.

### 3. Data extraction plan

Once you've made a choice for a website to actually scrape, it's time to get into the little nitty greedy technical details. The goal of the data extraction plan is to hand off a rule book to a rpogrammer, who could assist you in writing the data extraction kit, or, in a sense, a detailed roadmap to do it yourself.

1. First, determine which entities you would like to get. If these entitites are sampled from the site directly, how do you get to that site? You need to make it as specific as possible: go here, obtain the first 1000 products. And then strat scraping their pages.
2. Second, determine the frequency of data collection. For historical data, that's typically just once, unless you want to refresh your data towards the end of your project. For data that's only available in real time, things get more complicated and you need to balance the number of entities in your data, the extraction frequency, and the limits imposed by the website, such as only 5 requests per second.
3. Third, map out the exact navigation path on the site. Which page to open, for which entities? This becomes a loop in your data extraction code. What interaction is necessary: is it enough to visit a website with a link, or do you need to simulate clicks and scrolling behavior? Similarly, if not all units are shown at once, how can you reach the remianing units (e.g., via pagination/looping)?
4. Fourth, decide whether to store raw data. Each website today is about 1MB of size. The upside of storing raw data is you could extract data you haven't planned for. The downside is you may breach privacy laws, or exceed your disk space.
5. Fifth, select data for extraction, and protoytpe those in Python ro Juptyer Notebook. Can you make use of HTML tags, or do you make use of CSS or XPATH selectors?
6. Sixth, and finally, determine how to store the data. What's the file format: do you make use of flattened CSV files, or unstructured JSON files? Do you store it in a database or in files? And, finally, do you store it on a local computer, or somehwere in the cloud?

When you're done, you're entering another feedback loop, i.e., to assess the legal compliance about your data extraction strategy. Sometimes website prohibit the use of scrapers, but with a valid research purpose, you may be able to overwrite that and still do it. Sometimes data is hidden after a login screen, but also available before the login screen. Can you do with such data, too? Maybe you can limit the scope of the collection, and hence the exposure to legal risk in a way that makes your data collection better.

### 4. Collection

Wow, that is indeed a lot of planning, but... you've finally entered the data collection stage.

- Make a choice for a sfotware toolkit to use. If you're using an API, does this API have
 a package available in Python you could use? Or is it more advisable to self-program an interface?
- For websites, can you read the websites content without actuallys eeing them (e.g., via BeautifulSoup), or do you need to actually open a browser and "simulate" a user, such as clicking behavior? Or - are there commercial packages available you could use.

- Second, on what infrastructure to run the scraper. Your local PC may be cheap (you already own it), but how do you get that done, given you will have to restart your computer once in a while, or put it in your bag while traveling? A remote system, such as on a computer in the cloud, may be more durable.

- Third, how do you build in monitoring functionality in your code to inform you about what's wrong? For example, with a live data collection, can you put systems in a place that inform you about the health of your data collection?

The chance is high that you have to revise your scarper while it is running.e.g, to fix mistakes when it is borken, or to add additional data. WE also recommend you keep an eye on the focal firm's blog for any important service announcements, such as server downtimes, updates to algorithms, etc.

### 5. Preprocessing and documentation

After you've collected your data, it's time to preprocess and document it. Of course, when working on a live data collection, it makes a lot of sense preprocessing and documentating the data already while it is being collected.

It involves a couple of stages:
- Preprocessing means you have to clean the data, such as taking out unnecessary HTML tags in text you've extracted. It involves transfomration (such as anonymizing certain fields, or recoding them), and it involves making a decision about the final data format, for example long-to-wide conversions, or normalization.
- After preprocessing, you can continue to validate the data. Check the log files you've written: were there any interruptions? What does that mean for hte uqliaty of your data? Also check the raw data if you stored it: are there any new variables that popped up? Finally, check the preprocessed data: are all variables GDPR compliant? Are there any weird characters caused by encoding issues?
- Finally, document the data set for both internal and external use. If you plan using the data set only with your driect colleagues, share information on the composition of the data set (i.e., the entities and timeframe), collection process (any errors)?, the amount of preprocessing you've done, and start having a plakboek with instiutional backgrounds such as screenshots, a PDF version of the API documentation, or some blog articles about the site. Note that working on an academic study takes a long time, and chance is the site will change substantially in a while, so you have to take copies. If you plan on distributing the site externally, also include a statement of motivation of why you've collected the data. This will help people make more informed choices when they think about reusing your data. Also tell them for what you think the data is useful for, and what not. Mostly in the latter category, you'd be surprised how many times data gets used for impossible purposes because that hasn't been said. Finally, make a call for licensing the data.

While you're working on the project, kyou have to keep it up-to-date. Revalidate new data, and add documentation to it. Also track your teams errors, and fix those in the data. No scraping collected data set is perfect, so work on this conitnuously.

#### 6. Use

The last step is why you've gone down the route of collecting data in the first place: to *put it into productive use* - probably for an academic paper.

- Disseminate the data to your coauthors
- Use the data in analyses
- And report results.


To sum up - scraping involves numerous decisions along the way: especially data assessment and research fit, and extracvtion plan are processes involved that amount to a shere amount of decisions. Carefully review those when you embark on a scraping project, so that you can work on your best possible study.

Thanks for watching this overview video about the scraping workflow.
