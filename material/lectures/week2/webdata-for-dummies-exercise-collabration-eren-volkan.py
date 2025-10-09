#!/usr/bin/env python
# coding: utf-8

# # Web Scraping With Scheduling-Cron: Beginners' Walkthrough

# This notebook tries to understand the core coding concepts of web scraping, and do one's best to introduce scheduling-cron to it.
# 
# It will follow three main steps:
# 
# 1. Building the scraper,
# 
# 2. Figuring out the scheduling-cron and
# 
# 3. Doing some basic explarotary analysis with pandas.
# 
# The notebook contains commentary on the codes. It can be a little hard to read, if yes, we are open to suggestions.

# ## Building the Scraper

# In[ ]:


# Lets load the packages
import time
import requests
from bs4 import BeautifulSoup
import json


# ### Scraper part 1

# In[ ]:


url = 'https://api.music-to-scrape.org/artists/featured' # We are extracting the featured artists via music-to-scrape API. 

# The URL can be found within the Featured Artist header on the left of the API documentation.

header = {'User-agent': 'Mozilla/5.0'} # We are impersonating as a Mozilla browser.
web_request = requests.get(url, headers = header) # We are getting the info about featured artists into the web_request object.
web_request.encoding = web_request.apparent_encoding # We are setting encoding to UTF-8.

## This ensures enables us to read non-English characters too.

web_request_source_code = web_request.text # We are extracting the text data in the web_request object.

print(web_request_source_code)


# Below, we are prototyping a small scraper. It scrapes the featured artists from the website **each** second. It stops in **5 seconds**. 
# 
# We need to set a stop time for our while loop. Otherwise, it will run itself endlessly. Since we are prototyping, we decided to run the loop only for 5 seconds.
# 

# ### Scraper part 2

# In[ ]:


featured_artists = [] # We are defining an empty list of featured artists. It will be filled by the upcoming while loop.


end_time = time.time() + 5 # This code here retrieves now's time as unix and adds 5 seconds to it.


# When the while loop reaches the time of this end_time object, it will stop running.

while time.time() <= end_time: # As long as end_time is bigger than or equal to the now's time,
    print('collecting featuring data... please wait.')
    url = 'https://api.music-to-scrape.org/artists/featured'
    response = requests.get(url, headers=header)
    json_response = response.json()
    
    # The json_response object has a artists key and has values under it like 'artist' : X, 'artist_id' : 'ID'.
    # This is the information we've retrieved from the API. Now, we aim to get the IDs. You can print the object to inspect it.
    
    for ids in json_response['artists']: # We are looping through the json_response object's artists key.
        featured_artists.append(ids['artist_id']) # We are retrieving the artist_id's from each artist.
   
    # The loop iterates through artists, and get the values from artist_id key. 
    
    # Eg. [{'artist': 'Bob Neuwirth', 'artist_id': 'AR19SOA1187B98F6E6'}. Can you guess which information is extracted?
   
    time.sleep(1)

print(f'Printing featured artists: {featured_artists}')


# Since we are using API, response of the website is a json format. We can use the `.json()` method and easily and save the response from the server into a json_response object like above. Now we will loop through the values of **artists** key from the json_response object. Afterwards, we will expand the empty list at the top, `featured_artists` with the **artist_id** information.
# 

# The goal is to create a scraper that scrapes in **every** second, for **five** seconds. The delay provided above with the `time_sleep()` function enables that. Without it, code would've tried to get the complete data at once. 
# 
# This is not healthy for a server since it might get flooded with requests.
# 
# Now only part left is to get artist infos based on the artist ids above and write a json file that contains this information.

# ### Scraper part 3

# In[ ]:


f = open('artist_info_sc.json', 'a', encoding = 'utf-8') # We are opening a json file to append, 'a' the extracted information.

for artist in featured_artists: # We are pasting the retrieved artist id's into the URL below to get the artist infos.
    print(artist)
    url = f'https://api.music-to-scrape.org/artist/info?artistid={artist}' # We are adding artist ids here.
    response = requests.get(url, headers=header)
    json_response = response.json()
    json_response['retrieval_unix']=time.time() # We are creating this 'retrieval_unix' key first. 

# We save the time that the info is retrieved into this key as a value. This way, we can keep track when the info is acquired.

    f.write(json.dumps(json_response)) # We are obtaining the json file in character strings.
    f.write('\n') # This adds a blank between the lines.

    time.sleep(1)

f.close()


# ## Scheduling-Cron for macOS / Linux

