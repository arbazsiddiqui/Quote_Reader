__author__ = 'siddiqui'
import json
import urllib
import Tkinter
import tkMessageBox
import time


window = Tkinter.Tk()
window.wm_withdraw()
for i in range(1,5):
        url = "http://www.iheartquotes.com/api/v1/random?format=json&max_characters=480&source=hitchhiker+dune+plato+science+education+henry_david_thoreau+libery+wisdom+love+literature+technology+nietzsche+math+oscar_wilde+wisdom+humorists+art+platitudes+south_park+esr+humorix_misc+humorix_stories+joel_on_software+macintosh+mav_flame+osp_rules+paul_graham+prog_style+subversion+1811_dictionary_of_the_vulgar_tongue+codehappy+fortune+liberty+literature+misc+murphy+oneliners+riddles+rkba+shlomif+shlomif_fav+stephen_wright+calvin+forrestgump+friends+futurama+holygrail+powerpuff+simon_garfunkel+simpsons_cbg+simpsons_chalkboard+simpsons_homer+simpsons_ralph+south_park+starwars+xfiles"
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        quote = data["quote"]
        tkMessageBox.showinfo(title= "Quote", message=quote)
        time.sleep( 1500 )
#TODO traybar popup
#TODO implement scheduled text message