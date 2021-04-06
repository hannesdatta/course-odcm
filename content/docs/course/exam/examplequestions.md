---
title: "Example questions"
bookFlatSection: true
bookHidden: false
weight: 5
draft: false
---

# Example questions

Questions will be asked along five topic areas (e.g., "web scraping 101"), and six question types (e.g., "application") (for details, see [here](../exam#content)). Below, you can find a few example questions. Example questions will be discussed with students in the final live stream of this course.


## 1. Python Bootcamp

*Question type: Application*

Write a function `url_detector()` that loads a list of URLs from the file [`urls.txt`](https://github.com/hannesdatta/course-odcm/blob/master/content/docs/course/exam/urls.txt), and filters that list for valid URLs, starting with `https` and containing a link to a product ID. Although you could rely on [regular expressions](https://tilburgsciencehub.com/building-blocks/develop-your-coding-skills/learn-to-code/learn-regular-expressions/) to get the job done, other simpler workarounds exist. How many URLs do you end up with?


## 2. Web Scraping  

*Question type: Synthesis*

Scrape the top 1000 lifetime grossing movies (domestic) from [Box Office Mojo](https://www.boxofficemojo.com/chart/top_lifetime_gross/?area=XWW). Filter down on movies released since 2000 and export the rank, title, and lifetime gross of these movies to a CSV file.


## 3. APIs

*Question type: Application*

As a researcher you're interested in polarity in online communities and therefore collect data on the distribution of up and down votes on Reddit. Extract a random sample of at least 100 Reddit posts from the [`politics`](https://www.reddit.com/r/politics) and [`science`](https://www.reddit.com/r/science) communities and compare the upvote ratio. Comment on your findings.

## 4. Workflow

*Question type: Evaluation*

Review the following text in which a master student describes the institutional background of the data collection. The thesis centers around the effect of hiding like counts on user behavior and thus proposes a methodology for sample construction. Describe how you would define the treatment and control group, and how you would go about collecting data on a user-level. Keep in mind ethical and legal concerns of collecting and storing data.

*Late April 2019 Instagram announced that it would run an experiment among Canadian users in which the like counts were hidden (Constine 2019). Three months later, around mid-July, they expanded the treatment to users in various other countries including Australia, Canada, and Italy. Users located in these countries could not see the number of likes on media posted by others, whereas users living anywhere else could still view like counts (Loren 2020). Thus, treatment groups enter the treated pool of persons sequentially, and assignment to the treatment or control condition was dependent on users’ geography.*

{{< hint info >}}
**Solutions**  
The solutions of these example questions can be found [here](https://github.com/hannesdatta/course-odcm/blob/master/content/docs/course/exam/example_questions_solutions.ipynb). Keep in mind that there are often multiple ways to get to the same answer.
{{< /hint >}}


