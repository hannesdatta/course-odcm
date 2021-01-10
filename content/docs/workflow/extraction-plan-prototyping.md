---
bookFlatSection: true
title: "Technical Extraction Plan and Prototyping"
description:
bookHidden: false
weight: 30
description: "Make a technical plan for data extraction and storage, and prototype your data collection."
---


# Technical Extraction Plan and Prototyping

Once you’ve chosen (one or multiple) websites or APIs for data extraction, define the exact data that you would like to get, how to retrieve it (e.g., using software running on your local computer), and where to store it (e.g., files, databases in the cloud). Throughout, build a prototype to reassure yourself about the technical feasibility.

## Data extraction

### Entities and extraction frequency

Select the entities for which you would like to extract data from the website or API. Recall that not all entities available may be relevant for your research. Adding many entities seems "safe" for data coverage, but may inadvertently increase the complexity and costs of your data collection.

Next, determine the extraction frequency for each entity. In broad terms, do you require data only once, or at regular intervals (e.g., hours, days, weeks)? Alternatively, are there any external events that may trigger your data collection (e.g., such as when participation in a survey triggers the collection of your survey participant's data on social media).

### Seeds and sampling procedure

Choose the "seeds" for your data collection. Seeds serve as a starting point for your data collection, and we distinguish two types:

- Internal seeds originate on the site or API that you are about to scrape. For example, to obtain pricing data for a sample of books from Amazon.com, you could first gather the product IDs of all products listed on the product overview page for a particular category, and subsequently visit their product pages.

- External seeds do not originate on the focal site or API. They come from different, *external* sources. For example, you could start your data collection using a list of books from the New York Times Bestseller list. External seeds are widely used, for example because they convince readers of your study about your sampling scheme ("of course, the books on the NYT bestseller list are highly popular books!"), and may free you from the criticism that an unknown algorithm interfered in your sample selection, such as may be the case with internal seeds that may be ambiguously defined. Of course, using external seeds requires you to be able to link your seeds to your website or API (which, in the case of ISBNs is straightforward, but which may be more difficult in the absence of common, searchable identifiers).

### Navigation path

Imagine you would like to manually collect the data for your study from the web. Imagine how many times you would have to click (and copy-paste!), until you would have navigated the entire site! To free you from the effort (and time) involved in manually clicking, you need to define your scraper's *navigation path*.

#### Single entities

Information - even for single entities (such as the reviews for the latest iPhone) - is rarely available without "extra" clicks (e.g., on a single page). How does your scraper needs to navigate to obtain all necessary data? In the case of product reviews for the iPhone, you need to deal with *pagination*, by understanding *how* to make your scraper navigate through all of the available pages of reviews. Typically, you can iterate through all pages by slightly modifying the website URL (e.g., by swapping page numbers), or the arguments of an API endpoint (`&page=2`, `&page=3`, etc.). For most websites, unfortunately, merely modifying the arguments is not sufficient and you need to *simulate user behavior* (e.g., by opening a browser, and programmatically "clicking" on the button to accept cookies or proceed to a next page).

#### Multiple, connected entities

If you're planning on obtaining data on multiple entities that are related to one another (e.g., products, and the reviews for each of the products), you need to map the navigation from one entity to the other. Let's extend the example from before, except that now, we are interest in the reviews for *all smartphones*, not only the most recent iPhone. The navigation path becomes:
- obtain a list of seeds (e.g., loop through all pages of the product overview page),
- visit each product's product overview page (e.g., to gather product attributes), and
- visit each review page (pagination!) for each of the products in your sample.

{{< hint info>}}
If you haven't written code up to this point, it's high time you start prototyping your data retrieval. Can you reach particular pages by modifying the website's URL, or do you have to simulate clicking or scrolling behavior? Also, is any user interaction required to load all data that you would like to get from a page?

{{< /hint >}}

### Select data

Finally, for each entity, select the data you would like to extract. Determine how to "tell" your scrapeR where the particular data is located on a page. This process of making searchable a website's content or the results of an API call is called *parsing*. We give details on parsing data from websites and APIs next.

#### Data from websites

Numerous packages (e.g., `BeautifulSoup` in Python) exist which parsing and structure data for you. Still, the challenge is to identify *how to locate the elements* to extract information on. It's not without a good reason that the Python package is called __`BeautifulSoup` - the "soup" of information can easily be overwhelming!

Luckily, unstructured web data is actually pretty organized. The reason is that many years ago, the pioneers of the world wide web developed a standard for how code is visually rendered on websites. Even decades after the invention of this standard - HTML (or, hypertext markup language) -, the web relies on more or less of the same conventions: elements in your website's HTML source code - such as headers, bodies of texts, links, or images, all have particular characteristics. Once you know the characteristics of your target elements, extracting information from it becomes straightforward.

{{< hint info>}}

To find out how to identify the elements that you would like to extract, point your browser to the target page and open your browser's development tools. You can now concurrently browse the visual website, and take a look at the website's underlying source code. In particular, you can explore which attributes, classes or styles are associated with a particular target element. Also, you can experiment with writing some code to see whether you can actually capture what you're interested in.

Beware that a website's underlying source can change over time, rendering your extraction code useless. Also, a website's source code depends on the type of device or operating system that you're using to visit the page. So, if you've developed your scraping code on a Windows PC with Firefox, it probably won't run when scraping with Chrome on Linux...

{{< /hint >}}

#### Data from APIs

Extraction from data provided via APIs is much easier than extracting data from websites. Most APIs provide their data in the JSON (Java Script Object Notation) format, which boils down to a tree of attributes and values. Once parsed in Python (e.g., using the `json.loads` function), the tree is searchable, and information can be extracted simply by referring to its attribute names.

{{< hint info>}}

Parsing becomes more demanding when encountering *lists* rather than single values (this occurs in so-called *nested* JSON trees). Carefully think about *how* to extract and store the information. For example, you could concatenate multiple values, using commas as separators. In some situations, this could create a mess - especially when you're concatenating strings that contain the separation character you've used to tell them apart!). The rule of thumb here is that if information stored in arrays is individually important (i.e., each value of it), it's much safer to store it *normalized* (i.e., in its own table).

