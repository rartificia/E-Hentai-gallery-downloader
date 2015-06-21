#-*- coding: utf-8 -*-
import urllib2
import bs4
import os
import sys
import time
import datetime
import re
reload(sys)
sys.setdefaultencoding('utf-8')



target = sys.argv[1]
img_list = []
inittime = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())

def get_title(url):
    req = urllib2.Request(target, headers={'User-Agent' : "Magic Browser"})
    content = urllib2.urlopen(req)
    soup = bs4.BeautifulSoup(content)
    title = soup.title.string
    return title

def download_images(title):
    print "Downloading images..."
    for link in img_list:
        time.sleep(1.5)
        os.system('wget "%s" -P "%s/"'%(link,inittime))
    print "Image Downloading Complete."
    print "%d images fetched."%(len(img_list))
    os.system('mv "%s/" "%s/"'%(inittime, title))

    print '\n7z a "%s.zip" "%s/"\n'%(title, title)

    os.system('7z a "%s.zip" "%s/"'%(title, title))
    print "File zip archiving completed."
    os.system('rm -r "%s/"'%(title))
    print "Temporal folder erased."
    print "Done!"


def get_html_content(url):
    global img_list
    req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
    content = urllib2.urlopen(req)
    soup = bs4.BeautifulSoup(content)
    

    print "Received a HTML content from %s" %(url)
    img_link = soup.findAll('img')[4].get('src')
    img_list.append(img_link)
    print "Image url added from %s" %(img_link)
    
    for link in soup.find_all('a'):
        try:
            check = link.find_all('img')[0].get('src')
        except:
            pass
        else:
            if link.find_all('img')[0].get('src') == 'http://ehgt.org/g/n.png':
    		    if link.get('href') != url:
                        get_html_content(link.get('href'))
    		    else:
                        print "End of gallery:%s"%url
                        download_images(get_title(target))
                        print("--- %s seconds elapsed---" %(time.time() - start_time))
                        exit()
            else:
                pass
start_time = time.time()
get_html_content(target)
