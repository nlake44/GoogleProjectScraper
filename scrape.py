import pycurl
import urllib
import sys
def on_receive(data):
  """ Parse output of page for app name and number of stars"""
  lines = data.split()
  for ii in lines:
    if "star_count" in ii:
      ii = ii[15:] # removes first portion
      ii = ii.split('">')
      if len(ii) > 1:
        yield ii[0] + "," + ii[1].split('</')[0]
        sys.stdout.flush()

def getPage2(url):
  f = urllib.urlopen(url)
  return on_receive(f.read()) 
#languages = ["java", "ruby", "python", "php", "erlang", "C", "C++", "C#", "Objective-C", "Basic", "Perl", "Lisp", "Lua", "Javascript"]
#languages = ["all", "app"]
#languages = ['web']
languages = ['appengine']
for lang in languages:
  f = open("./out/"+lang, "w+")
  for ii in getPage2("http://code.google.com/hosting/search?q="+lang+"&btn=Search+projects"):
    f.write(ii +"\n") 
    print ii
  for ii in range(1,600): 
    url = "http://code.google.com/hosting/search?q=&filter=0&mode=&start="+str(ii*10)
    for kk in getPage2(url):
      f.write(kk +"\n")
      print kk
  f.close()

