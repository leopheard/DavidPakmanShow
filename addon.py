from xbmcswift2 import Plugin, xbmcgui
from resources.lib import davidpakmanshow

plugin = Plugin()
URL = "http://feeds.feedburner.com/davidpakmanshow"
URL2 = "https://davidpakman.com/past-shows"

@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://davidpakman.com/wp-content/uploads/2016/03/cropped-tdps-icon-300x300.png"},
   {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "https://davidpakman.com/wp-content/uploads/2016/03/cropped-tdps-icon-300x300.png"},
{
            'label': plugin.get_string(30002), 
            'path': plugin.url_for('past_episodes'),
            'thumbnail': "https://www.davidpakman.com/wp-content/uploads/2016/03/tdps-logo.png"},
    ]
    return items

@plugin.route('/all_episodes/')
def all_episodes():
    soup = davidpakmanshow.get_soup(URL)
    playable_podcast = davidpakmanshow.get_playable_podcast(soup)
    items = davidpakmanshow.compile_playable_podcast(playable_podcast)
    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    soup = davidpakmanshow.get_soup(URL)
    playable_podcast1 = davidpakmanshow.get_playable_podcast1(soup)
    items = davidpakmanshow.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/past_episodes/')
def past_episodes():
    soup2 = davidpakmanshow.get_soup2(URL2)
    past_episodes = davidpakmanshow.get_past_episodes(soup2)
    items = davidpakmanshow.compile_past_episodes(past_episodes)
    return items

if __name__ == '__main__':
    plugin.run()