# After our scraper is done, we need to dwell into the **Scheduling-Cron**. But first, what do they actually mean?
# 
# Scheduling in this sense means to run our scraper at a specific time. Remember that the scraper above runs for *5 seconds*, *every second*. We can manipulate this and ask for it to run for *2 hours*, in *every 10 minutes*, at for example *20:00*, without changing the code itself. In addition, we can tell the computer to perform this action at whichever time we want. 
# 
# So telling the computer to run the code at **20:00 for 2 hours in every 10 minutes** is scheduling.
# 
# Cron is the method we use to make the scheduling happen. We want the python script to run in a given time, in given intervals. Therefore we need to program the computer to do so. For example, when you want to run the script during the night, you can just use Cron to handle this. You can leave your PC open, and schedule a scraping task thanks to the Cron.

# To explain Cron syntax, follow the [Tilburg Science Hub Tutorial](https://tilburgsciencehub.com/building-blocks/automate-and-execute-your-work/automate-your-workflow/task-scheduling/?utm_campaign=referral-short) for Cron.

#  ### Cron syntax for macOS / Linux

# Cron needs a specific syntax to run in mac and Linux. The syntax consists of *5* different symbols. 
# 
# ```
# *    *    *    *    *  
# ┬    ┬    ┬    ┬    ┬
# │    │    │    │    └─  Weekday  (0 - 6)
# │    │    │    └──────  Month    (1 - 12)
# │    │    └───────────  Day      (1 - 31)
# │    └────────────────  Hour     (0 - 23)
# └─────────────────────  Minute   (0 - 59)
# ```
# 
# So if we were to run a script in every 5th and 55th minutes of an hour, we should construct it as: 5,55 * * * *.
# 
# Some examples from the [Tilburg Science Hub Tutorial](https://tilburgsciencehub.com/building-blocks/automate-and-execute-your-work/automate-your-workflow/task-scheduling/?utm_campaign=referral-short)
# 
# - 30 * * * * = every 30th minute of every hour every day
# - 30 5 * * * = at 05:30 on every day
# - 30 5 1 * * = at 05:30 the first day of the month
# - 30 5 1 1 * = at 05:30 on January 1st
# - 30 5 * * 1 = at 05:30 on every Monday
# - 0 0 */3 * * = every 3 days at midnight
# - 30 5 1,15 * * = at 05:30 on every 1st and 15th day of the month
# - */30 9-17 * * 1-5 = every 30 minutes during business hours
# 
# There is a great website called [CronGuru](https://crontab.guru) that explains the Cron Syntax. Check it out for more explanation.

# #### Important Tip

# In our case, we needed to give "Full Disk Access" permission to Cron from System Settings.
# 
# This [stack overflow discussion](URL) will guide you through.
# 
# 
# To add the exception:
# 
# 1. click the + button
# 2. hit ⌘⇧G
# 3. enter /usr/sbin
# 4. double click the cron file.
# 
# If you can see the cron clicked in the security & privacy settings: Perfect! Now you should be able to gave a permission for your cron tasks

# ### Implementing the Required 2 Hours every 10 Minutes Scheduling-Cron for macOS/Linux

# Let's follow the steps from [Tilburg Science Hub Tutorial](https://tilburgsciencehub.com/building-blocks/automate-and-execute-your-work/automate-your-workflow/task-scheduling/?utm_campaign=referral-short):
# 
# 1. `crontab -l` to have a look if there are any cron jobs settled.
# 
# If there are none, let's set one with:
# 
# 2. `crontab -e` 
# 3. `Press I` so that you can edit the text.
# 4. Insert the following syntax *always specify the full path!*
# 
# `<CRON CODE> <PATH OF YOUR PYTHON INSTALLATION> <PATH TO PYTHON FILE>`
# 
# Example: `<*/10 20,21 * * *> </Users/vscanturk/anaconda3/bin/python> </Users/vscanturk/Desktop/collabscript5.py>`
# 
# This will run the code in every 10 minutes for the hours of **20:00** & **21:00**. This way, we'll be able to accomplish what the exercise asks us, running the python script in 2 hours every 10 minutes.
# 
# 
# 5. Press `Esc` and type `:wq` followed by Enter to save your changes (if a window pops up, select OK).
# 
# If you run the `crontab -l` now, your newly scheduled task should be listed. We recommend keeping an eye out whether your scheduler works as expected, especially in the beginning. If not, you can make changes to the cron file at any time. To remove all existing tasks and clean up the cron filetype, use `crontab -r`.
# 
# There are 5 featured artists in the website and our Python retrieves them in every second for 5 seconds. So each time the code runs, we end up with 25 artists. In two hours for every 10 minutes, it will retrieve `12 * 25 = 300` artists.
# 

#  ### Cron for Windows

