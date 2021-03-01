#!/usr/bin/env python
"""
Simple web client, will get information from www.eps.udl.cat 

@author: carlesm
"""


from urllib.request import urlopen 
from urllib.parse import urljoin
import bs4


class Client(object):

    def __init__(self):
        pass 

    def get_web_page(self):
        # get by http a web page
        # return html
        webpage = urlopen("http://bid.udl.cat/ca/")
        html = webpage.read()
        return html

    def parse_web_page(self, html):
        soup = bs4.BeautifulSoup(html, features="lxml")
        events = soup.find_all("li","box")
        event_infomation = []
        for e in events:
            a_time = e.find('time')
            a_time = a_time.text.strip()
            a_element = e.find("a","no-text")
            a_link = a_element['href']
            a_link = urljoin('http://bid.udl.cat/ca/',a_link)
            a_title = a_element['title']
            event_infomation.append((a_title, a_time, a_link))
        return event_infomation

    def get_information(self):
        html = self.get_web_page()
        information = self.parse_web_page(html)
        return (information)



if __name__ == "__main__":
    #  create client 
    client = Client()
    information = client.get_information()
    print(information)