from pushbullet.pushbullet import PushBullet

apiKey = "YOUR_PUSHBULLET_API"
def notify_neighbor(name):
    p = PushBullet(apiKey)
    devices = p.getDevices()
    print(devices)
    response="Intruder Detected in {}'s Home. Please check.".format(name)
    p.pushNote(devices[0]["iden"], 'Smart Home Manager', response)
def notifyuser():
    p = PushBullet(apiKey)
    devices = p.getDevices()
    print(devices)
    p.pushNote(devices[0]["iden"], 'Smart Home Manager', 'Intruder Detected')
def notifyuser_place(msg):
    p = PushBullet(apiKey)
    devices = p.getDevices()
    print(devices)
    p.pushNote(devices[0]["iden"], 'Smart Home Manager', 'Intruder Detected in {}'.format(msg))