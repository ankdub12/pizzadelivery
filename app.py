#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res =   (res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    return {
        "speech": "pizza is on its way",
        "displayText": "pizza is on its way",
        #"data": {},
        # "contextOut": [],
        "source": "test"
    }
    if req.get("result").get("action") != "order.pizza":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    topping = parameters.get("topping")
    typeofpizza = parameters.get("type")
    size = parameters.get("size")
    time = parameters.get("time")
    address = parameters.get("address")
    speech = " All set enjoy your " + size + typeofpizza + " pizza with " + topping + " will be delivered at " + time + address
    print("Response: ")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "apiai-pizzadelivery-sample"
    }

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print "Starting app on port %d" % port
    app.run(debug=True, port=port, host='0.0.0.0')
