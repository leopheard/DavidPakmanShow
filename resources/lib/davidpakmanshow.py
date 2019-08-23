import requests
import re
from bs4 import BeautifulSoup

def get_soup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup))
    return soup
#ORIGINAL LINK get_soup("http://feeds.feedburner.com/davidpakmanshow")
get_soup("http://votesoon16:votesoon16@feeds.feedburner.com/tdpsmembers2012")


def get_soup2(url2):
    page = requests.get(url2)
    soup2 = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup2)
    return soup2
get_soup2("https://davidpakman.com/past-shows/")

def get_playable_podcast(soup):
    subjects = []
    for content in soup.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link
            title = content.find('title')
            title = title.get_text()
#            desc = content.find('description')
#            desc = desc.get_text()
            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
#                'desc': desc,
                'thumbnail': thumbnail,
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast(playable_podcast):
    items = []
    for podcast in playable_podcast:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
#            'info': podcast['desc'],
            'is_playable': True,
    })
    return items

def get_playable_podcast1(soup):
    subjects = []
    for content in soup.find_all('item', limit=15):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link
            title = content.find('title')
            title = title.get_text()
#            desc = content.find('description')
#            desc = desc.get_text()
            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'desc': desc,
                'thumbnail': "http://static.libsyn.com/p/assets/7/2/8/0/72802e4963645d76/DPS_Podcast_new.jpg"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast1(playable_podcast1):
    items = []
    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
#            'info': podcast['desc'],
            'is_playable': True,
    })
    return items

def get_past_episodes(soup2):
    subjects = []
    for content in soup2.find_all('article'):
        try:        
            link = content.find('source')
            link = link.get('src')
            print "\n\nLink: ", link
            title = content.find('h5')
            title = title.get_text()
#            desc = content.find('On the Show')
#            desc = desc.get_text('p')
#            thumbnail = content.find('h4')
#            thumbnail = thumbnail.get()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
#                'desc': desc,
                'thumbnail': "https://davidpakman.com/wp-content/uploads/2016/03/cropped-tdps-icon-300x300.png"
        }
        subjects.append(item) 
    return subjects
def compile_past_episodes(past_episodes):
    items = []
    for podcast in past_episodes:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
#            'info': podcast['desc'],
            'is_playable': True,
    })
    return items
