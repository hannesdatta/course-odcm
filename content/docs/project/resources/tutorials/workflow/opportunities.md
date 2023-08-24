---
bookFlatSection: true
title: "Opportunity Identification"
description:
bookHidden: false
weight: 2
description: "Learn when using web scraping or APIs pays off to increase the relevance and rigor of your research."
---


# Opportunity Identification

## For Academics

How to identify an opportunity for scraping data? Working on a research question and recognizing the need to collect data from the web is a straightforward way to get started. Sometimes, though, a mere feeling that a particular data context is interesting may already be good enough to warrant an investigation - even long before the research question has been formalized.

{{< hint info >}}
__How attending a party in Hamburg led to a [publication on music streaming](https://tiu.nu/spotify)__

For example, long before online music streaming was the default, I met a friend's friend at a house party, who told me about this fantastic app called Spotify, which had just launched in The Netherlands at the time. I was amazed by the amount of new music I discovered when using the app. I also noticed my music taste was slowly gravitating from rock music to electronic dance, and - as a researcher - I wondered why? So, I decided to look for data on users' digital music consumption.

After browsing the web for a while, I found this amazing social network for music. It's been around for ages, long before Spotify came into existence. That website provided an API that allowed me to extract users' consumption histories. [Check out the website](https://last.fm) and its [API](https://last.fm/api)!

{{< /hint >}}

Rather than a mere gut feeling, researchers may also have specific goals on their mind to improve the relevance or rigor of their research. For example, including data collected from the web in one's study allows researchers to __observe behavior that occurred in the real world__. Such behavioral data may complement experimental data generated (e.g., such as generated in labs or via online surveys), and hence improve the external validity of their research. Also, data collected via web scraping or APIs allows researchers to __increase the timeliness of their work__. Researchers that use data collected via web scraping or APIs can capture information that otherwise has not been structured or observed yet by commercial data suppliers.

## For Business

Web scraping is a technique that was initially invented for large-scale retrieval of data for business purposes. The business model of search engines, for example, relies on *data collected via web scraping* - namely data on what's on the internet. Web scrapers that index the web are referred to as "bots", "web crawlers" or "web spiders", and they automatically "roam around" on the internet (e.g., by visiting new links as they encounter them), and store information on the content of websites in a database.

Today, the business model of many firms hinges on web scraping. For example, businesses monitor prices and share those with firms (see, e.g., the Dutch firm [InPrijsVerhoogd](https://www.ipvdata.com/en/)) and consumers (see, e.g., [Skyscanner](https://skyscanner.com)), or gather data on the social media performance of influencers or music artists (see, e.g., [SocialBlade](https://socialblade.com), [Chartmetric](https://chartmetric.com)).

With the emergence of social networks, the need for exchanging data in a more structured way grew. Services like Twitter and Facebook popularized so-called Application Protocol Interfaces (APIs), which essentially are websites meant for *computers* - and not for humans - to read. The footprint of rendering API outputs, which mostly boils down to plain text only, is more efficient that rendering a full-fledged websites. APIs quickly have become the default way to exchange data among trusted partners or the public. For example, the API of financial service provider [Stripe](https://stripe.com) allows developers to add payment functionality to their services. Similarly, the API of [Facebook](https://developers.facebook.com) enables businesses to develop add-on applications for the platform, such as games.

{{< hint info >}}
__Recognizing opportunities from *posting* data__

Web scraping and APIs can be used not only for retrieving data, but also for *posting data* to the web. For example, firms have employed scraping to transfer data from old systems to new databases. In essence, that entails the firm scraping their own data, and making it more usable. Researchers, for example, could use web scrapers to programatically interact with participants in their study.

{{< /hint >}}


{{< hint info >}}

__[Web scraping ideas for businesses](https://www.youtube.com/watch?v=qljvs_ttgl0)__

<iframe width="560" height="315" src="https://www.youtube.com/embed/qljvs_ttgl0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

{{< /hint >}}


Whatever the reason is for you to get started with scraping, we advise you to make a list of potential websites and APIs that may be relevant. In the next step of this tutorial, you will learn how to characterize the type of data that's available via a website or API. That's a crucial ingredient to judging whether the data will match your research purpose, and whether you should go ahead scraping it.


{{< button relref="/overview.md" >}}Previous{{< /button >}}
{{< button relref="/dataassessment.md" >}}Next{{< /button >}}


<!--
- for doing academic research
- for developing new business ideas and conducting marketing research [*video*](https://www.youtube.com/watch?v=2XfA0e4Bzkk)

-->
