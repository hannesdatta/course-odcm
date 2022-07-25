---
bookFlatSection: true
title: "FAQs"
bookHidden: false
weight: 10
description: " "
---
# FAQs

## General

*I can't access documents and code stored on Google Drive or Google Colab!*

Please use your `@tilburguniversity.edu` address to log on to Google to view/edit documents posted to Google Drive or Google Colab. Your private `@gmail` addresses won't work.

-------

<!-->
*Will the live streams be recorded?*

Yes, we'll either post them on Canvas (for internal use), or edit them for publication on [YouTube](https://youtube.com/c/hannesdatta).

-------
-->

## Team Project

*How should I store API keys and personal credentials in my notebook without disclosing them (e.g., on Github, or to other students)?*  

With environment variables, you can access variables without literally writing them down in a notebook or script (e.g., `password = "..."`). Follow the steps [here](https://tilburgsciencehub.com/configure/environment-variables).

-------

*My scraper collects a whole lot of string (i.e., text) data, but I'd like to filter down on specific elements and exclude everything else. The `replace()` function does not suffice. What would you recommend?*  

Regular expressions are specifically designed to find patterns in string data. Have a look here](https://tilburgsciencehub.com/learn/regex) to get started with regex.  

-------

*How can I run my web scraper repetitevely (e.g., every day)*

You can use task scheduling to automate the execution of scripts at specified intervals. Follow the steps in [this](https://tilburgsciencehub.com/schedule/task) building block to set-up schedling for your scraper!

-------

*Are there (code) examples from previous years?*

Yes, some code examples are available [here](../../project/projectideas).

*How can I get additional support?*

A good starting point are recorded coaching sessions from previous years, which are available [on this YouTube playlist](https://www.youtube.com/playlist?list=PLdDbyJQwReWhis9Ns7_NfYzw4YAp91D6G). 

Also, Hannes collects useful code snippets on GitHub, see [gist.github.com](https://gist.github.com/hannesdatta).


## Python Bootcamp

*What's the difference between `if` and `elif`?*  

It's simply a matter of the order. `if` refers to the first condition and `elif` to the condition(s) that follow. There can be 0, 1 or many `elif` statements.

-------

*What is `[]`?*  
It's an empty list. More often than not, it's defined at the top of a function after which items are appended to it.

-------

*How should I interpret `discount_rate += 0.10`?*  
It means take the current value of `discount_rate` and add 0.10 to it. So, say that `discount_rate = 0.10` and you run `discount_rate += 0.10` its value becomes `0.20`.

-------

*Why is indenting code especially important in for-loops?*       
It tells the computer when to break out of a loop. The function below already returns its value after 1 iteration because the `return` statement is part of the loop.

```
sum = 0
for counter in range(10):
   sum += counter
   return sum
```

Actually, in this case it makes more sense to first finish the `for` loop and only then return the value of `sum`. Like this (i.e., `return` is unindented here!):

```
sum = 0
for counter in range(10):
   sum += counter
return sum
```

-------

<!--

---

**Webdata for Dummies**  
*Question*  
Answer  

---

**Webscraping 101**  
*I get an error message that a function or variable is undefined, how can I solve that?*
The code blocks often build on each other. That is to say, we use code defined earlier in a cell below that. Even though, the code may already be written there for you, you still need to run it so that the computer also stores it in the memory. Therefore, work your way through the notebook from top to bottom and run each and every cell to avoid problems!

*What does `url_book[6:]` mean?*  
It takes the url_book string and starts at index 6 and continues to the end of the string (so 6 and further). In other words, it skips the first few characters.

*My Spider script looks different than the one in the screenshot, how come?*  
Most likely, you accidentally opened the `.ipynb` file rather than the `.py` script. Jupyter Notebooks are stored as JSON files and therefore store a lot of ancillary data (like cell_type, meta data etc.). Download the `.py` from the website, store it in the same directory as your notebook and try again.

-->
