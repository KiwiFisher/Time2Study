__author__ = 'Julian Abraham'
__project__ = 'AUT Arion Paper Search Scraper'

"""This package is designed to scrape html information off on Arion. It can be used to access any information on any papers within AUT
including timetable information"""

from bs4 import BeautifulSoup as BS
from selenium import webdriver as webdriver
from paperscraper.paper import paper

paper_dictionary = {}


class paperscraper:
    def __init__(self):
        driver = webdriver.PhantomJS()
        my_url = 'https://arion.aut.ac.nz/ArionMain/CourseInfo/Information/Qualifications/PaperSearch.aspx'

        # Open a client
        driver.get(my_url)

        # By clicking search with no input we are able to view ALL papers. VERY handy :3
        button = driver.find_element_by_name("wucControl:cmdPaperSearch")
        button.click()

        # Parse the html for BS
        html_source = driver.page_source
        soup = BS(html_source, "html.parser")

        # Close the driver
        driver.close()

        # Find all the links in the class table
        paper_table = soup.findAll("a", {"class": "Navigation"})

        for i in range(len(paper_table)):
            if i % 2 == 0:
                code = paper_table[i].getText()
                name = paper_table[i + 1].getText()
                link = "https://arion.aut.ac.nz/ArionMain/CourseInfo/Information/Qualifications/" + paper_table[i][
                    "href"]

                # Add the paper to the paper dictionary
                paper_dictionary[code] = paper(code, name, link)

    # Returns a dictionary of all papers in the format {code : paper }
    def get_papers(self):
        return paper_dictionary

    # This method will return the paper object corresponding to the code parsed
    def get_paper(self, code):
        if code in paper_dictionary:
            return paper_dictionary[code]
        else:
            return paper(code, "INVALID CODE", "")
