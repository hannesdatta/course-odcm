---
bookFlatSection: true
title: "Technical Extraction Plan and Prototyping"
description:
bookHidden: false
weight: 30
description: "Make a technical plan for data extraction and storage, and prototype your data collection."
---


# Technical Extraction Plan and Prototyping

Once you’ve chosen (one or multiple) websites or APIs for data extraction, make a technical extraction plan by defining the exact data that you would like to get, decide about storage (e.g., files, databases) and deployment (e.g., local computer, or in the cloud). Throughout, test whether your plan is actually feasible in a prototype.

## Select entities and data for extraction

### Select entities and extraction frequency

Recall that your data assessment provided you with an overview of *all* available entities via the site or API. When assessing research fit, you evaluated which entities (and, in particular, which sampling scheme) fits your research purpose. Using this information, you now make a decision on which entities you would like to gather data. Recall that adding more and more entities to your study is "costly" in the sense that it takes you time to develop the code, and to actually run the data collection.

Also determine the frequency to retrieve data for each of the entities. For historical data, that's typically just once, unless you want to refresh your data towards the end of your project. For information that's only available in real-time, things get more complicated, and you need to balance the number of entities in your data, the extraction frequency, and the limits imposed by the website, such as only five requests per second.

### Select seeds and sampling procedure

Next, choose the "seeds" for your study - the entry point to starting your data collection. We distinguish between two types of seeds:

- Internal seeds come from the site or API that you also would like to run your scraper on. For example, to obtain a sample of books from Amazon.com, one could gather the product IDs of all products listed on the product overview page for a particular category.

- External seeds do not come from the site or API that you would like to run your scraper. They come from different, *external* sources. For example, you could also use as a start for your book data collection a list of books from the New York Times Bestseller list. Sometimes using external seeds is a "strong" start, because readers of your study may be familiar with the list and the algorithm with which it was build. Of course, using external seeds requires you to be able to link your list of seeds to the target page or API (which, in the case of ISBNs is straightforward, but which may be more difficult if you only had available the names of products).

### Map navigation path

#### Navigation within a single entity

Even information on a single entity - e.g., *all* reviews for the latest iPhone - are rarely available on a single page. You need to map the navigation path that you would like your scraper to follow to obtain complete data. In the case of the reviews we've just mentioned, you need to deal with *pagination*, by understanding *how* to make your scraper navigate through all of the available pages of reviews. Typically, this is done by iterating through all pages by slightly modifying the website URL (e.g., by swapping page numbers), or the arguments of an API endpoint. For most websites, though, merely modifying the page numbers is not sufficient and you need to simulate user behavior (e.g., by opening a browser, and programmatically "clicking" on the box to accept cookies, or on the next page button).

#### Navigation across multiple, connected entities

If you're planning on obtaining data on multiple, *linked* entities, you also need to map the navigation from one entity to the next. For example, let's continue the example from above. Now, we're not only interested on obtaining the reviews of *the latest* iPhone, but from *all smartphones*. The navigation path now becomes:
- obtain a list of seeds (e.g., looping through all pages of the product overview page),
- visit each product's product overview page (e.g., to gather product attributes), and
- visit each review page (pagination!) for each of the products in your sample.

{{< hint info>}}
If you haven't written code up to this point, it's high time that you start prototyping your retrieval strategy. Try out whether you can reach a particular page by merely modifying the URL, or whether you have to simulate clicking or scrolling behavior. Also, try to judge what user interaction is required to load all data that you would like to get from a page.

{{< /hint >}}

### Select data

Finally, for each entity, select the particular data you would like to extract. Of crucial importance is to also determine how to "tell" your scrape where the particular information is located. This process of making searchable the results of an API call or the data on a website is called *parsing*. We give details on parsing and extracting data from websites and APIs next.

#### Data from websites

Numerous packages (e.g., `BeautifulSoup` in Python) exist which assist you in parsing and structuring the data on websites. The challenge is to identify the elements to extract information from the soup of unstructured information (that's probably why it's called `BeautifulSoup`).

Luckily, web data - while it can be considered *unstructured - is pretty organized. The reason is that many years ago, the pioneers of the world wide web developed a standard for how code is rendered for visual websites. Even decades after the invention of this code standard - it's called HTML (or, hypertext markup language), more or less the same conventions are used. Elements in your website's HTML source code - such as headers, bodies of texts, links, or images, all have particular characteristics. Once you know the characteristics of the elements you would like to get, extracting information from it becomes straightforward.

{{< hint info>}}

To find out how to identify the elements that you would like to extract, point your browser to the target page and open your browser's development tools. You can now concurrently browse the visual website, and take a look at the website's underlying source code. In particular, you can now learn which attributes, classes or styles are associated with a particular block of information. Also, you can experiment with writing a little code snippet (e.g., in Python) to see whether you can actually capture what you're interested in.

