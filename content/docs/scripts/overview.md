---
bookFlatSection: true
title: "Workflow - Overview"
bookHidden: false
weight: 1
---

# Workflow for collecting online data

## Introduction

Gathering data from the web requires careful planning and execution, to a similar degree that econometricians think about model calibration, or experimentalists opt for a particular study design over another.

In fact, the numerous decisions that you will have to make when collecting data from the web have a crucial impact on your study's *relevance* and *rigor*. *Relevance* means that managers or public policy makers can make more informed and better decisions, based on your study's findings. *Rigor*, in turn, means whether your study has been correctly executed, such that the research community will actually believe the findings that you're reporting.

To guide you in making the right decisions when embarking on your scraping project, we provide you with a toolkit that helps you *think conceptually* about how to gather data from the web. We call our toolkit the "workflow for collecting web data", and I'll walk you through it right now.

## Quick preview

### 1. Opportunity Identification

Everything starts with identifying an opportunity for gathering data from the web. Such an opportunity could arise from a research project you're already working on but where you've just not managed to find useful field data yet. In other circumstances, you may just have this vague gut feeling that a particular data context may soon become important and hence interesting to study. Once you've identified an opportunity, start searching the web and make a list of potential websites to scrape, or APIs to retrieve data from.

### 2. Data Availability and Research Fit Assessment

From your list of websites and APIs, pick one that you think is the best candidate for gathering data, and (a) assess what data is really available on the site, and (b) whether the data actually fits your research purpose.

### Data Availability Assessment

Let's talk briefly about data availability here:

- Familiarize yourself with the structure of the website or API. What entities are actually available? A typical e-commerce website, for example, not only displays information on products and its reviews, but also allows you to extract information on the *sellers* of products, and the *users* that have written the reviews. Check out how these entities could potentially be linked to one another, or even to a dataset you're already working on.
- Next, check for what time period the data is available on the site or API. Some sources only display data in real-time, while others have historical data available. How long can you go back in time?
- Last, think about why the site or API displays particular content, and hides other. In other words, are there any algorithms in place that could potentially distort your data collection?

### Research fit

Once you've gotten a better idea on what data is available on the site, you need to assess whether the data that's there actually fits your research purpose.

- Start with evaluating how you could obtain a valid sample from the entities on the site or API. Can you actually obtain a random sample? If not, would convenience sampling be "good enough", or pose a serious threat to your study's generalizability?
- Then, think about how to actually measure the constructs you're interested in. Websites and APIs provide a whole lot of information, but, which one do you capture, and how do you convert the data into variables that you can use in your analysis? Do these variables really measure what you're interested in?
- Last, data on a website is typically flat - it's not particularly well arranged to be put into spreadsheets that you need for analysis. So ask yourself: *Can* the data that's on the site actually be structured in rows and columns, so that you can analyze it? And how would you do that?

Once you've assessed data availability and research fit, you have to make a tough call: proceed with your data collection plan, or explore alternative sources of data, for example because (a) either the data that you need isn't there or doesn't fit your research purpose, or (b) because the costs to develop a scraper or the fees you would have to pay to obtain API access are too high.

When looking for alternative data sources, think about the following characteristics:
- First, extracting data via websites may be difficult; are there APIs available - maybe even from the same service - that ease your data collection efforts?
- Second, is the web site or API you've looked at a *primary data provider*, or a *data aggregator*? For example, you can use the Spotify Web API to collect data from Spotify - a primary data provider -, while the API of Chartmetric.com - an aggregator - allows you to extract data not only from Spotify, but also from Apple Music, Deezer, and TikTok. This may offer interesting opportunities for broadening, or even simplifying the data collection.
- Third, are there publicly available data sets, e.g., Data Science Challenges published on sites like Kaggle? Obviously, using them tremendously cuts down your data collection efforst, but may pose a threat to study rigor if the data set is poorly ducmented.

Finally, make a call whether to proceed with the website or API, or identify alternative sources and re-conduct your data availability and research fit assessment.


### 3. Data extraction plan

Once you've made a choice for a website to actually scrape, it's time to get into the little nitty greedy technical details. The goal of working on a data extraction plan is to have a detailed roadmap that guides you in writing the necessary computer code to extract the information from the website or API. Think of it as a rulebook, that you could also hand off to a programmer, who could assist you in writing the data extraction code.

