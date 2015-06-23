# E-Hentai gallery downloader

You can automatically download the images of an E-Hentai gallery.
This program requires the URL of the first image page of the gallery(i.e. the first page of online reading)

Usage: python zcralwer.py url

Dependencies: wget, 7z, python2.7*

Required Python libraies(python2.7*): beautifulsoup4, re
   -- you can download these things with pip. (e.g. pip install beautifulsoup4)


Summary:

1. Collects the URLs of the target gallery.
2. Downloads the images with fetched urls using wget.
3. Archives the images with the title of the gallery.
4. Erases temporal folder.


And with downloader.py, you can download multiple galleries. (but it's very crude. need to be fixed)

currently developing navigator.py to download multiple gallerys with certain tags.



