# Merge Queue Testing for Apache Kafka


The purpose of this repository is to evaluate Github's merge queue feature
in the context of an Apache project. 

See https://issues.apache.org/jira/browse/LEGAL-599 for additional context.

# Testing with live GitHub events

Follow the instructions here to install `smee`: https://docs.github.com/en/webhooks/testing-and-troubleshooting-webhooks/testing-webhooks

We need a Python virtualenv for running a local server.
```
python3 -m venv venv
source venv/bin/activate
```

Download the quart framework https://github.com/apache/infrastructure-asfquart/ and install it
into the virtualenv we just made.


Now, we can start the SMEE client to start receiving events from GitHub.
```
smee -u https://smee.io/wfaiAis5XU4SHXrC -t http://localhost:3000/webhook
```

This will receive events from the SMEE proxy which this repository is sending its webhooks to. 
The events will be forwarded to a local server listening on 3000

Start the Python webhook receiver on 3000 to receive the forwarded events.
```
python webhook-receiver.py
```

Generate some events in this repository (open pull request, merge pull request, etc)

# Testing with sample GitHub events

Three event payloads are included in this repo. This can be used to simulate webhooks
coming from GitHub.

```
curl -X POST http://localhost:3000/webhook \
     -H "Content-Type: application/json" \
     -H "X-Github-Event: pull_request" \
     --data-binary "@webhook-payloads/pull_request_dequeued.json"
```

The three JSON payloads located in webhook-payloads require a cooresponding `X-Github-Event` header.

* pull_request_dequeued: `X-Github-Event: pull_request`
* pull_request_enqueued: `X-Github-Event: pull_request`
* merge_group: `X-Github-Event: merge_group`
