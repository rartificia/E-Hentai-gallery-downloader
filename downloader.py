import os

list = []

def download():
    global list
    for link in list:
        os.system("python zcrawler.py %s"%(link))
   

while True:
    get = raw_input("Paste url here. 'q' to proceed crawling")
    if get == 'q':
        download()
        exit()
    else:
        list.append(get)
