from __future__ import print_function
import sys
import json
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

chosen_meeting_number = sys.argv[1] if len(sys.argv) > 1 else None

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('/Users/janosmolnar/Documents/Processing/face_circle/token.pickle'):
        with open('/Users/janosmolnar/Documents/Processing/face_circle/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '/Users/janosmolnar/Documents/Processing/face_circle/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('/Users/janosmolnar/Documents/Processing/face_circle/token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    event_service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    events_result = event_service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for i, event in enumerate(events):
        attendees = []
        if event.get('attendees'):
            attendees = [attendee['email'] for attendee in event['attendees'] if attendee['responseStatus'] != 'declined']
        start = event['start'].get('dateTime', event['start'].get('date'))
        if not chosen_meeting_number:
            print('{}:'.format(i), start, event['summary'])
        else: 
            if i == int(chosen_meeting_number):
                print(attendees)
            

if __name__ == '__main__':
    main()
