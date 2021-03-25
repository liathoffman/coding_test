# Script below constantly tries to request a webpage.
# If status is not good, sends an alert to slack.

import os
from slack_sdk.webhook import WebhookClient

url = "https://hooks.slack.com/services/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"

while True:
    hostname = "google.com" #example
    response = os.system("ping -c 1 " + hostname)

    #and then check the response... if its down send an alert to slack
    if response == 0:
        print(hostname + ' is up!')
    else:
        webhook = WebhookClient(url)
        response = webhook.send(text=hostname + " is down!")
        assert response.status_code == 200
        assert response.body == "ok"
        print(hostname + ' is down!')
