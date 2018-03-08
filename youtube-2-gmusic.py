#!/usr/bin/env python

import sys, os
from gmusicapi import Mobileclient, Musicmanager, Webclient
from subprocess import getoutput

os.chdir('/tmp')

yt_url=sys.argv[1]

# download song
print('Downloading Song..')
output = getoutput('youtube-dl -x --audio-format m4a --audio-quality 0 ' + yt_url)

song_file = [l.replace('[ffmpeg] Destination: ','') for l in output.splitlines() if '[ffmpeg] Destination: ' in l][0]

gm_manager = Musicmanager()
print("Logging in...")
gm_manager.login()

print("Uploading " + song_file)
(uploaded, matched, not_uploaded) = gm_manager.upload([song_file])

if len(uploaded):
  print("Success")
else:
  print("Unsucessful!")
  if len(matched):
    print("Already Exists...")