Beware that a website's underlying source can change over time, rendering your extraction code useless. Also, websites use different source code, depending on the type of device or operating system that you're using to visit the page. So, if you developed your scraping code on a Windows PC with Firefox, it probably won't run when scraping information using Chrome on Linux...

{{< /hint >}}

#### Data from APIs

Extraction from data provided via APIs is much easier than extracting data from websites. Most APIs provide you their data in the JSON (Java Script Object Notation) format, which boils down to a tree of attributes and values. Once parsed in Python (e.g., using the `json.loads` function), the tree is searchable, and information can be extracted simply by referring to its attribute names.

{{< hint info>}}

Parsing becomes more demanding when encountering *lists* rather than single values (this occurs in so-called *nested* JSON trees). One then needs to either concatenate the information, or adapt the unit of analysis to a more fine-grained level when extracting information.

{{< /hint >}}

## Storage and deployment

### Storage format, location, and technology

When storing data, you need to make a choice on its storage technology, format, and location. You can make different choices for data stored *during* the collection, *after your collection* (e.g., for using the data), and *for archiving data to use for others*.

Storage technology refers to the type of "system" you want to use to organize your data. For example, if you're extracting image data, you may decide to save these as files ("file system"). You can also decide to parse the data directly into CSV files. Alternatively, you can store data in databases, which are collections of tables and its relationships to one another. Databases are more durable than file systems, and they allow you to easily separate extraction (e.g., on remote computers on AWS), from storage (e.g., in a safely secured database on campus).

Storage format refers to the structure of the data. Image data can merely be "left" as PNG or JPG files, while information from an ecommerce website may be structured in rows and columns (e.g., a "table" with product IDs, the review text, and the valence score for a particular review).

Finally, decide on where to store the information. For example, it's typically not advisable to store data on your local office PC if you're employing a data collection over extended periods. The decision of using databases and the decision of where to host these databases is typically done concurrently.

{{< hint info >}}
__Should you store the raw data during collection?__

We have encountered two predominant "scraping philosophies" among researchers. One group scrapes information, and selects and stores data of interest in tabular data files (e.g., CSV files, Excel files) or data bases. The upside of this procedure is that the data collection is "very clean", and optimizes on speed and storage usage.

A second group separates data collection from data storage. In particular, this group of people first obtains the raw website source code or JSON objects, and - in a second code snippets - extracts the information that they desire. The upside of such a process is that you can also extract data that you haven't even planned for (e.g., sometimes unexpected data pops up, which proves to be very valuable). Also, one can easily debug the data extraction and parsing scripts should website updates have rendered your initial parsing code meaningless, or should you discover that *actually* an API returns different data, for different type of objects that you get. The downside of following this philosophy is that storing *all data* - even if only temporarily - may breach privacy laws or exceed your disk space.

If you decide to separate data collection from storage, think *where* to store the raw data. For websites, we make use of S3 remote storage on AWS. For JSON objects from APIs, unstructured data bases are perfect (e.g., MongoDB Atlas databases).

{{< /hint >}}

### Software toolkit

Pick the software tool to execute your scraper. If you’re capturing data from an API, does this API have a package available in Python you could use? Or is it more advisable to self-program your data collection? If you’re using a website, can you reliably extract data without actually seeing the website, or do you need to (virtually) open a browser and simulate user behavior, such as clicking?

### Deployment infrastructure

Choose the hardware infrastructure on which to deploy your scraper. Your laptop may be cheap (you already own it), but probably you will have to restart it once a while, or its Wifi connection may drop - making it an error-prone tool. Even local office computers have reportedly been cut off from power for several days… Especially for long data collections, therefore, a remote computer, such as a computer in the cloud, may be much safer.

### Monitoring

Decide how to monitor the data collection while it is running. That’s particularly important for real-time data collections that run over extended periods. Still, even one-shot data collections may benefit from monitoring, e.g., to verify that all requested data, in fact, has been obtained.

{{< button relref="./legalfit.md" >}}Next{{< /button >}}



<!--


d.	Step 4. Select data for extraction
i.	Identify the location of the required content (e.g., CSS, XPATH, regular expressions)
ii.	Decide which specific data to extract (e.g., text on the page, attributes from source code, images or file names to download)
iii.	Convert data in appropriate form (e.g., removing ,000 separators, swapping . with ,. This can be achieved by cleaning or extracting substrings, searching and replacing, etc.)
iv.	Enrich with meta data (e.g., time stamp of scrape, timestamp of job initiation, IP address or derivatives like location details)

e.	Step 5. Determine storage of extracted data
i.	Data structure (structured/flat, versus unstructured JSON)
ii.	Files versus databases
iii.	Location (local versus remote)

-->
