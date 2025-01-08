"""
What are the key constructs required to create a loop? Identify two scenarios that may require two different types of loops.
Be sure to provide specific details for each scenario that illustrate why the different types of loops are required.
Include a brief pseudocode example to share that includes at least one loop.

To create a loop in programing we require
1. an initialization statement
2. a condition to check for continuation
3. an increment/decrement statement to update the loop variable

This means setting up a starting point, defining when to stop iterating, and specifying how to progress through the loop each time it runs

In Python, we can iterate a loop using a iterator Eg: For i in list


Scenario 1: Looping Over a Collection of urls for scraping data

lets say you are building a web scraping tool that gets data from differnt websites. You have a list of urls and
you need to vist each url to retrieve the data. In this case, a for loop is the best choice
as it allows you to iterate over your collection of urls.

Python pseudocode example:

urls = ["www.google.com", "www.uber.com", "www.microsoft.com"]

for url in urls:
    data = scrape_data(url)
    process_data(data)

This can be done in list comprehension too
[process_data(data) for data in [scrape_data(url) for url in urls]]

Here, the for loop loops over each url in the list, scraping and processing the data each url at a time.
We could do the loops over dict too {i: process_data(url) for i, url in enumerate(urls)}

Scenario 2: Waiting for an Event to happen

Lets say you are writing a program that has to wait for an event to happen before it continues.
For eg: it might need to wait until a file available before it open the file to read.
In this case, a while loop is a good choice as it can keep checking for the file till is is available.

Python pseudocode example:

file_path = "file.txt"

while not is_file_available(file_path):
    wait(1)

data = read_file(file_path)

"""