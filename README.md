# FaceCircle-processing
Renders a video with Circling Faces of colleagues

<img src="example.gif" width="250"/>

<hr>

# Components:

## Processing sketch
### [face_circle.pyde](face_circle.pyde)
- Calls `scripts/get_meeting_attendees.sh` script to get a meetings attendees
- Filters list of images in `images/` directory that match the meeting attendees
- Renders the visuals
- Outputs frames to `frames/` directory

## Scripts
### [scripts/generate_video.sh](scripts/generate_video.sh)
- If called without args it lists next meetings
```
0: 2020-07-22T10:30:00+02:00 This meeting should have been an email
1: 2020-07-22T13:00:00+02:00 Daily standup
2: 2020-07-22T14:00:00+02:00 Knowledgeshare
3: 2020-07-22T15:00:00+02:00 Planning
4: 2020-07-23T11:00:00+02:00 This meeting should have been an email
```
- If called with a chosen meeting number (`generate_video.sh 1`), it:
  - Runs the Processing sketch to generate the frames
  - Uses `ffmpeg` to assemle them to video2
  
### [scripts/next_meetings.py](scripts/next_meetings.py)
- Uses Google Calendar API to download meeting and attendee list
- Assumes that `credentials.json` is available in project root, see https://developers.google.com/calendar/quickstart/python
