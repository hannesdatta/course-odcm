---
bookFlatSection: true
title: "Evaluation of Research Fit"
description:
bookHidden: false
weight: 20
description: "Not all that glitters is gold. Does the data that's available via a site or API really fit your research purpose?"
---

# Workflow for collecting online data

## Evaluation of Research Fit

Once you've gotten a better idea of what data is available on the site, you need to assess whether the available information fits your research purpose.

### Sampling

*Evaluating how to sample entities from the site or API. Does your study require a random population sample? If so, how to obtain it? If random sampling is not feasible, would convenience sampling be "good enough" to warrant publication?*

First, determine the *desired sampling procedure* to obtain data from the site or API. Typically, you choose a sampling procedure for your *seeds* - the first entry point to a site, and then obtain complete information on each of your sampled seeds. For example, when scraping pricing data from an e-commerce website, the "seeds" are all products listed under a particular product category (from which you then visit all product detail pages).

Common sampling procedures to obtain seeds are:
- population sample (you obtain *all* seeds)
- random sample (you obtain a list of *all* seeds, and then take a random sample),
- stratified sample (you obtain a list of *all* seeds, along with some meta data, and then take random samples for stratas of meta dat), and
- convenience sample (you sample from what is shown on the page)

It's mandatory to check whether your desired sampling procedure is also *feasible*. For example, in order for you to be able to draw a random sample from entities on the site, you need to either collect data on all entities first (and then take a random sample of those), *or* find a way to make the website or API obtain a quasi-random sample.

{{< hint info>}}
__Quasi random sampling__

To obtain data on the music listening behavior of users, I scraped the profile pages of customers on a social media site. Of course, it was infeasible to obtain a list of *all* users of the site (from which I could have drawn a random sample). That's why I looked around on the site, and found a page which listed the user names of *recently active users* from the site. That site was also updated in real-time, i.e., upon refreshing the browser, I was able to retrieve a new list of recently active users. While arguably not a random sample from *all users* of the site, this was - indeed - a random sample of *recently active users* of the site.

__Assess need for random sampling__

Many times, early work in a particular domain doesn't care that much about generalizability, but in the overall phenomena, so it would be defendable to sample from the site, even though you can't guarantee it's randomly sampled. Maybe even you can come up with a quick fix to that problem: suppose you generate a list of random product numbers, and then look at Amazon.com whether these products actually exist, you'd probably build an even stronger case for the randomization of your sample.
{{< /hint>}}

#### Effective sample size

Important to consider is also the minimum sample size that you require to satisfy statistical power requirements, or conform with practice in your field of research (e.g., if "everybody" else has sampled 1,000 users, a study with merely 10 users will probably be a hard sell to reviewers).

What makes sampling in web scraping difficult is that you also need to take into account the *technically feasible sample size*.

Let me give an example: suppose you need to obtain data on at least 10,000 users, who you would like to scrape once per hour, and the website's fair use policy requires you to limit your data scraping to max. 


Number of requests per day = Sample size * Number of requests per entity * Number of visits per day





Given the sampling frequency and potential limits to making retrieval requests, your effective sample size can severely shrink.


Let's start with sample size first: it's good practice to first motivate your sample size theoretically by means of calculating statistical power, or motivating sample size by checking comparable studies in the literature.

Second, in what frequency do you need to obtain data




how can you actually obtain such a sample? And how large does your sample need to be, e.g., to meet statistical power requirements? And what are the implications of sample size on the necessary sampling frequency?

Here's an example: I worked on a study on music behavior on Spotify, but I only had access to a sample of users who listen music on a social network - arguably not a random sample of the population. The site was updated in real-time, and I had to visit each user profile pages every 15 minutes. As the fair use policy of the site implied no more than 5 requests per second, that limited be to about 5000 users that I could include - which were enough to meet statistical power requirements.

<!--
- Sampling procedure
- Sample size
- Sampling frequency
-->


### Construct measurement

*Think about how actually to measure the constructs you're interested in. Websites and APIs provide a lot of information, but which one do you capture, and how do you convert the data into variables you can use in your analysis? Do these variables measure what you're interested in?*

The second dimension to consider concerns construct operationalization. In other words, can the constructs that you're interested in actually be measured with the data available on the site or API. The most typical extraction method when scraping is to capture text. However, information can also be extracted from the *presence* or *absence* of certain images (e.g., the "Top Reviewer Badge", that's displayed alongside a review, allowing you to potentially detect commercial reviewing activity).

Then, ask yourself whether the construct you're interested in can actually be measured with sufficient validity. Do the data points *really* capture the construct of interest? Are there any biases (e.g., algorithmic interference) present, and is it clear how the metric is computed (e.g., lack of transparency)?

{{< hint info>}}

Suppose you're interested in measuring the number of views for Netflix movies, given the public Netflix website. Well, statistics on the number of views aren't even available to the directors that have *made* a movie or series, so it's hard to make that claim in a paper. Yet, what *is* available on the Netflix site are daily lists of the top 10 movies and series people in a geographic territory have watched. So ask yourself the question on whether you can *still* study the popularity of, let's say, movies and series on Netflix, using such a Top 10 list! It's not views, but it's not too bad afterall. Recognize the limitations, and seize opportunities!
{{< /hint>}}

### Data structure and mergeability

*Data on a website is typically flat - it's not particularly well arranged to be put into spreadsheets that you need for analysis. So ask yourself: Can the data that's on the site actually be structured in rows and columns so that you can analyze it? And how would you do that?*

-	Structure of raw data (e.g., review ID; enhance with dates)
-	Structure of target data (e.g., cross section, time series, panel data, network data)
- How to get from raw to target data
- How frequently is the site updated?

{{< hint warning>}}
__Go or no-go? Avenues to look for alternative data sources__

After having assessed the research fit of the website or API, it's time to make a call: proceed with the data collection, or look for alternative sources because the data that you need isn't there or doesn't fit your research purpose.

If you deem the data collection infeasible, you have several opportunities to look for alternative data sources:
- If you so far have only considered websites, maybe you can find (commercial) APIs that provide similar data - maybe even from the same service, to ease data collection efforst?
- Is the website or API you've looked at a *primary data provider*, or a *data aggregator*? For example, you can use the Spotify Web API to collect data from Spotify - a primary data provider -, while the API of Chartmetric.com - an aggregator - allows you to extract data not only from Spotify but also from Apple Music, Deezer, and TikTok. This may offer exciting opportunities for broadening or even simplifying the data collection.
- Are there publicly available data sets, e.g., Data Science Challenges published on sites like Kaggle? Using them tremendously cuts down your data collection efforts but may pose a threat to study rigor if the data set is poorly documented.

{{< /hint>}}

{{< button relref="/dataextraction.md" >}}Next{{< /button >}}
