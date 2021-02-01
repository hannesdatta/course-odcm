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


## FAQ

**Python Bootcamp**

*What's the difference between `if` and `elif`?*  
It's simply a matter of the order. `if` refers to the first condition and `elif` to the condition(s) that follow. There can be 0, 1 or many `elif` statements.

*What is `[]`?*  
It's an empty list. More often than not, it's defined at the top of a function after which items are appended to it.

*How should I interpret `discount_rate += 0.10`?*  
It means take the current value of `discount_rate` and and 0.10 to it. So, say that `discount_rate = 0.10` and run `discount_rate += 0.10` its value becomes `0.20`.

*Why is indenting code especially important in for-loops?*       
It tells the computer when to break out of a loop. The function below already returns its value after 1 iteration because the `return` statement is part of the loop.

```
sum = 0
for counter in range(10):
   sum += counter
   return sum
```

Actually, it makes more more sense to first finish the loop and only then return the value of `sum`. Like this (i.e., `return` is unindented here!):

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