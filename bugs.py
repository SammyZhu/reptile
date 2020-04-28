import requests
from bs4 import BeautifulSoup
import urllib.request
import re

cookies = {
        "_zendesk_cookie": "BAhJIkp7ImRldmljZV90b2tlbnMiOnsiNDA1NjE1OTI3MDUzIjoiQ0ViMW1vVk5wZ2xjU2QwenhSb1pCWUVBN1JBOFRGM0oifX0GOgZFVA%3D%3D--b5cc1bf9fc4b17e082efe146bb2c2c5a12519364",
        "ajs_anonymous_id": "%2268d6c6d0-b865-43d1-b4aa-73014f131235%22",
        "_ga": "GA1.2.1562438430.1587116702",
        "__cfduid": "d0044d05fba70a626804d86a929c9d8921587485244",
        "__cfruid": "ad11c316e67675d2355b90d4f6f2665f4c9e70f4-1587518890",
        "_gid": "GA1.2.191549298.1587477969",
        "_zendesk_authenticated": "1",
        "_zendesk_shared_session": "-ak5uSWRTSXNzeVo3eTJ2Slp3d2FDalhacC9vMFhPOHhtSzY2U0tybldITzRUazZscTM2a1ZwOE8za3hUSzVYRWduVUZBZUFMOGFYVFl0SVpXOVgzdm9nMmVjNGkwNFVuclZZQVJHZHgvOWpQMUprK2kyclVScXdSZ2h4YUhUS1ktLW83R24xSWF2djRUMnhPQ1hlZXl5WXc9PQ%3D%3D--24d5b5fa2a2b6f1fa669c87c455a95beea4b28e1",
        "_zendesk_session": "BAh7C0kiD3Nlc3Npb25faWQGOgZFVEkiJWRkZmU5YzBkMzk0ZWY4NTlkZmQzZDdjNTZjOTUxODI5BjsAVEkiDGFjY291bnQGOwBGaQKjqEkiCnJvdXRlBjsARmkD2CMDSSITd2FyZGVuLm1lc3NhZ2UGOwBUewBJIhBfY3NyZl90b2tlbgY7AEZJIkVFS0g3L3N4c2FmcHdTRDhQWFRxRTZ1eFAyQzFuMHJoR3U3THpKNzFBc3M3azdRNjc5YUQwcGliR3RkNlBGdXlLBjsARkkiDmlzX21vYmlsZQY7AFRG--f3b45fbfc918440acd11e96464199d0499807c7c",
        "_help_center_session": "cjN2MkJXdDY4ZngwNWRrNWhEYmc4eDFNSUh2STJldmpISTZ2V0lROHRqS09VWVA3NkJ6U0s5Tlp1Zzg4VmJyV1hETkc4TVhrcG1LNnRLekdyNzJHekVxTnQwaldLWE0rWFZ3NkR5Kzh0K2ZhWmdHQVdOeiszTWJRQUR5VVRTSmZuazZWYkZlZ094THpucm5laGFsaWJ3UWw0T2toYzQzN2NTQ3JtcUx5aTlXQm9wV0pEeDFFcWxZQ3dwcS9lcC9NNGRGVmtlZjdlUnRQdE5XVklDMmI5Zz09LS03NXBEVE9LMEdlSGEySHdUV2xHY2Z3PT0%3D--66ba1ce07408af59c80d258b5ddcdc78fcd9d1c0"}


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

