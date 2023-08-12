#! python3
# lucky.py - Opens several Google search results
import sys, webbrowser, googlesearch
print('Googling ... ')
query = ' '.join(sys.argv[1:])
webbrowser.open("https://www.google.com/search?q=" + query)
for link in googlesearch.search(query, tld="co.in", num=10, stop=10, pause=2):
    print(link)
    webbrowser.open(link)