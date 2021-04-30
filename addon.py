from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://www.omnycontent.com/d/playlist/4809bc8a-e41a-405c-93da-a8cf011df2f4/f4c20113-e8b0-4a61-88fc-aafb0100639f/b89b4c6a-cc72-43f2-a35c-aafb0102f899/podcast.rss"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://www.omnycontent.com/d/playlist/4809bc8a-e41a-405c-93da-a8cf011df2f4/f4c20113-e8b0-4a61-88fc-aafb0100639f/b89b4c6a-cc72-43f2-a35c-aafb0102f899/image.jpg?t=1612818988&size=Larg"},
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('episodes'),
            'thumbnail': "https://www.omnycontent.com/d/playlist/4809bc8a-e41a-405c-93da-a8cf011df2f4/f4c20113-e8b0-4a61-88fc-aafb0100639f/b89b4c6a-cc72-43f2-a35c-aafb0102f899/image.jpg?t=1612818988&size=Larg"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes/')
def episodes():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast = mainaddon.get_playable_podcast(soup1)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

if __name__ == '__main__':
    plugin.run()
