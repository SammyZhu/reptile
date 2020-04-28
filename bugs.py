import requests
from bs4 import BeautifulSoup
import urllib.request
import re

cookies = {}

def test_get_sample():
        url = 'https://hubsoft.zendesk.com/hc/en-us/articles/360039745453-Move-to-New-Domain-Object-ID'
        c = cookies
        r = requests.get(url=url, cookies=c)
        print(r.text)


def test_get_home():
        url = "https://hubsoft.zendesk.com/hc/en-us"
        c = cookies
        response = requests.get(url=url, cookies=c)
        f = open('home.html', 'w', encoding='utf-8')
        f.write(response.text)
        f.close()


def get_url_from_homepage():
        html = open('home.html').read()
        soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
        list1 = []
        for item in soup.find_all("a"):
                list1.append(item.get("href"))
        return list1



def request_url_of_categories(list1):
        print(list1)
        base_url = 'https://hubsoft.zendesk.com'
        str1 = '/hc/en-us/categories/'
        list2 = []
        for i in range(0, len(list1)):
                if list1[i] != None:
                        if str1 in list1[i]:
                                url = base_url + list1[i]
                                print(url)
                                c = cookies
                                response = requests.get(url=url, cookies=c)
                                f = open(list1[i][21:] + '.html', 'w', encoding='utf-8')
                                f.write(response.text)
                                f.close()


def get_url_from_categories():
        list2 = []
        for i in range(6, 14):
                html = open('home_url_' + str(i) + '.html').read()
                soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
                for item in soup.find_all("a"):
                        list2.append(item.get("href"))
        return list2


def request_url_of_articles(list2):
        print(list2)
        base_url = 'https://hubsoft.zendesk.com'
        str1 = '/hc/en-us/articles/'
        for i in range(0, len(list2)):
                if list2[i] != None:
                        if str1 in list2[i]:
                                url = base_url + list2[i]
                                print(url)
                                c = cookies
                                response = requests.get(url=url, cookies=c)
                                f = open(list2[i][19:] + '.html', 'w', encoding='utf-8')
                                f.write(response.text)
                                f.close()


def request_url_of_session(list2):
        print(list2)
        base_url = 'https://hubsoft.zendesk.com'
        str1 = '/hc/en-us/sections/'
        j = 0
        for i in range(0, len(list2)):
                if list2[i] != None:
                        if str1 in list2[i]:
                                url = base_url + list2[i]
                                print(url)
                                c = cookies
                                response = requests.get(url=url, cookies=c)
                                j = j+1
                                f = open(list2[i][19:] + '.html', 'w', encoding='utf-8')
                                f.write(response.text)
                                f.close()


def get_url_from_session():
        list3 = []
        for i in range(1, 97):
                html = open('sections_url_' + str(i) + '.html').read()
                soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
                for item in soup.find_all("a"):
                        list3.append(item.get("href"))
        return list3


if __name__ == "__main__":
        request_url_of_categories(get_url_from_homepage())

