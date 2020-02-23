

#import requests
#url = 'http://localhost:5000/predict_api'
#r = requests.post(url,json={'experience':2,'test_score':9,'interview_score':6})
#print(r.json())


import requests
#import json

URL = 'https://www.sms4india.com/api/v1/sendCampaign'

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':"L5086OICDXBP4NECTSQQW7BCRUPTAGR9",
  'secret':"PXJ06I7IDFT0AFH9",
  'usetype':"stage",
  'phone': "7024267076",
  'message':"Hello There !!!! It's an emergency !! BE CAREFUL",
  'senderid':"mihirdutta9@gmail.com"
  }
  return requests.post(reqUrl, req_params)

# get response
response = sendPostRequest(URL, 'provided-api-key', 'provided-secret', 'prod/stage', 'valid-to-mobile', 'active-sender-id', 'message-text' )
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
# print response if you want
print (response.text)