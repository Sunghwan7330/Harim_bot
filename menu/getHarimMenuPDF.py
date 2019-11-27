#!/usr/bin/python
# -*- encoding: utf-8 -*-
import urllib2
import sys, urllib as ul
import os
from requests import get  # to make GET request


g_szMenuURL="http://pvv.co.kr/bbs/index.php?code=bbs_menu01"
szLastFileCache="cache.dat"

szPDF_URL=""
szUTF8_Name=""
PDF_FILE_NAME="menu_pdf.pdf"
TXT_FILE_NAME="menu_text.pdf"

def download(url, file_name):
  with open(file_name, "wb") as file:   # open in binary mode
    response = get(url)               # get request
    file.write(response.content)      # write to file


def CheckLastFile(szFileName):
  global szLastFileCache
  try:
    f = open(szLastFileCache, "r")
    szOldFileName=f.read()
    f.close()
    if ( szFileName == szOldFileName ):
      return 0
  except:
    pass
  f = open(szLastFileCache, "w")
  f.write(szFileName)
  f.close()
  return 1

response = urllib2.urlopen(g_szMenuURL)
html = response.read()
response.close()

for curLine in html.split('\n'):
  if curLine.find("filename=") > 0:
     szTmpURL=curLine.split("href='")[1].split("'>")[0]
     szNEWURL_ARR=szTmpURL.split("&filename=")
     szUTF8_Name=szNEWURL_ARR[1].decode('cp949')
     szNEWURL="bbs/%s&filename=%s" % ( szNEWURL_ARR[0], ul.quote_plus(szNEWURL_ARR[1]))
     szPDF_URL="http://pvv.co.kr/%s" % ( szNEWURL )
     print szPDF_URL
     break

if len(szPDF_URL) > 0 :
  response = urllib2.urlopen(szPDF_URL)
  html = response.read()
#  print html
  if ( CheckLastFile(szPDF_URL) ):
    print ("get menu")
    download(szPDF_URL, PDF_FILE_NAME)
    command = "pdftotext {} {}".format(PDF_FILE_NAME, TXT_FILE_NAME)
    os.system(command);
