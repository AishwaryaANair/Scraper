The scraper requires the following:
1. Selenium library
2. Chromedriver executable

After installing the above requirements, follow the instructions in the comments above the lines (if any)

(a) How you have implemented the scraper, what challenges you faced and how did you solve them?
A: The scraper is implemented using selenium and it's libraries like webdriver and action chains. The main challenges faced were the security checks implemented by walmart to prevent scraping like the 'click and hold'. I had to bypass them manually. The second challenge was to obtain the rating. The rating was in two formats in star icons and in hidden text for seo purposes. I used the hidden text for the same.

(b) What else you could do to improve your scraper?
A: Automatically bypass the 'click and hold' dialog.

(c) How would you design it to make it work on other retailers as well?
A: Using more 'contains' expression in xpath.