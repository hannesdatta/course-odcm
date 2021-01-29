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

# About myself

## Background

- born and raised in Germany
- moved to NL 12 years ago
- married, 2 kids (2 and 5 years old)
- streaming from 'de zolderkamer' in 's-Hertogenbosch
- geek at heart (got a 3D printer for Christmas), love listening & playing music, start new hobbies every few months...
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
    - causality in observational data

## Teaching activities

- MSc Marketing Analytics and Management
    - Research in Social Media (*legacy*)
    - Data preparation and workflow management (*new*)
    - Online data collection and management (*new*)

::: notes

* prototyped some content with managers, but now... release to students
* talk about how dPrep and oDCM differ (and how students may benefit from taking both courses). Why R and Python (rather than just one of them)?


:::

## Current research interest

__Impact of digitization on consumers, producers__

- How did [online streaming](https://tiu.nu/spotify) (Spotify, Netflix) change behavior?
- Bunch of follow-ups
    - "Who runs Spotify?" (measuring power of platforms)
    - [Music "filter" bubbles](https://research.tilburguniversity.edu/en/publications/streaming-services-and-the-homogenization-of-music-consumption)
    - Covid-19 & music consumption
    - Platform incentives & production of music
- More: see [website](https://hannesdatta.com)


# About you

## Getting to know you

> - Where are you located? (city, country)
> - Why are you interested in Marketing *Analytics*?
> - Where do you see yourself in a few years from now (professionally)?
> - What's your experience with R?
> - How much are you willing to invest in this course?

<!--(map of NL & Europe - use Zoom annotation!)
-->

::: notes

Consider using polling software for these questions (to increase response rate)

- What stage are you in?
- What are you working on right now?
- What's your ambition with your study program?

## Covid-19
- Where are you at right now?
- Home office, on a scale from 1 to 10...?
- Wanna have
-    the last half-an-hour of this with a borrel? ;)

:::

# Motivation for course

## Disclaimer

> - Course runs for the first time (buggy!)
- Course is public, live streams are not
- Streams are complements, not substitutes for working through self-study material
- Mix of students at various levels
- Consider me your coach, not your professor
- Slow me down
- Know the course website inside-out
- I'm a marketer, not a data or computer scientist

::: notes


- I'm a marketer
    - I do marketing analytics
    - It’s close to data science in terms of data acquisition, but...
    - rather distant in terms of methods (e.g., ML methods only enter the field gradually; we’re mostly applied econometricians)

- In the (spontaneous) exercises, I may not know all the answers all the time – but will deliver later if required

:::

## Mr. Spotify


::: notes

- The story about the legal issues you faced (prior to switching to Chartmetric)
- Show example of Chartmetric API output (a website with lots of text)
- Unfortunately, not every websites provides an API

:::


## Opportunities for Web Scraping

::: notes
  - In principle, everything you see can be obtained
  - Simple demo where you go to a website, open Google Inspector, and make a few changes

:::


# This course

## Course objectives

- Identify online data sources and evaluate their value in the context of a specific research question or business problem
- Assess the terms and conditions for collecting, storing, and sharing data
- Collect data via web scraping and Application Protocol Interfaces (APIs) by mixing, extending and repurposing code snippets
- Transform semi-structured JSON data to structured data sets for statistical analysis (“parsing”)
- Store and manage data using file-based systems
- Draft, execute, monitor and audit online data collections locally and remotely
- Document and archive collected data, and make it available for public (re)use

## Modules
1. Research and business opportunities
2. Data availability and research fit
3. Skill-building
4. Data extraction plan
5. Skill-building
6. Data collection & packaging
7. Project
8. Course summary


::: notes



:::

## Tutorials

- Software Installation & Python Bootcamp
- Webdata for dummies
- Web scraping 101 & APIs 101 (both)
- Web scraping Advanced & APIs Advanced (one of both)

::: notes
choice for web scraping & apis depends on group project

structure:
* Importance
* Let's try it out!
* Exercises
* Wrap-up
*
:::


## Canvas versus the web

- Canvas is only used for
  - posting important announcements,
  - sign up for teams,
  - submitting data challenges/projects, and
  - discussion board.

- The course website shows the syllabus and grading details

## Live streams

- use the public chat (tell me if I don't see it! who can take that role?)
- maybe share screen (install [TeamViewer](http://tilburgsciencehub.com/setup/teamviewer))
- if you have, use two screens (one to program, one to view slides/others)


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
  - "proof of investment in skills" (submitted tutorials/data challenges)
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
* What do you mean with "Share individual progress and learnings "
* Both multiple choice and open questions (you can't pass this course if you don't learn programming -> make sure you actively participate in the team project so that you can replicate it individually)

:::


## My commitment

- Get up to speed with both web scraping and APIs (and know when to pick which one!)
- Learn Python, __but__, becoming an expert requires years of practice
- Discuss own work and ideas
- __But__: requires interaction, talking to me, working hard


::: notes

- Other's efficiency
    - Not recollect what has been collected
    - Not reprogram what has been programmed
    - Learn from one's code, etc.
    - Share ideas
- Light-weight structure: no commercial tools, readily implementable, do not need admin rights [...]

:::

## Comments on coding

- Coding can be extremely frustrating if you're starting out
- You will learn from your mistakes
- Take breaks! Stop coding. Go for a run. Start again.
- Use cheat sheets. See course site.
- [Support section](https://odcm.hannesdatta.com/docs/course/support/)


::: notes

Mention how we aim to remedy this initial hurdle? (quick feedback loops especially in the first few weeks)

:::


## Help

Make computer throws an error. What now?
1. Google
2. Ask a friend/classmate
3. Google
4. Ask a friend/classmate
5. Ask course instructor


::: notes

* Google/Stackoverflow are your best friends
* Live demonstration of how to search on Google and Stackoverflow
* Comment on experiment with live coding sessions (start a call - talk to fellow classmates who're facing the same struggles)



:::

## What's in for you?

- Essential job market skills
  - get the jargon, know your tools
  - marketing is much more than blabla - high-tech!

- Essential to show expertise
  - potential for follow-ups here in Tilburg and beyond

- Exiting area
  - new business models
  - new methods
  - new technologies

## Success factors

Please tell me __what would make this course a success__ for you

::: notes

(for me): become more efficient, use Tilburg Science Hub, give me feedback

:::

## Being in touch

- WhatsApp
  - Please use WhatsApp for short questions: +31 13 466 8938
  - Submit your name and telephone number on Canvas (so I can create contacts on my phone and know whom I'm talking to)
- More info on the support section of the course website


## Getting started

- Install Python/Anaconda an do the Python Bootcamp
- Web data retrieval for dummies (tutorial)

- Any questions?! If not -- I'll see you in the live stream on Friday! (--> course schedule).

- Installation issues: stay on Zoom.

::: notes

* can use the break for installation problems
* show on the website where they can find the information they need
* how to download the files (right click)
* manage expectations: DataCamp courses are simplistic (copy-paste etc.) and should not take too long, the data challenges are more challenging and will likely take more time, and are more representative of the level we expect in this course.

:::

## Any questions?


# Wrap-up

## Summary

What are __your__ takeaways?

## Met the objective?

Apply web scraping and API parsing strategies to collect data from a variety of online sources

## Your feedback

- About this course
    - About me
    - The format of this course
    - Communication
- About Tilburg Science Hub
    - About the text mining tutorial
    - About the installation instructions
    - About the overall workflows
- ...anything else


## Next session

Friday, 5 February, 2021 (08:45 - 10:30)
Prepare a list of research and business ideas (in the realm of web scraping and APIs)


::: notes

See Opportunity identification section on the website

:::


## Contact

Hannes Datta

https://hannesdatta.com
