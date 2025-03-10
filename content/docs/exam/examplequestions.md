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

1. According to "Fields of Gold", what are useful dimensions to distinguish websites when considering them for a scraping project? (*knowledge*)

2. What is the purpose of `beautifulSoup` in the context of web scraping? (*comprehension*)

3. Please describe the difference between "parsing on the fly" versus "parsing after the data collection" (according to "Fields of Gold"). (*comprehension*)

4. What conclusions can you draw with regard to the accuracy of the timestamps provided in the user review section of metacritic (e.g., https://www.metacritic.com/movie/the-godfather/user-reviews )? Provide a short answer in less than 50 words. (*analysis*)

5. Please take a look at the code snippet below, which retrieves data on the title and number of comments for posts on the 'marketing' subreddit. Please modify the code such that this data is extracted for the 'digitalmarketing' and 'socialmedia' subreddits, in addition to the 'marketing' subreddit. The output should be a list with dictionaries including the subreddit name, title and number of comments for each post.


    ```
    import requests
    headers = {'authority': 'www.reddit.com', 'cache-control': 'max-age=10', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-language': 'en-GB,en;q=0.9'}

    def get_posts(subreddit):
        url = f'https://www.reddit.com/r/{subreddit}.json'
        response = requests.get(url,
                                headers=headers)
        json_response = response.json()
        posts = []
        for item in json_response['data']['children']:
            posts.append({'title': item['data']['title'],
                        'number of comments:': item['data']['num_comments']})
        return posts

    posts = get_users('marketing')
    posts
    ```

    **Solution**
    ```
    import requests
    headers = {'authority': 'www.reddit.com', 'cache-control': 'max-age=10', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-language': 'en-GB,en;q=0.9'}

    def get_posts(subreddit):
        url = f'https://www.reddit.com/r/{subreddit}.json'
        response = requests.get(url,
                                headers=headers)
        json_response = response.json()
        posts = []
        for item in json_response['data']['children']:
            posts.append({'subreddit name': item['data']['subreddit'],
                        'title': item['data']['title'],
                        'number of comments:': item['data']['num_comments']})
        return posts

    subreddits = ['marketing', 'digitalmarketing', 'socialmedia']

    all_posts = [] # create empty list to hold final results

    # loop through subreddits
    for sub in subreddits:
        # use `get_users()` function to retrieve post for subreddit `sub`
        retrieved_posts = get_posts(sub)
        # loop through posts, and add to `posts` list holding all posts as a final result
        for post in retrieved_posts:
            all_posts.append(post)
    all_posts
    ```

6. Please evaluate the feasibility of this data extraction plan:

    {{< hint >}}

example data extraction plan*

    {{< /hint >}}

7. Please collect the product names and prices for all books listed in this section: https://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html. Please not only list these variables, but also provide timestamps from the moment that you started your data collection. Submit your (a) Python code (as `.py` or `.ipynb`), along with the collected data (`.json`). Please start from the code snippet below.

    **Code to start from**

    ```
    # import packages
    import requests
    from bs4 import BeautifulSoup
    import time
    import json

    # set url
    page_url = 'https://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html'

    res = requests.get(page_url)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, "html.parser")
    books = soup.find_all(class_="product_pod")

    for book in books:
        name = book.find('h3').get_text() 
        print(name)
    ```

    **Solution**

    ```
    # import packages
    import requests
    from bs4 import BeautifulSoup
    import time
    import json

    # set url
    page_url = 'https://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html'


    def get_books(page_url):

        res = requests.get(page_url)
        res.encoding = res.apparent_encoding
        soup = BeautifulSoup(res.text, "html.parser")
        books = soup.find_all(class_="product_pod")

        time_start = int(time.time())

        book_list = []

        for book in books:
            name = book.find('h3').get_text() 
            price = book.find('p', class_='price_color').get_text()
            return_dic = {'name': name,
                        'price': price,
                        'time_start': time_start}
            book_list.append(return_dic)
        return(book_list)

    # write a function that checks whether there is a next page
    def check_next_page(url):
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        next_btn = soup.find(class_= "next")
        return next_btn.find("a").attrs["href"] if next_btn else None

    all_books = []
    while page_url:
        print(page_url)
        for book in get_books(page_url):
            all_books.append(book)

        if check_next_page(page_url) != None: 
            page_url = "https://books.toscrape.com/catalogue/category/books/nonfiction_13/" + check_next_page(page_url)
        else: 
            break 

    # write to file
    f = open('all_books.json', 'w')
    for book in all_books:
        f.write(json.dumps(book)+'\n')
    f.close()
    ```


8. Scrape the top 1000 lifetime grossing movies (domestic) from [Box Office Mojo](https://www.boxofficemojo.com/chart/top_lifetime_gross/?area=XWW). Export the rank, title, lifetime gross and release year of these movies to a CSV file.

   **Code to start from**

    ```
    # import packages
    import requests
    url = 'https://www.boxofficemojo.com/chart/top_lifetime_gross/?area=XWW&offset=0'
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, "html.parser")
    movies = soup.find(class_='imdb-scroll-table')
    
    ```

    **Solution**
  

    ```
    import requests
    import csv
    
    
    top_1000=[]
    
    for i in range(5):
        page_url='https://www.boxofficemojo.com/chart/top_lifetime_gross/?offset='+ str(i*200)
        
        res = requests.get(page_url)
        res.encoding = res.apparent_encoding
        soup = BeautifulSoup(res.text, "html.parser")
        movies = soup.find('table', class_= 'mojo-body-table')
       
        j=0  
        for movie in movies:
            
            if j!=0:
                
                ranking= movie.find('td', class_='a-text-right').get_text()
    
                title= movie.find('a', class_='a-link-normal').get_text()
    
                lifetime_gross=movie.find('td', class_='mojo-field-type-money').get_text()
    
                release_year= movie.find('td', class_='mojo-field-type-year').get_text()
            
    
                top_1000.append({'ranking':ranking,
                                'title': title,
                                'lifetime_gross': lifetime_gross,
                                'release_year': release_year})
    
            j=j+1
        
        
    with open('top_1000movies.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['ranking', 'title', 'lifetime_gross', 'release_year'])
        writer.writeheader()  
        writer.writerows(top_1000)  

   
    ```


9. Please use Selenium to open https://infinite-scroll.com/demo/full-page/, and scroll down 10 times. As you proceed, store all H2 titles in a new-line separated JSON file (store not only links, but also the iteration number).

   **Code to start from**

    ```
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from bs4 import BeautifulSoup
    import time

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    url = "https://infinite-scroll.com/demo/full-page/"
    driver.get(url)
    time.sleep(4)

    # Scroll down the page
    scroll_pause_time = 2
    for _ in range(3):  # Scroll down 3 times
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)

    ```

    **Solution**
  

    ```
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from bs4 import BeautifulSoup
    import time
    import json

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    url = "https://infinite-scroll.com/demo/full-page/"
    driver.get(url)
    time.sleep(4)

    f=open('infinite_scroll.json','w',encoding='utf-8')

    # Scroll down the page
    scroll_pause_time = 2
    for _ in range(10):  # Scroll down 10 times
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        soup = BeautifulSoup(driver.page_source)
        for title in soup.find_all('h2'):
            obj={'title': title.get_text()}
            f.write(json.dumps(obj))
            f.write('\n')
            
        time.sleep(scroll_pause_time)

    f.close()    
    ```


10. Please scrape all key headlines along with their URLs from the New York Times homepage (https://www.nytimes.com/). Since the site has a cookie consent banner, please use Selenium to automate clicking the "Accept all" button. First, collect your data to a dictionary. Then, save the data to a JSON file (`nytimes_articles.json`). 

**Starter Code:**
```
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# Initialize WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Open New York Times homepage
url = "https://www.nytimes.com/"
driver.get(url)
time.sleep(3)  # Wait for page to load

# Handle cookie banner (Click "Accept all" button)
try:
    cookie_button = driver.find_element(By.XPATH, 'TODO: Add cookie button path here')
    cookie_button.click()
    print("Cookie banner accepted.")
    time.sleep(2)  # Allow time for the banner to close
except:
    print("No cookie banner found or already accepted.")

# Extract article headlines and URLs
soup = BeautifulSoup(driver.page_source, 'html.parser')
articles = []

# TODO: Find all article elements and extract the title and URL

# Save extracted data to a JSON file
with open('nytimes_articles.json', 'w', encoding='utf-8') as f:
    # TODO: Write the articles list to the JSON file

# Close WebDriver
driver.quit()
```

**Solution:**

```
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# Initialize WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Open NYTimes
url = "https://www.nytimes.com/"
driver.get(url)
time.sleep(3)  

# Handle cookie banner (Click "Accept all" button)
try:
    cookie_button = driver.find_element(By.XPATH, '//button[@data-testid="Accept all-btn"]')
    cookie_button.click()
    print("Cookie banner accepted.")
    time.sleep(2)  # Allow time for the banner to close
except:
    print("No cookie banner found or already accepted.")

# Extract all articles with titles and URLs
soup = BeautifulSoup(driver.page_source, 'html.parser')
articles = []

for section in soup.find_all('section', class_='story-wrapper'):
    link = section.find('a', class_='css-9mylee')  # Find the article link
    title_tag = section.find('div', class_='css-xdandi')  # Find the title container
    
    if link and title_tag:
        article_title = title_tag.get_text(strip=True)  # Extract the article title
        article_url = link['href']  # Extract the article URL

        # Store in dictionary format
        articles.append({
            "title": article_title,
            "url": article_url
        })

# Save to JSON
with open('nytimes_articles.json', 'w', encoding='utf-8') as f:
    json.dump(articles, f, ensure_ascii=False, indent=4)

print("\n Articles saved to 'nytimes_articles.json'")

# Close WebDriver
driver.quit()
```

11.  Scrape all category names, (e.g., "academic study applications"), and their corresponding article subcategories (e.g., exam preparation) and links from tilburg.ai (https://tilburg.ai/articles/) using BeautifulSoup. Please extract information on the category names, along with the subcategory names and links listed within them. Save them in *one* JSON object, stored in *one* JSON file called `tilburg_ai_articles.json`.

**Starter Code:**
```
import requests
from bs4 import BeautifulSoup
import json

# URL to scrape
url = 'https://tilburg.ai/articles/'

# Fetch the page content
response = requests.get(url)

# Check if the request is successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    data = []

    # TODO: Find all sections containing subheaders and articles

    # TODO: Loop through each section, extract subheader and articles

    # TODO: Save extracted data in JSON file

    print("Data saved to 'tilburg_ai_articles.json'")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
```




**Solution:**

```
import requests
from bs4 import BeautifulSoup
import json

# URL of the Tilburg.ai Articles page
url = 'https://tilburg.ai/articles/'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Initialize a list to hold the data
    data = []

    # Find all sections that represent subheaders and articles
    sections = soup.find_all('section', class_='menu-section')

    # Iterate over each section
    for section in sections:
        # Extract the subheader (category) name
        subheader_tag = section.find('h2')
        if subheader_tag and subheader_tag.a:
            subheader = subheader_tag.a.get_text(strip=True)

            # Initialize a list to hold articles under this subheader
            articles = []

            # Find all article links within the section
            article_tags = section.find_all('a', href=True)
            for article_tag in article_tags:
                article_name = article_tag.get_text(strip=True)
                article_url = article_tag['href']
                articles.append({'name': article_name, 'url': article_url})

            # Append the subheader and its articles to the data list
            data.append({'subheader': subheader, 'articles': articles})

    # Save the data to a JSON file
    with open('tilburg_ai_articles.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("Data has been saved to 'tilburg_ai_articles.json'")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
```

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
