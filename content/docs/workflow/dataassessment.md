---
bookFlatSection: true
title: "Data Availability and Research Fit Assessment"
description:
bookHidden: false
weight: 2
description: " "
---

# Workflow for collecting online data

##  Data Availability and Research Fit Assessment



### Data Availability Assessment

Let's talk briefly about data availability here:

- Familiarize yourself with the structure of the website or API. What entities are actually available? A typical e-commerce website, for example, not only displays information on products and their reviews, but also allows you to extract information on the *sellers* of products and the *users* that have written the reviews. Check out how these entities could potentially be linked to one another or even to a dataset you're already working on.
- Next, check for what time the data is available on the site or API. Some sources only display data in real-time, while others have historical data available. How long can you go back in time?
- Last, think about why the site or API displays certain content and hides others. In other words, are there any algorithms in place that could potentially distort your data collection?

### Research fit

Once you've gotten a better idea of what data is available on the site, you need to assess whether the information that's there actually fits your research purpose.

- Start with evaluating how you could obtain a valid sample from the entities on the site or API. Can you get a random sample? If not, would convenience sampling be "good enough" or pose a serious threat to your study's generalizability?
- Then, think about how actually to measure the constructs you're interested in. Websites and APIs provide a lot of information, but which one do you capture, and how do you convert the data into variables you can use in your analysis? Do these variables measure what you're interested in?
- Last, data on a website is typically flat - it's not particularly well arranged to be put into spreadsheets that you need for analysis. So ask yourself: *Can* the data that's on the site actually be structured in rows and columns so that you can analyze it? And how would you do that?



When looking for alternative data sources, think about the following characteristics:
- First, extracting data via websites may be difficult; are there APIs available - maybe even from the same service - that ease your data collection efforts?
- Second, is the website or API you've looked at a *primary data provider*, or a *data aggregator*? For example, you can use the Spotify Web API to collect data from Spotify - a primary data provider -, while the API of Chartmetric.com - an aggregator - allows you to extract data not only from Spotify but also from Apple Music, Deezer, and TikTok. This may offer exciting opportunities for broadening or even simplifying the data collection.
- Third, are there publicly available data sets, e.g., Data Science Challenges published on sites like Kaggle? Using them tremendously cuts down your data collection efforts but may pose a threat to study rigor if the data set is poorly documented.




 call: proceed with your data collection, or explore alternative sources of data, for example, because (a) either the data that you need isn't there or doesn't fit your research purpose, or (b) because the costs to develop a scraper or the fees you would have to pay to obtain API access are too high.



Let's say you've narrowed down your search to just a few websites or APIs. A common mistake done by many is to directly go ahead and scraping that data without actually thinking through *which* particular data you need, and whether that data actually fits your research idea.

Therefore, we recommend you to take stock about the *actual* data that's available, on each site or API that may be relevant. Here are our top three questions you definitely need to answer before going ahead with scraping:

First, what entities are available on the site, how can they be linked to existing data sets? Consider a typical e-commerce website like Amazon.com. Entities, obviously, are the products and product reviews. But did you know that Amazon.com also lists information on the particular *users* that are reviewing products (such as where they're from), or information on third-party sellers (such as the shipping fees they charge)? Look for entities, write them down, and think carefully about how you could use these various entities to incorporate in your study. Much of the best publications I've seen use data that is *not* obviously available on the site, but data that's somewhere hidden, where you have to think twice about its potential existence, but when you do incorporate it, it can boost your relevance for practitioners tremendously.

Second, what time period does your website or API cover? Some websites, such as Amazon.com, list historical data on reviews. That means you can easily go back in time and download all of these reviews. Other sections of the website, though, only display information in realtime (such as product prices), which means that if you don't capture the data today, you probably never will be able to capture that data. Even if you think data is historically available, you may be fooled easily: for example, social media tracker Chartmetric.com records historical playlist data, but - surprisingly - most of the tracks where added on the 1st of January, 2016. That does not mean it actually took place, but it's merely an outcome of the company starting *their* data collection sometime in 2016.

Third, which mechanisms affect which data is displayed on the site, and which not? Algorithms that make a site easily navigable (which we love as users) can easily cause distractions in our data collections (which we hate as researchers). Let me give you an example. Suppose you want to calculate average prices in a product category, and you start scraping data from the category pages of Amazon.com. Chance is you'll end up scraping prices for only the most popular products - which certainly are not representative of the whole product assortment on the platform. When screening a site for data availability, it's therefor crucial to look out for options to exert *control* about which data is show. For example, you can sort products also by alphabet, which - arguably - probably isn't related to popularity, and would be a safer selection filter when you're interested in the price of an average product, rather than of the most popular products.

#### Research fit assessment

After you've carefully inventorized the available data - that's entities and linkages, time coverage, and the extent to which you have control about the data display mechanisms, you can now check on whether the data that is available to you actually fits your research purpose.

The first dimension to consider is sampling. Suppose it's absolutely required to get a randomized sample product prices to scrape, even an alphabetical filter wouldn't guarantee you're seeing the most popular products, in alphabethical older. So you need to think on whether that disqualifies the website for collecting data. Many times, early work in a particular domain doesn't care that much about generalizability, but in the overall phenomena, so it would be defendable to sample from the site, even though you can't guarantee it's randomly sampled. Maybe even you can come up with a quick fix to that problem: suppose you generate a list of random product numbers, and then look at Amazon.com whether these products actually exist, you'd probably build an even stronger case for the randomization of your sample.

The second dimension to consider concerns construct operationalization. In other words, can the constructs that you're interested in actually be measured with the data available on the site or API. [EXAMPLE NEEDED] Suppose you're interested in measuring the number of views for Netflix movies, given the public Netflix website. Well, statistics on the number of views aren't even available to the directors that have *made* a movie or series, so it's hard to make that claim in a paper. Yet, what *is* available on the Netflix site are daily lists of the top 10 movies and series people in a geographic territory have watched. So ask yourself the question on whether you can *still* study the popularity of, let's say, movies and series on Netflix, using such a Top 10 list! It's not views, but it's not bad at all!

The third dimension to consider is the data structure available on the site. Is it feasible to *convert* the raw data from the site to a dataset that I couldn't end up analyzing in a statiscial software package? And if so, how? [EXAMPLE NEEDED]






# TAKE OUTS


- TITLE [Sample: For which entities to get data, when?]
- First, consider how you could obtain your study sample from the website. If your requirement is to obtain a random sample from the site, how can you actually obtain a random sample? What's the size of that sample, e.g., to meet statistical requirements of power. And what are the implications of sample size on the necessary sampling frequency? Here's an example. I worked on a study on music behavior on Spotify, but I only had access to a sample of users who listen music on a social network - arguably not a random sample of the population. The site was updated in real-time, and I had to visit each user profile pages every 15 minutes. As the fair use policy of the site implied no more than 5 requests per second, that limited be to about 5000 users that I could include - which were enough to meet statitsitcal power requirements.


In terms of research fit,
And are you able to turn them off? For example, many ecommerce websites display products in descending order of their popularity: best selling on top, worst selling on the bottom. You have control about that display order many times, so it's good to note that down and remember when judging whether the data is good enough for a study. Sometimes you don't have control at all, so check the site's or API's documentation on any details how the data actually gets on the site.