# There is already a built-in program for running scripts in Windows. Following the [Tilburg Science Hub Tutorial](https://tilburgsciencehub.com/building-blocks/automate-and-execute-your-work/automate-your-workflow/task-scheduling/?utm_campaign=referral-short) once again, we will use the the **task scheduler**.

# 1. Double check if the python script works.
# 
# 2. Open a notepad and get the following script in:
# 
# - @echo off
# - python.exe "name_of_your_python_script.py"
# 
# 3. Save the file as run_script.bat
# * **Important note**: Windows can save notepads with *.txt* extension. Be sure to save your file as not *run_script.bat.txt* but *run_script.bat*.
# 
# 4. Now the script for the scheduler is ready. Next step is to open up the **task scheduler**.
# 
# 5. Type **Task Scheduler** to the search bar and open the built-in program.
# 
# 6. Click *Create Basic Task* and fill out a Name and a Description.
# 
# 7. Under Security Options choose “Run whether user is logged on or not” and tick the box “Run with highest privileges”. These will allow your scheduler to use the .bat script eventhough computer goes into sleep mode and will run the program as an *admin*. 
# 
# * **Important note**: Scheduler can ask for a password at this step. Provide your PC's login password. 
# 
# 8. Create a *Trigger* like *Daily* and set a start and end date/time.
# 
# 9. Create an *Action* and choose your .bat script.
# 
# 10. Now the task is added to your scheduler. On the left, there is *scheduler library*. Select your task and select *Properties*. There you may want to untick the box “Start the task only if the computer is on AC power” (i.e., the script still runs if your laptop is on battery power) and tick the box “Wake the computer to run this task” to make sure the tasks are always executed on time.
# 
# 11. To let the scheduler perform **every 10 minutes for 2 hours**, go to the *Triggers* tab and select the trigger you've created earlier and click *Edit*.
# 
# 12. In the "Edit Trigger" window, set "Repeat task every" to 10 minutes and duration for 1 hour.
# 
# 13. Select the expire time 2 hours prior to the start of the scheduler.
# 
# 14. Save and close.
# 
# 15. Click the task you've created and click *Run*.
# 
# Same again with macOS scheduling, we will end up with **300** artist names and infos.
# 
# **Important Note**: If your PC's Desktop name has different characters, (eg. 'Masaüstü' is the Turkish for Desktop) task scheduler struggles to operate. If so, you can set up a virtual desktop. Contact Eren for further information.
# 

# ## pandas and Summary Statistics

# In[ ]:


import pandas as pd

# Loading the data.

# Specify the path to your JSON file

json_file_path = "artists_info_sc.json" # This is the file that contains 300 artists. 

# In this case, our file is in the same directory with our jupyter notebook. If yours is not, locate it and provide it above.

# For example: json_file_path = "C:/Users/meren/OneDrive/Masaüstü/artists_info_sc.json"

data = []
with open(json_file_path, "r") as json_file:
    for line in json_file:
        json_data = json.loads(line.strip())
        data.append(json_data)

# Read the JSON file line by line and process each JSON object separately


# ChatGPT says that the **with** clause in the beginning helps Python to open the data in reading mode -that's the *r* in the open function. We tend to forget to close the data we've opened. When the opening and closing process is dealt via **with** clause, and data is opened in a reading mode, whole process is safer for both data and Python.
# 

# In[ ]:


data_frame = pd.DataFrame(data) # Now we are changing the imported json file to a data frame.


# Our object is a **pandas dataframe** now. 
# 
# Following functions are all pandas functions, which work well with pandas dataframes.

# In[ ]:


# 1. Number of unique artists captured

unique_artists_count = data_frame['artistname'].nunique() # This nunique() method returns unique values from given column.

print(f"Number of unique artists captured: {unique_artists_count}")

# 2. Number of duplicate artists captured

duplicate_artists_count = len(data_frame) - unique_artists_count # This is the count of all artists minus the unique ones.

print(f"Number of duplicate artists captured: {duplicate_artists_count}")

# 3. Start and end timestamp of process

start_timestamp = data_frame['retrieval_unix'].min() # min() method gets the start time of the scraping.

print(f"Start timestamp of the scraper: {start_timestamp}")

end_timestamp = data_frame['retrieval_unix'].max() # Similar here, max() gets the end of it.

print(f"End timestamp of the scraper: {end_timestamp}")

# 4. Average number of plays for featured artists

average_plays_for_featured_artists = data_frame.groupby('artistname')['total_plays'].mean()

# We group the database by artist names and get the mean of their total plays.

print(average_plays_for_featured_artists)


# ##### *Authors: Volkan Cantürk, Eren Erdoğan*
