---
bookFlatSection: true
title: "Course"
bookHidden: false
weight: 1
bookCollapseSection: true
---

# Course Syllabus

## Instructor

This course is instructed by [dr. Hannes Datta](https://hannesdatta.com), Associate Professor at the Marketing Department of Tilburg University. 

{{< hint info >}}
Join Hannes' professional network on [LinkedIn](https://www.linkedin.com/in/hannes-datta/), subscribe to his [YouTube Channel](https://youtube.com/c/hannesdatta), and start following him on [GitHub](https://github.com/hannesdatta) and [Twitter](https://twitter.com/hannesdatta) to stay up-to-date!
{{< /hint >}}

## Course description

### Learning goals

Web scraping and Application Programming Interfaces are among the must-have skills of marketing analysts and data scientists. The internet offers abundant possibilities to collect data used in empirical research projects and provide business value (e.g., social networks, digital media providers, price comparison websites, and online platforms). After successful completion of this course, students will be able to:

- Explain how to use web data for creating marketing insight[^1]
- Select web data sources and evaluate their value to inform a specific research context or business problem[^1]
- Design the web data collection while balancing validity, technical feasibility, and exposure to legal/ethical risks[^1]
- Collect data via web scraping and Application Programming Interfaces (APIs) by mixing, extending, and repurposing code snippets
- Document and archive collected data and make it available for public (re)use

The specification matrix for this course can be [downloaded here](specification_tables_odcm.pdf). This matrix gives an overview of all the learning goals and their weights in each graded component of the course (i.e., in the final exam, team project and Pulse). 

[^1]: Based on (1) Boegershausen, Johannes, Hannes Datta, Abhishek Borah, and Andrew T. Stephen (2022). “Fields of Gold: Scraping Web Data for Marketing Insights.” *Journal of Marketing*. [Download paper](https://doi.org/10.1177/00222429221100750) and [visit web companion](https://web-scraping.org), and (2) Guyt, Jonne, Hannes Datta, and Johannes Boegershausen (2024). "Unlocking the Potential of Web Scraping for Retailing Research." Working paper. [Download paper](jretailing_jan2024.pdf).

<!--
[^2]: Students use a web app to monitor their progress on the course's learning goals by "ticking off" items from a to-do list (e.g., "I have installed Python," "I have finished Tutorial X," etc.). The instructor can use the app to learn which topics to highlight during live streams. Students, in turn, can use the app to see how far others in the class have already proceeded, giving them direct feedback on their performance.
-->

### Positioning of the course in the study program

The course is instructed to MSc students in the Marketing Analytics (TiSEM) program. Seats are also offered to interested Research Master and PhD students. Learn more about enrollment [here](enroll).

Considering the typical process in which research is carried out, this course is positioned *at the beginning of a research project* (i.e., when the research question is being defined and the data being collected). This course does not zoom in on *how to analyze* data collected from the web but focuses on the process of collecting data for later use (e.g., for thesis or PhD projects). Therefore, students are recommended to follow this course before embarking on thesis projects.

To illustrate the wide range of applications of web data, the course introduces both national and international websites and APIs. For example, the Dutch analytics firm[InPrijsVerhoogd](https://inprijsverhoogd.nl) monitors prices across a wide range of retailers on a global scale. When collecting web data for their research, students mostly rely on a mix of both Dutch and international data sources, ranging from Dutch e-retailers (e.g., [Coolblue](https://coolblue.com), [Bol.com](https://bol.com), [Albert Heijn](https://ah.nl)) and marketplaces (e.g., [Autoscout](https://autoscout.nl)) to globally available platforms (e.g., [Reddit](https://reddit.com), [Twitch](https://twitch.com), [Kayak](https://kayak.com)).

## Prerequisites

- The course uses Python for the technical implementation of collecting web data. The course welcomes novices, of whom a significant investment of effort and time is required to learn the necessary skills.
- [Preparation material](../modules/prep) is available in the form of Jupyter Notebooks or course recommendations at Datacamp. Novices may further benefit from following other courses at Tilburg University in which Python is used, for example, *Research Skills: Data Processing* and *Research Skills: Data Processing Advanced*.
- Students are recommended to use their computer for this course. Windows and Mac users can typically install all required software easily. Linux users may require some advanced understanding of their operating system to install all required software. Android/Chromebook/iOS devices are not supported. Cloud services (e.g., Tilburg's Jupyter Notebook server) may not be fully supported (because you can usually not see what happens "outside" of Jupyter Notebook). 


## Teaching format

- Blended (a mix of online/offline lectures and tutorials, and online/offline coaching sessions)
- Combination of self-paced tutorials (e.g., using Jupyter Notebooks or pre-recorded clips), and interactive live streams for feedback and coaching <!--(recordings are shared with students)-->
- Learn state-of-the-art tools popular among scientists, marketing analysts, and data scientists (e.g., Python), and collect data from real websites and APIs
- Open education & open science (all material is open; publicly accessible course page that stays with you, even after the end of the course)

<!--, simulations, hackathon-->
<!-- work on VMs on AWS, code in SQL and R, compete on Kaggle, or work on own computer--; Coding Dojo student-=led analysis; while sharing screens-->

## Assessment

- [Team project](project) (50%, out of which 10% are based on students' individual contribution, measured by [self- and peer assessment](../project/grading/peerassessment))
- [Computer exam](/docs/exam) (50%)

<!--
[^3]: In particular, students regularly monitor their progress on the course's learning goals. __At least one evaluation per course week is required to obtain points on this component of the course grade.__
-->

### Passing requirements

Students pass this course if
- the final course grade (i.e., the weighted average of the following two components: (1) the group project, and (2) the exam; weights indicated above) is ≥ 5.5, and
- the exam grade is higher than or equal to 5.0 (≥ 5.0).

Final course grades are rounded to multiples of half points (e.g., 6, 6.5, 7, etc.).

### Resit policy

- If students have a grade lower than 5.0 on the exam, they cannot pass this course.
  - Required action: Students will have to take the [exam resit](/docs/exam).
- If students are not part of a team, they cannot obtain a grade for the team project and hence cannot pass this course.
  - Required action: Re-enroll in this course's next edition, and ensure you are part of a team.
- If students have an exam grade higher or equal to 5.0 but fail the team project (after SPA correction), their total course grade may be lower than 5.5, and hence students fail this course.
  - Required action: Correct team project based on the course coordinator's grading report, and hand it in again within two weeks after publication of the final grades in this course (submission on Canvas). Only students who fail the team project can have their projects re-graded. The maximum attainable grade on the regraded team project is a 6.0.
- Students who have passed the course, but wish to retake the exam, can take the exam resit. The highest exam grade counts. Grades for the team project are retained. In other words, the resit exam still counts for 50% of the final course grade.
- Students who fail the exam and wish to retake the course in a subsequent semester can *retain* their assignment grades upon approval of the course coordinator (grades remain valid for the *next* edition of the course).

### Bonus points

The course is designed as an open education course, with all of its source code publicly available at [the course's GitHub repository](https://github.com/hannesdatta/course-odcm). Students can earn bonus points for contributing to the course in the form of source code (e.g., to provide solutions for assignments, to write a tutorial for a new scraping toolkit, or for debugging code). Some contributions may also qualify for publication at [Tilburg Science Hub](https://tilburgsciencehub.com) (see also [here](https://github.com/tilburgsciencehub/website) for the platform's GitHub repository).

Bonus points are awareded to motivate students and reward excellence (e.g., students showing a performance exceeding the normally expected learning outcomes of the course). The award of bonus points can only lead to a mark-up of a sufficient grade, not of an insufficient grade. Moreover, the mark-up is not higher than 0.5 points and is only be awarded once at the level of the final grade. 

Each award of a bonus point is accompanied by an individualized argumentation (i.e. for each student). The award of bonus points is used sparsingly.


## Code of Conduct

- Please always use English as the default language so that non-Dutch speakers can follow the conversations, even if it concerns topics not directly related to the class (e.g., during breaks).
- Please head over the course's [support section](support) to solve problems or get in touch with the instructor.
- Stay up-to-date by checking this website, Canvas, and watch out for updates on Hannes' social media channels.
- Be on time, and start on time.
- Feel invited to provide informal feedback!
- It's totally fine calling the instructor by his first name. 
- When meeting on Zoom, please turn on your camera, which will facilitate interaction with the course instructor and other students.

{{< hint info >}}
__We value diversity and inclusion__

We do our best to embrace diversity and stimulate integration in this course. We encourage students to be proud of their background (e.g., ethnicity, nationality), personal interest (e.g., hobbies), or any other thing that characterizes them. 

Two ways in which students can bring in *their perspective* is 

- choosing with whom to collaborate (e.g., purposefully bring in people of diverse backgrounds or technical skill levels to a team), and 
- choosing which topic to work on in the team project (e.g., spending sufficient time getting to know each other, creating a safe space, and being open to work on topics off the mainstream).

Curious to learn more? Check out [Tilburg's Diversity & Inclusion Policy](https://www.tilburguniversity.edu/about/working/gender-policy), and learn how Tilburg [supports student diversity](https://www.tilburguniversity.edu/students/studying/campus/diversity). Also feel invited to talk to the course coordinator at any point in time!

{{< /hint >}}

## Structure of the course

Please head over to the course's [modules](../modules) and check out the weekly schedule!

## More links

{{<section>}}