1. First, determine which entities you would like to get. If these entitites are sampled from the site directly, how do you get to that initial list? Be as specific as possible: go here, obtain the first 1000 products there, then start scraping these pages, etc.
2. Second, determine the frequency of data collection. For historical data, that's typically just once, unless you want to refresh your data towards the end of your project. For data that's only available in real time, things get more complicated and you need to balance the number of entities in your data, the extraction frequency, and the limits imposed by the website, such as only 5 requests per second.
3. Third, map out the exact navigation path on the site. Which page to open, for which entities? This becomes a loop in your data extraction code. What interaction is necessary: is it enough to visit a website with a link, or do you need to simulate clicks and scrolling behavior? Similarly, if not all units are shown at once, how can you reach the remaining units (e.g., via pagination/looping)?
4. Fourth, decide whether to store raw data during the collection procedure. The upside of storing raw data is you could extract data you haven't planned for. The downside is you may breach privacy laws, or exceed your disk space.
5. Fifth, select data for extraction, and prototype data capture in Python or Juptyer Notebook. Can you make use of HTML tags, or do you need to make use of CSS or XPATH selectors?
6. Sixth, and finally, determine how to store the data. What's the file format: do you make use of flattened CSV files, or unstructured JSON files? Do you store it in a database or in files? And, finally, do you store it on a local computer, or somehwere in the cloud?

When you're done, you're entering another feedback loop, i.e., to assess the legal compliance about your data extraction strategy. Sometimes website prohibit the use of scrapers, but with a valid research purpose, you may be able to overwrite that and still do it. Sometimes data is hidden after a login screen, but also available before the login screen. Can you do with such data, too? Maybe you can limit the scope of the collection, and hence limit your exposure to legal risk in a way that makes your data collection more sustainable.

### 4. Collection

Wow, that is indeed a lot of planning, but... you've finally entered the data collection stage.

- Make a choice for a software toolkit to use. If you're using an API, does this API have a package available in Python you could use? Or is it more advisable to self-program an interface?
- For websites, can you read the websites content without actually seeing them (e.g., via BeautifulSoup), or do you need to actually open a browser and "simulate" a user, such as clicking behavior? Or - are there commercial packages available you could use?

- Second, on what infrastructure will you run the scraper? Your local PC may be cheap (you already own it), but how do you get that done, given you will have to restart your computer once in a while, or put it in your bag while traveling? A remote system, such as on a computer in the cloud, may be more durable.

- Third, how do you build in monitoring functionality in your code to inform you about what's wrong? For example, with a live data collection, can you put systems in a place that inform you about the health of your data collection?

The chance is high that you have to revise your scarper while it is running, e.g., to fix mistakes when it is broken, or to add additional data. We also recommend you keep an eye on the focal firm's blog for any important service announcements, such as server downtimes, updates to algorithms, etc.

### 5. Preprocessing and documentation

After you've collected your data, it's time to preprocess and document it. Of course, when working on a live data collection, it makes a lot of sense preprocessing and documenting the data already while it is being collected.

Adhere to the following tips:

- Preprocessing means you have to clean the data, such as taking out unnecessary HTML tags in text you've extracted. It involves transfomration (such as anonymizing certain fields, or recoding them), and it involves making a decision about the final data format, for example long-to-wide conversions, or normalization.

- After preprocessing, you can continue to validate the data. Check the log files you've written: were there any interruptions? What does that mean for hte uqliaty of your data? Also check the raw data if you stored it: are there any new variables that popped up? Finally, check the preprocessed data: are all variables GDPR compliant? Are there any weird characters caused by encoding issues?

- Finally, document the data set for both internal and external use. If you plan using the data set only with your driect colleagues, share information on the composition of the data set (i.e., the entities and timeframe), collection process (any errors)?, the amount of preprocessing you've done, and start having a plakboek with instiutional backgrounds such as screenshots, a PDF version of the API documentation, or some blog articles about the site. Note that working on an academic study takes a long time, and chance is the site will change substantially in a while, so you have to take copies. If you plan on distributing the site externally, also include a statement of motivation of why you've collected the data. This will help people make more informed choices when they think about reusing your data. Also tell them for what you think the data is useful for, and what not. Mostly in the latter category, you'd be surprised how many times data gets used for impossible purposes because that hasn't been said. Finally, make a call for licensing the data.

While you're working on the project, kyou have to keep it up-to-date. Revalidate new data, and add documentation to it. Also track your teams errors, and fix those in the data. No scraping collected data set is perfect, so work on this conitnuously.

#### 6. Use

The last step is why you've gone down the route of collecting data in the first place: to *put it into productive use* - probably for an academic paper. This stage involves the dissemination of data to your collaborators and team members, use the data in your analysis, and report the results.


To sum up - scraping involves numerous decisions along the way. Carefully review those when you embark on a scraping project, so that you can work on your best possible study.
