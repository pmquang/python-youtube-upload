#!/usr/bin/python

import subprocess
import sys
import glob, os
import time

title= sys.argv[1] + ": "
#keywords="javascript, javascript tutorial, java training, javascript training, javascript essential, javascript essential training, javascript structure, javascript variable, javascript function, javascript loop, javascript console, javascript event handle, javascript event handling, javascript debug, javascript css, javascript html5, javascript regular expression"
keywords=sys.argv[2]
category=27
description=""
privacyStatus="public"

n = 0

for file in sorted(glob.glob("./%s/*.mp4" % sys.argv[1])):
  n = n + 1
  f=open( "./%s/videofile.txt"  % sys.argv[1],'a+')
  f.write(str(os.path.basename(file)) + "\n")
  f.close()


  f=open("./%s/info.txt" % sys.argv[1])
  subtitle=f.readlines()
  f.close()

  f=open("./%s/videofile.txt"  % sys.argv[1])
  files=f.readlines()
  f.close()

  for x in range(0, n):
    print subtitle[x].strip()
    print files[x].strip()

    try:
      subprocess.call(["./upload_video.py --noauth_local_webserver --file=\"%s/%s\" --title=\"%s\" --keywords=\"%s\" --category=%d --privacyStatus=\"public\"" %  ( sys.argv[1], files[x].strip() ,(title + subtitle[x].strip())[:75], keywords , category  )   ], shell=True)
      time.sleep(30)
    except Exception , e:
      print e
      continue

#try:
#       subprocess.call(["./upload_video.py --file=%s" % courlink], shell=True)
#except:
#       continue
