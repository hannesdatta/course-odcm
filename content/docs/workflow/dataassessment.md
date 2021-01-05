---
bookFlatSection: true
title: "Data Availability Assessment"
description:
bookHidden: false
weight: 10
description: " "
---

# Workflow for collecting online data

##  Data Availability Assessment

Let's say you've narrowed down your search to just a few websites or APIs. A common mistake done by many is to directly go ahead and scraping that data without actually thinking through *which* particular data is available on the site or API, and whether that data actually fits your research idea. However, a critical assessment of data availability may surface additional, more suitable data, or offer the opportunity to address multiple stakeholders of a particular business setting. Also, a more rigorous analysis may show problems with actual research - e.g., if algorithms are detected that may invalidate the author's supposed identification strategy.

Therefore, we recommend you to first take stock about the *actual* data that's available, on each site or API that may be relevant. After that, you critically assess whether the data fits your research purpose.

### Entity coverage and Linkages

*What entities are actually available? A typical e-commerce website, for example, not only displays information on products and their reviews, but also allows you to extract information on the sellers of products and the users that have written the reviews. Check out how these entities could potentially be linked to one another or even to a dataset you're already working on.*

__Which entities are available?__

Familiarize yourself with the structure of the website or API to understand for which entities (e.g., consumers, products, reviews) are available. Consider a typical e-commerce website like Amazon.com. Entities, are the products and product reviews. But did you know that Amazon.com also lists information on the particular *users* that are reviewing products (such as where they're from), or information on third-party sellers (such as the shipping fees they charge)? Look for entities, write them down, and think carefully about how you could use these various entities to incorporate in your study. Much of the best publications I've seen use data that is *not* obviously available on the site, but data that's somewhere hidden, where you have to think twice about its potential existence, but when you do incorporate it, it can boost your relevance for practitioners tremendously.

__How many entities are available?__

Knowing entities exist (e.g., reviews) doesn't mean you can all retrieve them! So zoom in on how many entities are actually accessible for you. For example, via the product page of Amazon.com, you can only view at maximum 1,000 entries, or at max. xxx review pages.

__How are entities identified?__

When building code to extract data, you need to tell a browser where to look for that data. Typically, this happens via some kind of URL/endpoint, appended with an identification number for a particular entity. For example, Amazon.com uses ASINs (UPCs) to point to a product page (e.g., XXXX), and the same ID is used to also point to the review pages (xxxx.). In other circumstances, IDs are merely numerics that don't mean much (e.g., such as is the case for Chartmetric's internal artist ID numbers); other sources may use commonly accepted metrics (e.g., such as Spotify's Track ID or Album ID, that is more widely accepted and used by others).

__How are entities linked to one another?__

Another crucial assessment to make is how entities are linked to one another, if at all. For example, the product pages at Amazon.com (e.g., ) list products together with their ID number, from which you can then visit product pages. This is an example of a consistent linking scheme that can be readily scraped. Other sections of the website or other services may not provide such linkages. For example [...do we have an example of stuff that's NOT linked?]

__How can entities be linked to external entities?__

After assessing the internal linkage structure, critically reflect how entities may potentially be linked to external data sources. For example, websites may list existing identifiers (e.g., in an ecommerce setting, Amazon.com lists book ISBNs, next to their own ASINs). Music intelligence provider Echonest.com, in its early days, allowed users to query their API for so-called Musicbrainz IDs, which were at the time widely used by "the wikipedia of the music industry", musicbrainz.org. This allowed the service to grow and be usuable (as mbids were used widely), and offered opportunities for reserachers to gather meta data for existing data sets.

Linkages need not to be explicitly present on the site. Suppose a researcher was interested in merely gathering day-level data, he/she could simply write the current date/time in their scraping code, and use that as a matching thing.

Finally, linkages could be established by some form of string-based matching. Exact matching - e.g., in the case of brand names, approximate, or fuzzy matching schemes, like done in Datta et al. (2018). [...]

__Which lists could serve as potential seeds?__

Suppose you are interested in gathering data from a social network on users, and that network has millions of users. How could you obtain a sample from that network? You need to start with a seed. Where are these seeds located? Maybe there is an internal page using most recent active users (Datta et al. 2018), from which a sample was taken for a duration of 1 month, encompassing x thousands user names, from which itself was a sample was drawn.

Other studies use "external" lists, such as NYT book best seller lists, to link to data sets.

Yet others use a website's search function to search for potential seeds. Like with Google Trends, specific brand keywords can be entered, which then serve as linking points.

### Time Coverage

*Next, check for what time the data is available on the site or API. Some sources only display data in real-time, while others have historical data available. How long can you go back in time?*

__For what time period is data available?__

What time period does your website or API cover? Some websites, such as Amazon.com, list historical data on reviews. That means you can easily go back in time and download all of these reviews. Other sections of the website, though, only display information in realtime (such as product prices), which means that if you don't capture the data today, you probably never will be able to capture that data. o	“False friends”: what looks like archival (e.g., review valence) is actually a snapshot (either back-engineer metric, or use live data collection instead)

Even if you think data is historically available, you may be fooled easily: for example, social media tracker Chartmetric.com records historical playlist data, but - surprisingly - most of the tracks where added on the 1st of January, 2016. That does not mean it actually took place, but it's merely an outcome of the company starting *their* data collection sometime in 2016.

__How is time encoded?__

In the case of historical data, sometimes detailed timestamps are available. How are they encoded? Are they given in a users' time zone (so if you gather from multiple locations, you have to correct it), or are they encoded in some kind of universal format (universal standard time). Yet others provided very aggregate timestamps, such as "more than a year ago", which may impact the usefulness for building panel data and warrant a "live" data collection.

__Can posted data be modified?__

What looks like archival does not need to be strictly archival (e.g., changing input data; can users modify data after it has been submitted?); a live data collection may be able to track that. Can you observe whether such data was modified? (e.g., Last.fm API reports the bootstrap value, which means users have reset their listening count sometime).

__How often is the site/endpoint refreshed?__

For live data: how often does the page get updated? Is information actually available in realtime?

### Algorithmic transparency

*Think about why the site or API displays certain content and hides others. In other words, are there any algorithms in place that could potentially distort your data collection?*

A website or API can actively choose which data to show, and which data to hide/not show/make inaccessible.

__Which mechanisms / algorithms / design choices affect the display of data?__

Which mechanisms affect which data is displayed on the site, and which not?

Design choices: only top x products, likely to be constant.

Algorithms affecting everyone: e.g., popularity, relevance

Algorithms affecting individuals: personalized recommendations


Algorithms that make a site easily navigable (which we love as users) can easily cause distractions in our data collections (which we hate as researchers). Let me give you an example. Suppose you want to calculate average prices in a product category, and you start scraping data from the category pages of Amazon.com. Chance is you'll end up scraping prices for only the most popular products - which certainly are not representative of the whole product assortment on the platform.

Typical ones are sorting algorithms, such as in descending order of popularity, or relevance. Also, recommendation algorithms (users that have viewed X also have viewed), people interested in X also looked for.

__Can the researcher exert control over the data display?__

When screening a site for data availability, it's therefor crucial to look out for options to exert *control* about which data is show. For example, you can sort products also by alphabet, which - arguably - probably isn't related to popularity, and would be a safer selection filter when you're interested in the price of an average product, rather than of the most popular products.

For some, the reseracher can make active decisions (e.g., sort in alphabetical order, rather than by popularity). Others are beyond the control of researchers (e.g., a personalization algorithm for th epages visited) - which could be circumvented by resetting cookies at every browser initiation. Yet, others are completely beyond the control fo a researcher, such as in which experimental condition one is.



In terms of research fit,
And are you able to turn them off? For example, many ecommerce websites display products in descending order of their popularity: best selling on top, worst selling on the bottom. You have control about that display order many times, so it's good to note that down and remember when judging whether the data is good enough for a study. Sometimes you don't have control at all, so check the site's or API's documentation on any details how the data actually gets on the site.
