import os
import requests

"""Upload file to channel

Note:
    URLs can be constructed from:
    https://api.slack.com/methods/files.upload/test
"""
def sendimage(img):
    path=img
    data = {}
    data['token'] = 'YOUR_SLACK_API_HERE'
    # data['file'] = path
    data['filename'] = "Guest"
    data['channels'] = 'YOUR_CHANNEL_NAME'
    files = {
        'file': (path, open(path, 'rb'), 'image/jpg', {
            'Expires': '0'
        })
    }
    data['media'] = files
    response = requests.post(
        url='https://slack.com/api/files.upload',
        data=data,
        headers={'Accept': 'application/json'},
        files=files)
    os.remove(img)
    print(response.text)
