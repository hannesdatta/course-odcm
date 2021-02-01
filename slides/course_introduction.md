% Online Data Collection and Management
% [Hannes Datta](https://hannesdatta.com)
% February 2, 2021

# Live stream #1

## Hi there!

Please turn on your camera :)

If you haven't done so, navigate to the course page at [odcm.hannesdatta.com](https://odcm.hannesdatta.com)


::: notes

- drafted this course for a long time
- finally got the chance to teaching it now

- While you can find tons of resources online on how to scrape, or how to access data from APIs, none of these tutorials will actually teach you how the way you scrape affects your research. This is the void we will.

- happy to share that vision

:::

## Agenda

(before we *really* start)

- About myself
- (More elaborate) motivation for the course
- Course framework and learning goals
- Agenda and practical arrangements

## Disclaimer

> - Slow me down & use the chat
- Streams are complements, not substitutes for self-study & course website
- Minimal use of slides; will post
- Course runs for the first time (buggy!)
- Mix of students at various levels; public (but streams are not)
- I'm a marketer, not a data or computer scientist
- Consider me your coach, not your *distant professor*

# About myself

## Background

- born and raised in Germany
- moved to NL 12 years ago
- married, 2 kids (2 and 5 years old)
- streaming from 'de zolderkamer' in 's-Hertogenbosch
- geek at heart (got a 3D printer for Christmas), love listening & playing music, starting new hobbies every few months...
- now Associate Prof at Tilburg University

<!--
## Professional background

- PhD, quantitative marketing (Maastricht University)
- Associate professor Tilburg University
- Visiting professor
    - Duke University (Sept - Nov 2018)
    - University of New South Wales, Sydney (Jan 2020)
-->

## Key areas of expertise

- Substantive
    - subscription-based business models
    - marketing-mix modeling and optimization
    - branding

- Method
    - data management of structured and unstructured data
    - online data collection via APIs and web scraping
    - causal effects with observational data

## Teaching activities

- MSc Marketing Analytics and Management
    - Data preparation and workflow management (*new*, dprep.hannesdatta.com)
    - Online data collection and management (*new*, odcm.hannesdatta.com)
    - MSc Thesis supervision (thesis.hannesdatta.com)
    - Research in Social Media (*legacy*)
