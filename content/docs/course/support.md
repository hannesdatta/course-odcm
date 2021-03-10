---
bookFlatSection: true
title: "Support"
bookHidden: false
weight: 6
description: " "
---

# Support

Are you experiencing technical difficulties, e.g., when working through the tutorials?

For quick questions, please use *WhatsApp* to get in touch with us (+31 13 466 8938).

- Be as specific as possible (e.g., include screenshots, your Jupyter Notebooks or other source code, errors) so that we can help you better.
- Informal language is perfectly fine.
- Please write to us in English.
- Be prepared that we call you back.
- We may ask you for permission to share the conversation with other students on the course's FAQ page. Names/etc. are of course taken out! If you don't wish your issue to be shared with others, simply say so!

**WhatsApp**
+31 13 466 8938

**Email**
h.datta@tilburguniversity.edu

{{< hint info >}}
__Submitting code for feedback__

When submitting code (e.g., as a Jupyter Notebook) for feedback, please ensure that it __runs from top to bottom without errors__ - up to the point where you need feedback. In other words, __don't send "incomplete" code__ in which you ask us to debug a scraper, without actually loading the website.

Please also make use of specific comments in your code to explain the problem. This will help us to help you quicker.


{{< /hint >}}


## FAQ

**Team Project**     

*How should I store API keys and personal credentials in my notebook without disclosing them (e.g., on Github)?*  
With environment variables, you can access variables without literally writing them down in a notebook or script (e.g., `password = "..."`). Follow the steps in [this](https://tilburgsciencehub.com/building-blocks/store-and-document-your-data/store-data/environment-variables/) building block on Tilburg Science Hub (TSH) to learn how to configure environment variables. 

*My scraper collects a whole lot of string (i.e., text) data, but I'd like to filter down on specific elements and exclude everything else. The `replace()` function does not suffice. What would you recommend?*  
Regular expressions are specfically designed to find patterns in string data. Have a look at the [building block](https://tilburgsciencehub.com/building-blocks/develop-your-coding-skills/learn-to-code/learn-regular-expressions/) on TSH on how to get started with regex.  


**Python Bootcamp**

*What's the difference between `if` and `elif`?*  
It's simply a matter of the order. `if` refers to the first condition and `elif` to the condition(s) that follow. There can be 0, 1 or many `elif` statements.

*What is `[]`?*  
It's an empty list. More often than not, it's defined at the top of a function after which items are appended to it.

*How should I interpret `discount_rate += 0.10`?*  
It means take the current value of `discount_rate` and add 0.10 to it. So, say that `discount_rate = 0.10` and you run `discount_rate += 0.10` its value becomes `0.20`.

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
