__author__ = 'siddiqui'
import json
import urllib

for i in range(1,1000):
    ans = raw_input("Do you want to read a quote ?")
    if ans == "no" :
        break;
    else :
        url = "http://www.iheartquotes.com/api/v1/random?format=json&source=hitchhiker+dune+plato+science+education+henry_david_thoreau+libery+wisdom+love+literature+technology+nietzsche+math+oscar_wilde+wisdom+humorists+art+platitudes"
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        quote = data["quote"]
        print quote

#TODO implement scheduled notification
#TODO implement scheduled text message