# Elliot

TASK DESCRIPTION

part1) the client ordered me to scrape pagesjaunes.fr an online repository for French businesses. I had to perform search on that platform by using a predefined keyword and a list of locations. The search resulted in a list of the links to the businesses' profile pages in the repository. I had to access each of the profile pages to get an URL directing to the businesses' websites.

part2) I had to go through every single website domain that I had extracted and extract all emails (expression containing '@' or 'mailto:')

The keyword to be searched was 'pharmarcie' (it means 'drugstore' in french). That keyword had to be searched in combination with 50 different location. The client provided an .xlsx file containing the list of the locations in the first column with the rest of the columns left empty.

GENERAL APPROACH
I decided to solve this task using by making to bots and a separate script. The first bot crawled pagesjaunes.fr. The second one crawled the URLs obtained by the first bot and finally the script processed the results of the second bot and prepared the final .xlsx file to be forwarded to the client.

Part 1 - SOLUTION - Initially I attempted to scrape the  pagesjaunes.fr website using Python Scrapy as the most efficient solution for the most of the crawling tasks. However, it turned out that the website had a quite complicated structure and advanced anti-bot protection which prevented Scrapy from being able to perform any reasonable work on it. So I decided to go for Python Selenium Webdriver as an alternative which could more efficiently imitate user behavior to avoid anti-bot protection and interact with the website's complicated structure.

First I discovered that the search phrase + location inquiries could be passed as URL arguments. Therefore, the first task of the bot was to design 50 initial search URLs to get the search results for pharmacies in each of the 50 cities provided by the client. After the search URL was accessed, the bot randomly scrolled the page up and down to imitate user behavior. Then it opened the profile pages of the businesses one by one, scrolled each of the profile pages to the bottom for the profile pages to fully load, located the businesses' websites and saved those in a dictionary with the pharmacies' names as keys and pharmacies' website URLs as values. If bot discovered a pharmacie's name which had already been saved it did not access the business's profile page to save time. The results were saved in .json format.

Part 2 - SOLUTION - After the extraction of the websites URLs from the pagesjaunes.fr was over the resulting .json file was passed to another Scrapy bot designed by me. The bot accessed each of the URLs provided and followed every link with the website's domain name searching for emails (expressions containing "@" symbol). Luckily, it turned out that it were only the e-mails that included  the "@" symbol. Each of the search hits was saved as a separate dictionary with the domain name as a key and e-mail as a value. Since it took pretty while for the Scrapy bot to accomplish this task I deployed it to a Scrapy Cloud (https://scrapinghub.com/scrapy-cloud), which I rented for 10 USD/month. The resulting .json file was processed by the third script which merged all the dictionaries in one with domain name as a key and all the corresponding e-mails as a value in the format of a list of strings. The same script prepared the .xlsx file to be provided to the client.

RESULTS

The client was completely satisfied with the my job and came back to me shortly with a similar task