- Tilburg Science Hub (http://tilburgsciencehub.com)

::: notes

* prototyped some content with managers, but now... release to students
* talk about how dPrep and oDCM differ (and how students may benefit from taking both courses). Why R and Python (rather than just one of them)?


:::
<!--
## Current research interest

__Impact of digitization on consumers, producers__

- How did [online streaming](https://tiu.nu/spotify) (Spotify, Netflix) change behavior?
- Bunch of follow-ups
    - "Who runs Spotify?" (measuring power of platforms)
    - [Music "filter" bubbles](https://research.tilburguniversity.edu/en/publications/streaming-services-and-the-homogenization-of-music-consumption)
    - Covid-19 & music consumption
    - Platform incentives & production of music
- More: see [website](https://hannesdatta.com)

-->

# About you

## Getting to know you

<!--
> - Where are you located? (city, country)
> - Why are you interested in Marketing *Analytics*?
> - Where do you see yourself in a few years from now (professionally)?
> - What's your experience with R?
> - How much are you willing to invest in this course?

<!--(map of NL & Europe - use Zoom annotation!)
-->

::: notes

Consider using polling software for these questions (to increase response rate)

- Who's taking only this course (and not dprep)
- What stage are you in?
- What are you working on right now?
- What's your ambition with your study program?

## Covid-19
- Where are you at right now?
- How much do you like your home office, on a scale from 1 to 10...?
- How lonely are you?
- Wanna have the last half-an-hour of this with a borrel (eventually) - we can plan it? ;)

:::

# Motivation for course

## Mr. Spotify

- started out as a PhD student without data
- was interested in music, and found website with data (https://last.fm)
- no best practices in scraping; learnt all by myself and made many mistakes
- scraping undervalued in academic job market, __but__, key role in shaping relevance and rigor of your work


::: notes

- The story about the legal issues you faced (prior to switching to Chartmetric)

- Show example of Chartmetric API output (a website with lots of text)

- Unfortunately, not every websites provides an API

:::

## Bol.com - scraping

A demo of a simple __web scraper__ on Bol.com


::: notes
  - In principle, everything you see can be obtained
  - Simple demo where you go to a website, open Google Inspector, and make a few changes

:::

## Getting inspired...

What are cool websites/services you always wanted to get data from?

What for?


## Chartmetric.com - APIs

A demo of a simple __API__

## Opportunities from web scraping

- Increase relevance
  - e.g., be more timely, address a wider set of stakeholders (e.g., firms, markets, consumers, products, brands)

- Increase rigor
  - e.g., from cross-sectional studies to longitudinal studies
  - e.g., meet more rigorous identification requirements, think about biases


# This course

## Course objectives (I)

- Identify online data sources and evaluate their value in the context of a specific research question or business problem
- Assess the terms and conditions for collecting, storing, and sharing data
- Collect data via web scraping and Application Protocol Interfaces (APIs) by mixing, extending and repurposing code snippets

## Course objectives (II)

- Transform semi-structured JSON data to structured data sets for statistical analysis (“parsing”)
- Store and manage data using file-based systems
- Draft, execute, monitor and audit online data collections locally and remotely
- Document and archive collected data, and make it available for public (re)use

## Course structure

- Weekly modules, structured along the *workflow for online data collections*
  - Self-study
  - Tutorial
  - Live stream for feedback & immersive activities

- Project in which you put into practice your skills from the weekly modules

## Workflow for collecting online data

1. Opportunity Identification
2. Data Availability Assessment
3. Evaluation of Research Fit and Resource Use
4. Technical Extraction Plan and Prototyping
5. Evaluating legal and ethical concerns
6. Collecting and monitoring
7. Preprocessing and Documentation
8. Using, Distributing and Maintaining

## Tutorials

- Themes
  - Software Installation & Python Bootcamp
  - Webdata for dummies
  - Web scraping 101 & APIs 101 (both)
  - Web scraping & APIs Advanced (one of both)
  - Documentation and Packaging

- Structure: Importance, Let's try it out, Exercises, Wrap-up

::: notes
choice for web scraping & apis depends on group project

:::

## Course positioning

<img width="1000" alt="Course framework" src="odcm_positioning.png">

## Course website

odcm.hannesdatta.com

::: notes

- Will show you the course website now
* show on the website where they can find the information they need
* how to download the files (right click)

:::

## Canvas versus the web

- The course website is your #1 resource

- Canvas only used for
  - posting important announcements,
  - sign up for teams,
  - submitting data challenges/projects, and
  - discussion board.

::: notes

all students have Canvas access?

:::

## Live streams

- use the public chat
- use it like on Twitch or YT (massively); question to me: prefix with `???`
- help me as a moderator if I miss questions
- maybe share screen (install [TeamViewer](http://tilburgsciencehub.com/building-blocks/configure-your-computer/automation-and-workflows/teamviewer/))
- if you have, use two screens (one to code, one to view colleagues/slides)


## Python Bootcamp

From zero to hero

::: notes
- Python bootcamp notebook assumes that you have done the DataCamp courses first (it does NOT start from 0)
- emphasize importance of building up the foundations -> otherwise you'll likely struggle in the rest of the course
- really try to solve the exercises on your own before looking at the solutions
- If you're new to Python important to schedule time for this course (in week 1 also the Webdata for dummies tutorial kicks off)

- Demo: View preview of notebooks on Github (without having to download it first)
- Sometimes you may  need to refresh the page

:::

## Project

- specifics to be made available on the course website
- self- and peer assessment
  - written feedback to team members (tba)
  - assessment of own performance and that of team members


::: notes
- Emphasize that (contrary to dPrep) the group project already starts in week 1
- Also here there's a less strict path they need to follow - we have curated a list of marketing-related data sources (yet they're fully free to steer their project in another direction)


:::

## Grading

- Team project (50%)
- Share individual progress and learnings (10%)
- Computer exam (40%)

::: notes
* 50% team project = (40% + 10% individual assessment on the basis of self- and peer assessment)
* What do you mean with "Share individual progress and learnings"?
* Both multiple choice and open questions (you can't pass this course if you don't learn programming -> make sure you actively participate in the team project so that you can replicate it individually)

:::


## My commitment

- Get up to speed with both web scraping and APIs (and know when to pick which one!)
- Learn Python, __but__, becoming an expert requires years of practice
- Discuss own work and ideas, __but__ requires interaction, talking to me, working hard


::: notes

- Light-weight structure: no commercial tools, readily implementable, do not need admin rights [...]

:::

## Brain-dead by coding

- Coding can be extremely frustrating if you're starting out
- I tend to become semi-"brain-dead" after a day of coding
- Take breaks! Stop coding. Go for a run. Start again.
- You will learn from your mistakes
- Use cheat sheets and our support section.

&#8594; quick feedback loops in first few weeks

::: notes

Mention how we aim to remedy this initial hurdle? (quick feedback loops especially in the first few weeks)

:::

## Steps of escalation & getting in touch

When you run into trouble, this is your way out!

1. Ask Google and Stackoverflow
2. Ask friend/classmate (form groups!)
3. Can it wait? Defer to live streams.
4. If it can't wait: be in touch with me

::: notes

* Google/Stackoverflow are your best friends
* Live demonstration of how to search on Google and Stackoverflow
* Comment on experiment with live coding sessions (start a call - talk to fellow classmates who're facing the same struggles)


:::

## Use of WhatsApp

- Please use WhatsApp for short questions: +31 13 466 8938.
- Send me your names (first and last names) now (so I can create contacts on my phone and know whom I'm talking to)
- More info on the support section of the course website
- Email is not so optimal


## What's in for you?

- Essential skills for entrepreneurs
  - e.g., have your own company on the basis of web data and APIs
  - be the linking pin (interface between marketing and analytics)

- Investment in research skills
  - e.g., collect own data & shape its creation to create relevant and rigorous research

- Showcast expertise in coding


## Success factors

Please tell me __what would make this course a success__ for you

::: notes

(for me): become more efficient, use Tilburg Science Hub, give me feedback

:::

## Getting started

- Install Python/Anaconda and do the Python Bootcamp (all done?)

- This week
  - Tutorial for "web data retrieval for dummies"
  - First part of the "web scraping workflow" (overview & opportunities)

- Preparation for Friday

## Next session

Friday, 5 February, 2021 (08:45 - 10:30)
Prepare a list of research and business ideas (in the realm of web scraping and APIs)

::: notes

See Opportunity identification section on the website

:::


## Any questions?

Stick around now if you have questions.

(e.g., installation issues, prep week)

::: notes

* can use the break for installation problems
* show on the website where they can find the information they need
* how to download the files (right click)
* manage expectations: DataCamp courses are simplistic (copy-paste etc.) and should not take too long, the data challenges are more challenging and will likely take more time, and are more representative of the level we expect in this course.

:::

## Contact

Thanks a lot, and have fun with the course!

Hannes Datta

https://hannesdatta.com
