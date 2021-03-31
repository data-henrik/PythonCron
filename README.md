# Sample dispatch action in IBM Cloud Functions / OpenWhisk

The file [dispatch.py](dispatch.py) implements a small dispatcher to demonstrate cron-like scheduling. It checks the passed in arguments for a known job ID. If found it sets up the request, calls out to the provided URI and passes the provided payload. It returns with details about the processed request.

It uses the deployed [Twitter Bot](https://github.com/data-henrik/twitterBot/tree/feed) as target. The request and its payload cause a new Twitter status update (tweet) to be generated.

### IBM Cloud Functions setup

```
ibmcloud fn namespace target bot
```

```
ibmcloud fn action update dispatch dispatch.py --kind python:default
```

```
ibmcloud fn trigger create cf_tweety --feed /whisk.system/alarms/alarm --param cron "22 10 * * *" --param trigger_payload '{"CE_TWEET": { "url":"https://twitterbot.7aervajuhho.us-south.codeengine.appdomain.cloud/tweet", "payload":{"secret_key":"LET_ME_TWEET","tweet_string2":"Triggered by #OpenWhisk and dispatched in #Python on #IBMCloud" }}}'
```

```
ibmcloud fn rule create myTweetRule cf_tweety dispatch
```

