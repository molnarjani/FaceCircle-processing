#!/bin/bash
WORKDIR="$(dirname $0)/.."
cd "$WORKDIR"
if [ $# -eq 0 ]
  then
    python scripts/next_meetings.py
else
  # The processing sketch will access meeting which meeting to use from ENV	
  export MEETING_NUMBER_CHOICE=$1

  # Remove previous frames
  rm -rf frames/*

  # Generate new frames
  /Library/Java/JavaVirtualMachines/jdk1.8.0_202.jdk/Contents/Home/bin/java -jar deps/processing-py.jar face_circle.pyde
  
  # Assemble frames to a video
  ffmpeg -framerate 30 -pattern_type glob -i 'frames/*.png' -y -c:v libx264 -r 30 -pix_fmt yuv420p out.mp4
fi