{{< /hint >}}

## Storage and deployment

### Storage format, location, and technology

When storing data, you need to choose how exactly to store it *during* the collection, *after the collection* (e.g., for using the data), and *for long-term use in a data archive* (e.g., so that others can use the data).

Storage format refers to the structure of the data. For example, image data is best kept in its original file format (unless you want to compress it), while numeric or textual information is best stored in tabular format with a primary key that you can later use to merge other data to. Typically, each entity that you capture gets its own "table" of data. Of course, there are exceptions to this rule, such as when the information of your focal entity, in fact, contains data on multiple entities (e.g., the (one or many) artist names associated with song releases). Another way to think about this is to evaluate whether normalization of your resulting data seems warranted.

Location consists of two main "types" of locations: first, the geography of data storage (e.g., within the EU), and whether you're storing the data locally (e.g., on your office PC), or remotely (e.g., in the cloud).

Finally, choose how to organize your data. The choice is between a file-based system, versus a database. For example, if you're extracting image data, you may decide to store them as files. Also tabular CSV files belong to this category. Alternatively, you can store data in databases, which are collections of tables with clearly defined relationships to one another. Databases are more durable than file systems, and they allow you to easily separate extraction (e.g., on remote computers on AWS), from storage (e.g., in a safely secured database on campus).

{{< hint info >}}
__Should you store the raw data during collection?__

We have encountered two predominant "scraping philosophies" among researchers. The first group scrapes from websites, and directly saves the required and parsed data in files or to databases. Such a data collection is optimized for simplicity, speed and storage usage.

The second group *separates data collection from data storage*. In particular, a researcher would obtain a website's source code or JSON objects, and store it as is. Then, in a post-processing step, the desired information is extracted from these stored raw data files. The upside of such a process is that you can also extract data that you haven't even planned on getting (e.g., sometimes unexpected data pops up, which proves to be very valuable!). Also, one can easily debug the data extraction and parsing scripts should website updates render your initial parsing code faulty, or should you discover that *actually* an API returns unexpected data. The downside of following this process is that storing *all data* - even if only temporarily - may breach privacy laws or exceed your disk space.

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
