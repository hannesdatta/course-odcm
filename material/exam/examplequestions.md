---
title: "Example questions"
bookFlatSection: true
bookHidden: false
weight: 5
draft: false
---

# Example questions

Questions will be asked along the course's learning goals (e.g., "learn how to scrape") and six cognitive skill levels (e.g., "application") (for details, see [here](../exam#content)). Below, you can find a few example questions. Example questions will be discussed with students in the final live stream of this course.

{{< hint warning >}}

The exam consists of __open (answer boxes, file uploads) and closed (multiple-choice) questions__. You can go freely back and forth between questions.

{{< /hint >}}

![](../intro_part1.png)
![](../intro_part2.png)

*Note: the number of questions depends on the points awarded to each question. The instructions during the final exam may slightly vary, so make sure to still read it accordingly.*



<!--
8. As a researcher you're interested in polarity in online communities and therefore collect data on the distribution of up and down votes on Reddit. Extract a random sample of at least 100 Reddit posts from the [`politics`](https://www.reddit.com/r/politics) and [`science`](https://www.reddit.com/r/science) communities. Store the original JSON response, along with a parsed CSV dataset with the ID and text of a post. Submit your (a) Python code (as `.py` or `.ipynb`), along with the collected data (`.json` and `.csv`).

    **Code to start from**
    
    ```
    # import packages
    import requestsgit st
    import json
    import csv

    # politics JSON response 
    url_politics = "https://www.reddit.com/r/politics.json"

    headers = {'authority': 'www.reddit.com', 'cache-control': 'max-age=10', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-language': 'en-GB,en;q=0.9'}
    response_politics = requests.get(url_politics, headers=headers)
    json_response_politics = response_politics.json()

    # science JSON response
    url_science = "https://www.reddit.com/r/science.json"
    ```

    **Solution**

    ```
    # import packages
    import requests
    import json
    import csv

    # politics JSON response 
    url_politics = "https://www.reddit.com/r/politics.json"

    headers = {'authority': 'www.reddit.com', 'cache-control': 'max-age=10', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-language': 'en-GB,en;q=0.9'}
    response_politics = requests.get(url_politics, headers=headers)
    json_response_politics = response_politics.json()

    # science JSON response
    url_science = "https://www.reddit.com/r/science.json"

    response_science = requests.get(url_science, headers=headers)
    json_response_science = response_science.json()

    # write to a .json file
    # politics
    with open('json_response_politics.json', 'w') as outfile:
        json.dump(json_response_politics, outfile)
    print('done!')
    # science 
    with open('json_response_science.json', 'w') as outfile:
        json.dump(json_response_politics, outfile)
    print('done!')

    # write a function that collects all reddit posts on a certain subredddit page
    def reddit_posts(subreddit, num_pages):
        after = None
        posts = []
        
        for counter in range(num_pages): 
            url = f'https://www.reddit.com/r/{subreddit}.json'
            print('processing ' + url + ' with after parameter: ' + str(after))
            response = requests.get(url, 
                                    headers=headers, 
                                    params={"after": after})
            json_response = response.json()
            after = json_response['data']['after']
            for item in json_response['data']['children']:
                    tmp = {}
                    tmp['title'] = item['data']['title']
                    tmp['id'] = item['data']['id']
                    posts.append(tmp)
        return posts
        
    total_posts =  reddit_posts("politics", 10) +  reddit_posts("science", 10)

    # convert to csv
    with open("reddit_posts.csv", "w", encoding = "utf-8") as csv_file:
        writer = csv.writer(csv_file, delimiter = ";")
        writer.writerow(["title", "id"])
        for content in total_posts:
            writer.writerow([content['title'], content['id']])
    print('done!')
    ```
-->

<!--

{{< hint info >}}

__This section is still work-in-progress (i.e., we are still adding examples and add code/data where needed).__

{{< /hint >}}
-->




<!--

## 1. Python Bootcamp

*Question type: Application*

Write a function `url_detector()` that loads a list of URLs from the file [`urls.txt`](https://github.com/hannesdatta/course-odcm/blob/master/content/docs/course/exam/urls.txt), and filters that list for valid URLs, starting with `https` and containing a link to a product ID. Although you could rely on [regular expressions](https://tilburgsciencehub.com/building-blocks/develop-your-coding-skills/learn-to-code/learn-regular-expressions/) to get the job done, other simpler workarounds exist. How many URLs do you end up with?


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
-->
