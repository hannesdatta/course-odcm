---
bookFlatSection: true
title: "About"
bookHidden: false
weight: 20
---

# Workflow for collecting online data

## Introduction

Gathering data from the web requires careful planning and execution, to a similar degree that econometricians carefully calibrate a statistical model, or experimentalists opt for a particular study setup.

In fact, the numerous decisions that researchers have to make when collecting web data have a crucial impact on the study's *relevance* to practitioners and academics, the rigor of the study's research design, and the projected use of resources (e.g., in terms of time, and money).

To guide researchers in making the right decisions, we have structured the process of gathering web data in what we call "the workflow for collecting web data." Think of this workflow as a rich toolkit that you can revisit anytime you want to work on an academic scraping project.

## Quick preview

### Opportunity identification, and initial website or API

Everything starts with identifying an opportunity for gathering web data. For example, such an opportunity could arise from a research project you're already working on but where you've just not managed to find useful field data yet. In other circumstances, you may just have this vague gut feeling that a particular data context may soon become important and hence interesting to study. Once you've identified an opportunity, you can start to no create a list of websites and APIs that could potentially shed light on the idea you're working on.

### Data availability and research fit


### Opportunity identification

 Our goal is to help you plan a data collection properly to gather relevant data, that improve research rigor, while at the same time balancing resource use. We'll come back to the concepts of relevance, rigor, and resource use throughout this process.


It may sound simple, but it is actually not. How to identify an opportunity for scraping data? Unlike what many researchers think, you don't really have to have a research question ready to get started. Sometimes, a mere feeling for a hot data context may be enough to warrant investigating scraping the data.
#


Once you've identified a research idea, or at least have a feeling for a good context, it's time to take a closer look at the site or API that you would like to gather data from. Before you even start building your scraper, you need to pass this stage of the workflow, by crucially reflecting on two key questions:

(1) What data really is available on the site, and
(2) Does the data really fit my research purpose.

Let's briefly zoom in on the first point, which we call "Data availability assessment"
There are actually two main things that you need to do.

First, you need to check what data *really* is available on the site. This step sounds simple, but you'd be amazed to take a closer look at the data.

This is a screenshot of Amazon.com.

and you may browse the site to get an idea on *what exactly* is listed on the site. We call those objects "entities". For example, Amazon.com's (predominant) entity is products like books or movies, but they also have information on not so apparent entities that are tucked away on the site. For example, they list reviewers of their products on the product detail pages, or information about the suppliers of products, such as their assortment.

Also, it's crucial to check the time availability of the data on the site. Is all data available always and can you go back in time? Amazon.com seems to supply endless histories of reviews, but when you take a closer look, you realize boundaries, such as page limits or dates.

Another important aspect of the data availability process is to think how the data can be linked to other data sources, and to check how long the data goes back in time - if at all!

Second, you need to assess the site [...]

Second, you need to assess whether the data fits your research question. Let's stick with the example of Amazon.com and say you want to analyze the effect of review valence (i.e., the stars for the products) on sales. This is what we would typically qualify as an unstudiable quesiton given the current context, as data on sales isn't available on the site.

There are tons of things to mention that could potentially go wrong when you try to relate the data that is *actually* available to you to your research question. It's something like a feasibility check: given what we know about the data, can we actually study what we want to study?






### The big thing





#### Data availability assessment

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

### Extraction plan

[...]









### Other text snippets

Many researchers that gather data from websites or APIs more or less re-invent the process of gathering such data. In fact, some researchers even consider web scraping to be nothing more than a technical skill, which merely requires writing a bit of computer code.

[...]

To make matters even worse, it could also mean you're scraping *your very own personal product recommendations*, which would severely threaten the generalizability of any finding derived from your data. A remedy to this is to understand what algorithms are potentially in place, and how you could make simple tweaks to your code to reduce the likelihood of introducing biases. To avoid scraping only the most popular products, you could turn off the "filter by popularity" option on the site. To avoid scraping your own personal product recommendations, you could delete cookies before turning on your scraper, so that Amazon.com cannot link your visit to your profile.

[...]


When you carefully think about entities, it will help you to broaden your ideas on what potential data a website has to offer. Also, it will allow you to understand how the data could be potentially linked to other data sets - such as via ISBN numbers or UPCs available on a products' page, or the website URLs of third-party sellers. We call this <linkages> that you need to assess.

[...]

###

For example, long before online music streaming was the default, I met a friend's friend at a house party, who told me about this fantastic app called Spotify, which had just launched in The Netherlands at the time. I was amazed by the amount of new music I discovered when using the app. I also noticed my music taste was slowly gravitating from rock music to electronic dance, and - as a researcher - I wondered why? So, I decided to look for data that tracks users' digital music consumption on the web, so that I could study that behavior later.s When browsing the web, I found that amazing social network for music - it's been around for ages, long before Spotify came into existence. That website provided an API which allowed me to extract users' consumption histories.

[...]

So we would like to formally introduce you to the workflwo of automated web data collection, in which we formalize many of the decisions that a researcher has to make. This process is not a fixed rule book you need to adhere to, whatever the role of web data in your project is, you are allowed to modify or even skip some of the parts that we highlight. However, this workflow should be considered a tool to help you increase relevance, improve rigor, and balance resource use while working on your study.

[...]


[...]


### Opportunity identification [academic]

[inspired from Johannes?]
Let me give you an example from my own experience. A few years ago, I scraped data from a social network for listening to music, think of this like an early version of Spotify. My scraper ran on my office computer, and extracted data from the profile pages of about 5,000 users of the site, every 15 minutes, for about 1.5 years. I once went on a short holiday while the scraper was running, and when I returned to my office, my computer was off. Turns out there was a power cut in the building over the weekend. I switched my computer back on, checked the files on the disk, and shockingly noticed that the power cut happened early Saturday morning. I returned back to office after a long weekend on a Wednesday - so I lost four days of valuable data - data that I can't recover because the site doesn't list users' historical profile pages. What's my lesson learnt here? Whenever I scrape, I also actively *monitor* my data collection and send a push message to my phone every day, informing me that the collection is still on. This helps me to prevent errors in collecting data - especially when it concerns data collections that take place over extended periods.
