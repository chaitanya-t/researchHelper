import os
import sys
import urllib.request
import requests
import pdfkit
from googlesearch import search
counter = 0
result = ''
resultPpt = ''
args = sys.argv[1:]
rootName = sys.argv[1]
result = ''
cwd = os.getcwd()
rootDir = cwd + "/" + str(rootName) + "_research"
pdfPath = rootDir + "/documentsPdf"
if not os.path.isdir(pdfPath):
   os.makedirs(pdfPath)
os.chdir(pdfPath)
for arg in args:
	result += " " + arg + 'filetype:pdf'
for url in search(result, stop=2):
#	pdfkit.from_url(url,"test")
	#pdfName = "pdf" + str(counter)
	filename = url[url.rfind("/")+1:]
	#pdfName = urllib.unquote(s).decode('utf8')
	#headers = "headers={'User-Agent': 'Mozilla/5.0'}"
	#req = url + ',' + headers
	opener = urllib.request.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	urllib.request.install_opener(opener)
	urllib.request.urlretrieve(url, filename)
	print(filename)
	#counter = counter +1
#counter = 0
print("downloading Presentations Now")
for arg in args:
	resultPpt += " " + arg + 'filetype:ppt'
os.chdir(rootDir)
pptPath = rootDir + "/Presentations"
if not os.path.isdir(pptPath):
   os.makedirs(pptPath)
os.chdir(pptPath)
for url in search(resultPpt, stop=2):
##        pdfkit.from_url(url,"test")
#pptName = "ppt" + str(counter)
	filename = url[url.rfind("/")+1:]
	opener = urllib.request.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	urllib.request.install_opener(opener)
	urllib.request.urlretrieve(url, filename)
	print(filename)
#        counter = counter +1
