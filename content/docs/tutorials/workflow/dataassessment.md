---
bookFlatSection: true
title: "Data Availability Assessment"
description:
bookHidden: false
weight: 10
description: "Learn to critically look at a website or API, and really try to understand which data you can retrieve, and which not."
---

# Data Availability Assessment

Let's say you've narrowed down your search to just a few websites or APIs. Do not just go ahead and scrape the data immediately. You first need to critically assess *which* particular data is available on the site or API.

Assessing data availability is vital to guarantee a minimum level of rigor. For example, you may notice that the existence of personalization algorithms could compromise your study's validity. Also, investigating data availability may help you to enhance the relevance of your study. For example, you may encounter new data that would allow you to address multiple stakeholders in a particular business setting.

## Entity Coverage and Linkages

*What entities are actually available? A typical e-commerce website, for example, not only displays information on products and their reviews but also allows you to extract information on the sellers of products and the users that have written the reviews. Check out how these entities could potentially be linked to one another or even to a dataset you're already working with.*

__Which entities are available?__

Familiarize yourself with the structure of the website or API to understand which entities (e.g., consumers, products, reviews) are available. Consider a typical e-commerce website like Amazon.com. Entities are the products and product reviews. But did you know that Amazon.com also lists information on the particular *users* that are reviewing products (such as where they're from), or information on third-party sellers (such as the shipping fees they charge)? Look for entities, write them down, and think carefully about how you leverage the data from various entities in your study.

{{< hint info >}}
Much of the best publications I've seen use data that is *not* "obviously" available on the site, but data that's somewhere hidden. Where you have to think twice about its potential existence. But when you *do* incorporate it, such data can boost the relevance for practitioners tremendously.
{{< /hint >}}

__How many entities are available?__

Try to understand how many entities are available on the site, and how many of those you can actually retrieve. For example, the category pages on Amazon.com only list a few hundred products - out of potentially ten thousand of products per category. So, while it *seems* data is abundantly available, it's not so straightforward that all data can actually be retrieved easily.

__How are entities identified?__

When extracting data, you need to specify the exact location of where to find that data. Typically, this is done by programatically opening the URL of website or API, appended with an identification number for a particular entity. For example, Amazon.com uses ASINs (UPCs) to point to a product page (e.g., [`https://www.amazon.com/dp/B087BC4DJH/`](https://www.amazon.com/dp/B087BC4DJH/)), and the same ID is used to also point to the review pages (e.g., [`https://www.amazon.com/product-reviews/B087BC4DJH/`](https://www.amazon.com/product-reviews/B087BC4DJH/)). In other circumstances, IDs are merely numbers without any particular meaning (e.g., such as Chartmetric's artist IDs, which are only used internally). Other data sources may use commonly accepted identifiers (e.g., such as [Songkick](https://www.songkick.com/developer/upcoming-events-for-artist), which allows users of their API to query for on artist's upcoming concerts using an artist's "Musicbrainz ID" from [Musicbrainz.org](https://musicbrainz.org)).

__How are entities linked to one another?__

Another crucial assessment to make is how entities are linked to one another, if at all. For example, the product overview pages at Amazon.com list the ASINs of each product in the website's source code. Using this list, you can then visit the product pages of each product, and thereby start constructing your data set. This is an example of a consistent linking scheme that can be readily scraped. Other sections of the website or other services may not provide such linkages, or make it difficult for researchers to navigate the website for data extraction.

<!--[For example [...do we have an example of stuff that's NOT linked?]-->

__How can entities be linked to external entities?__

After assessing the internal linkage structure, critically reflect how entities may potentially be linked to external data sources. For example, websites may list existing identifiers (e.g., in an e-commerce setting, Amazon.com lists book ISBNs, next to their own ASINs). Music intelligence provider Echonest.com, in its early days, allowed users to query their API for so-called Musicbrainz IDs. This allowed the service to grow and be usable (as Musicbrainz IDs were and still are used widely) and offered opportunities for researchers to gather meta data for existing data sets.

Linkages could also be established by string-based matching. For example, the web API of Songkick allows users to search for artists based on their (approximate) names (so-called fuzzy matching).

Finally, linkages need not be explicitly present on the site or API. Suppose a researcher was interested in merely gathering data from a website at the day-level, he/she could simply augment the data with the current date and timestamp, and use this information later for matching.

__Which lists could serve as potential seeds?__

After having inventorized which entities are available, think about *which entities* serve as an entry point for your data collection. These "entry points" are commonly referred to as "seeds".

Suppose you are interested in gathering data from a social network on users, and that network has millions of users. How could you obtain a sample from that network? Maybe there is an internal page displaying the service's most recently active users, from which you can draw a sample. For example, Datta et al. (2018) visited the service's "recently active users" page for a duration of 1 months, collecting thousands of user names, from which a final sample of 5,000 users was drawn that entered the actual data collection.

Other studies use "external" lists, such as the New York Times book best seller lists, to link to data sets.

Yet others use a website's search function to search for potential seeds. Like with Google Trends, specific brand keywords can be entered, which then serve as linking points.

## Time Coverage

*Check for what time period the data is available on the site or API. Some sources only display data in real-time, while others have historical data available. In the case of historical data, how long can you go back in time?*

__For what time period is data available?__

What time period does your website or API cover? Some websites, such as Amazon.com, list historical data on reviews. That means you can easily go back in time and download all of these reviews. Other sections of the website, though, only display information in realtime (such as product prices), which means that if you don't capture the data today, you probably never will be able to capture that data.

{{< hint info >}}
__Be aware of "false friends"__

Even if a website makes available historical data, that does *not* mean *all* of the data is historically available. For example, Amazon.com reports the current review valence (the average of all customer reviews) and current price on their product pages. Yet, that data changes over time. While you can re-construct review valence from historical review data, you won't be able to re-construct pricing data (at least not entirely on Amazon.com).

{{< /hint >}}


__How is time encoded, and how accurate is it?__

In the case of historical data, detailed timestamps may be available. How are they encoded? Are they given in a users' time zone, or in [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time)? Do you need to convert the time to a common format for storage?

Also assess how accurate timestamps are. Some providers, for example, "aggregate" timestamps in descriptions like "more than a year ago", which may impact the usefulness of such data for building a panel data set, warranting a real-time data collection.

{{< hint info >}}
__Verify timestamps__

Verify whether you can trust the timestamps recorded in the data. For example, social media tracker Chartmetric.com records historical playlist performance data. In the Spotify playlist data retrieved via their API, most of the music tracks have supposedly been added to playlists some time in January, 2016. However, that does *not* mean it actually took place like this. In fact, the addition dates in January 2016 merely reflect the starting point of Chartmetric's data collection. So a bit of industry knowledge and background checks are absolutely required!
{{< /hint>}}

__Can data be modified after it has been published?__

What looks like archival data does not need to be strictly archival. For example, some e-commerce websites allow users to *change* their review after it was posted (check out [the blog post by Yelp](https://www.yelp-support.com/article/How-do-I-edit-one-of-my-reviews?l=en_US)). Do you find any traces of such events on the page? Sometimes, reviews or comments are also deleted, and this can only be detected when comparing reviews or comments over time. Other websites explicitly report when data has been deleted or reset, such as the social music network Last.fm (in their API, they set the `bootstrap` flag to 1 in the case users have reset their profiles, which may render their historical data incomplete).


{{< hint info >}}
__Recognize research opportunities__

The fact that reviews are deleted without posting a notice may sound like bad news. However, it creates amazing research opportunities. For example, if you were to scrape such a page multiple times, you could compare which reviews have been deleted, and label those as fake reviews. [Check out how identifying fake reviews has led to published work recently](https://www.nytimes.com/2020/11/19/technology/fake-reviews-amazon.html).

{{< /hint>}}

__How often is the site/endpoint refreshed?__

When you plan to scrape data in real-time from a website, try to get a feeling for how often the site is actually refreshed. This may help you to make a decision on how often you need to collect data from the site.


## Algorithmic transparency

*Think about why the site or API displays certain content and hides others. In other words, are there any algorithms in place that could potentially distort your data collection?*

A website or API can actively choose which data to show, and which data to hide/not show/make inaccessible.

__Which mechanisms affect the display of data?__

Design choices and algorithms that make a site easily navigable (which we love as users) can cause problems in collecting and using data for scientific purposes (which we dislike, for obvious reasons). Suppose you want to calculate average prices in a product category, and you start scraping data from the category pages of Amazon.com. Chance is you'll end up scraping prices for only the *most popular products* - which certainly are not representative of the whole product assortment on the platform.

Typical mechanisms that affect the display and retrieval of data are:
- sorting algorithms: e.g., by popularity, or relevance (though it's not clear what relevance really means)
- recommendation algorithms: e.g., users (i.e., your scraper) that have viewed product X also have viewed product Y; "customers interested in X also viewed Y"
- experimental conditions: e.g., you may end up being in an experimental treatment group of a firm
- sampling: e.g., the free Twitter API only returns a random subset of Tweets, and sample size can vary over time - such data is invalid for computing total tweet volume. Instead, commercial access from the entire Twitter database may be warranted.

{{< hint info>}}

Make sure to understand and gather information on how *metrics have been calculated*. For example, Chartmetric.com reports the *listeners* of playlists, while this data is not even available on Spotify. Looking at their blog, though, one can understand that *listeners* have been proxied. This is important to note when working on a paper!
{{</hint>}}


__Can the researcher exert control over the data display?__

When screening a site for data availability, it's crucial to look out for options to exert *control* about which data is shown. For example, you can sort products alphabetically, which - arguably - isn't related to popularity, and may hence be a better sampling scheme if you're interested in random samples.

On some websites or APIs, the researcher can make active decisions on how data is shown. For example, the documentation of a service's API may offer the option to sort data in alphabetical order, rather than by popularity. Other display options may be beyond the control of researchers (e.g., a personalization algorithm for pages visited). Some services allow users to specify whether they wish to be included in experiments conducted by the firm. It's recommendable to opt out of experiments when collecting data for research purposes (unless, of course, it's exactly these experimental conditions you're trying to study!).

{{< hint info>}}

When working with an API, carefully compare the output of the API with what is shown on the service's website. That way, you can detect any remaining errors or inaccuracies in your data.

{{< /hint >}}

{{< button relref="/opportunities.md" >}}Previous{{< /button >}}
{{< button relref="/researchfit.md" >}}Next{{< /button >}}
