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
    data['token'] = 'xoxb-305601000482-EagaR9CZuvKS2IxdMvteXxUW'
    # data['file'] = path
    data['filename'] = "Guest"
    data['channels'] = 'C8ZHL73RS'
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
