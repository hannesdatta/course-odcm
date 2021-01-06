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

Once you've gotten a better idea of what data is available on the site, you need to assess whether the information that's there actually fits your research purpose.

### Sampling

*Start with evaluating how you could obtain a valid sample from the entities on the site or API. Can you get a random sample? If not, would convenience sampling be "good enough" or pose a serious threat to your study's generalizability?*

First, consider how you could obtain your study sample from the website. If your requirement is to obtain a random sample from the site, how can you actually obtain a random sample? What's the size of that sample, e.g., to meet statistical requirements of power? And what are the implications of sample size on the necessary sampling frequency?

Here's an example: I worked on a study on music behavior on Spotify, but I only had access to a sample of users who listen music on a social network - arguably not a random sample of the population. The site was updated in real-time, and I had to visit each user profile pages every 15 minutes. As the fair use policy of the site implied no more than 5 requests per second, that limited be to about 5000 users that I could include - which were enough to meet statistical power requirements.

<!--
- Sampling procedure
- Sample size
- Sampling frequency
-->

{{< hint info>}}
Many times, early work in a particular domain doesn't care that much about generalizability, but in the overall phenomena, so it would be defendable to sample from the site, even though you can't guarantee it's randomly sampled. Maybe even you can come up with a quick fix to that problem: suppose you generate a list of random product numbers, and then look at Amazon.com whether these products actually exist, you'd probably build an even stronger case for the randomization of your sample.
{{< /hint>}}

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
