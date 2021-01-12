---
bookFlatSection: true
title: "Workflow - Other"
bookHidden: false
weight: 40
description: " "
draft: true
---


### Other text snippets




{{< mermaid class="text-left">}}

graph TD
    A[Opportunity Identification] --> B
    B[Data Availability Assessment] --> C
    C[Evaluation of Research Fit] --> D
    D[Data Extraction Plan] --> E
    E[Collection and Monitoring] --> F
    F[Preprocess and Document] --> G
    G[Update and Maintain] --> H
    H[Use]

{{< /mermaid>}}

- Choose a software toolkit for data extraction. If you're using an API, does this API have a package available in Python you could use? Or is it more advisable to self-program an interface?
- For websites, can you read the website's content without actually seeing them (e.g., via BeautifulSoup), or do you need to open a browser and "simulate" user behavior, such as clicking? Or - are there commercial packages available you could use?

- Second, on what infrastructure will you run the scraper? Your local PC may be cheap (you already own it), but how do you get that done, given you will have to restart your computer once in a while or put it in your bag while traveling? A remote system, such as on a computer in the cloud, maybe more durable.

- Third, how do you build monitoring functionality in your code to inform you about what's wrong? For example, with a live data collection, can you put systems in a place that tell you about your data collection's health?





###

For example, long before online music streaming was the default, I met a friend's friend at a house party, who told me about this fantastic app called Spotify, which had just launched in The Netherlands at the time. I was amazed by the amount of new music I discovered when using the app. I also noticed my music taste was slowly gravitating from rock music to electronic dance, and - as a researcher - I wondered why? So, I decided to look for data that tracks users' digital music consumption on the web, so that I could study that behavior later.s When browsing the web, I found that amazing social network for music - it's been around for ages, long before Spotify came into existence. That website provided an API which allowed me to extract users' consumption histories.

[...]

So we would like to formally introduce you to the workflwo of automated web data collection, in which we formalize many of the decisions that a researcher has to make. This process is not a fixed rule book you need to adhere to, whatever the role of web data in your project is, you are allowed to modify or even skip some of the parts that we highlight. However, this workflow should be considered a tool to help you increase relevance, improve rigor, and balance resource use while working on your study.

[...]


[...]


### Opportunity identification [academic]

[inspired from Johannes?]
Let me give you an example from my own experience. A few years ago, I scraped data from a social network for listening to music, think of this like an early version of Spotify. My scraper ran on my office computer, and extracted data from the profile pages of about 5,000 users of the site, every 15 minutes, for about 1.5 years. I once went on a short holiday while the scraper was running, and when I returned to my office, my computer was off. Turns out there was a power cut in the building over the weekend. I switched my computer back on, checked the files on the disk, and shockingly noticed that the power cut happened early Saturday morning. I returned back to office after a long weekend on a Wednesday - so I lost four days of valuable data - data that I can't recover because the site doesn't list users' historical profile pages. What's my lesson learnt here? Whenever I scrape, I also actively *monitor* my data collection and send a push message to my phone every day, informing me that the collection is still on. This helps me to prevent errors in collecting data - especially when it concerns data collections that take place over extended periods.
