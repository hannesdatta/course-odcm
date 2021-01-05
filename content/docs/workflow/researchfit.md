---
bookFlatSection: true
title: "Evaluation of Research Fit"
description:
bookHidden: false
weight: 20
description: " "
---

# Workflow for collecting online data

## Evaluation of Research Fit

Once you've gotten a better idea of what data is available on the site, you need to assess whether the information that's there actually fits your research purpose.

### Sampling

*Start with evaluating how you could obtain a valid sample from the entities on the site or API. Can you get a random sample? If not, would convenience sampling be "good enough" or pose a serious threat to your study's generalizability?*

- Sampling procedure
- Sample size
- Sampling frequency

After you've carefully inventorized the available data - that's entities and linkages, time coverage, and the extent to which you have control about the data display mechanisms, you can now check on whether the data that is available to you actually fits your research purpose.

The first dimension to consider is sampling. Suppose it's absolutely required to get a randomized sample product prices to scrape, even an alphabetical filter wouldn't guarantee you're seeing the most popular products, in alphabethical older. So you need to think on whether that disqualifies the website for collecting data. Many times, early work in a particular domain doesn't care that much about generalizability, but in the overall phenomena, so it would be defendable to sample from the site, even though you can't guarantee it's randomly sampled. Maybe even you can come up with a quick fix to that problem: suppose you generate a list of random product numbers, and then look at Amazon.com whether these products actually exist, you'd probably build an even stronger case for the randomization of your sample.



First, consider how you could obtain your study sample from the website. If your requirement is to obtain a random sample from the site, how can you actually obtain a random sample? What's the size of that sample, e.g., to meet statistical requirements of power. And what are the implications of sample size on the necessary sampling frequency? Here's an example. I worked on a study on music behavior on Spotify, but I only had access to a sample of users who listen music on a social network - arguably not a random sample of the population. The site was updated in real-time, and I had to visit each user profile pages every 15 minutes. As the fair use policy of the site implied no more than 5 requests per second, that limited be to about 5000 users that I could include - which were enough to meet statitsitcal power requirements.


### Construct measurement

*Then, think about how actually to measure the constructs you're interested in. Websites and APIs provide a lot of information, but which one do you capture, and how do you convert the data into variables you can use in your analysis? Do these variables measure what you're interested in?*

•	Which data, specifically, and how to extract it?
o	E.g., recognizing presence of image, and classifying something as a “new release”
•	Construct validity
o	Does the metric really capture the constructs of interest?
o	Does the firm have a say in how the data is shown?
o	Does the firm disclose how metrics are calculated?
o	Why and how do users contribute to the site (e.g., pay, sample selection)?


The second dimension to consider concerns construct operationalization. In other words, can the constructs that you're interested in actually be measured with the data available on the site or API. [EXAMPLE NEEDED] Suppose you're interested in measuring the number of views for Netflix movies, given the public Netflix website. Well, statistics on the number of views aren't even available to the directors that have *made* a movie or series, so it's hard to make that claim in a paper. Yet, what *is* available on the Netflix site are daily lists of the top 10 movies and series people in a geographic territory have watched. So ask yourself the question on whether you can *still* study the popularity of, let's say, movies and series on Netflix, using such a Top 10 list! It's not views, but it's not bad at all!


### Data structure and mergeability
•	Structure of raw data (e.g., review ID; enhance with dates)
•	Structure of target data (e.g., cross section, time series, panel data, network data)
•	How to get from raw to target data
•	How frequently is the site updated?

*Last, data on a website is typically flat - it's not particularly well arranged to be put into spreadsheets that you need for analysis. So ask yourself: Can the data that's on the site actually be structured in rows and columns so that you can analyze it? And how would you do that? Are mergers available*


When looking for alternative data sources, think about the following characteristics:
- First, extracting data via websites may be difficult; are there APIs available - maybe even from the same service - that ease your data collection efforts?
- Second, is the website or API you've looked at a *primary data provider*, or a *data aggregator*? For example, you can use the Spotify Web API to collect data from Spotify - a primary data provider -, while the API of Chartmetric.com - an aggregator - allows you to extract data not only from Spotify but also from Apple Music, Deezer, and TikTok. This may offer exciting opportunities for broadening or even simplifying the data collection.
- Third, are there publicly available data sets, e.g., Data Science Challenges published on sites like Kaggle? Using them tremendously cuts down your data collection efforts but may pose a threat to study rigor if the data set is poorly documented.


call: proceed with your data collection, or explore alternative sources of data, for example, because (a) either the data that you need isn't there or doesn't fit your research purpose, or (b) because the costs to develop a scraper or the fees you would have to pay to obtain API access are too high.

The third dimension to consider is the data structure available on the site. Is it feasible to *convert* the raw data from the site to a dataset that I couldn't end up analyzing in a statiscial software package? And if so, how? [EXAMPLE NEEDED]
