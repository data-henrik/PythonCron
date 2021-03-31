
# IBM Cloud Function action as generic dispatcher
# after being invoked from cron-like scheduler (alarm trigger)
#
# (C) 2021 IBM
# Written by Henrik Loeser, hloeser@de.ibm.com ("data-henrik")

import requests

def main(args):
    # check parameters
    if 'CE_TWEET' in args:
        try:
            url=args['CE_TWEET']['url']
            payload=args['CE_TWEET']['payload']
        except:
            return {"error": "issues with CE_TWEET parameters"}
        try:            
            res=requests.post(url,json=payload)
            return {"message":"success", "res":{"url":url, "payload":payload, "result":res.text}}
        except:
            return {"error": "issues with CE_TWEET request", "payload":payload, "url":url}
    else:
        return {"message":"no known job ID found"}