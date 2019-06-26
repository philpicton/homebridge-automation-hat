#!/usr/bin/env python

import time
import json
import automationhat

from flask import Flask, jsonify, make_response, request


app = Flask(__name__)

def switchOn() :
	automationhat.relay.one.on()

def switchOff() :
	automationhat.relay.one.off()

def getStatus() :
	return automationhat.relay.one.is_on()

@app.route('/api/status', methods=['GET'])
def status() :
	return jsonify({'currentState': getStatus() })

@app.route('/api/order', methods=['POST'])
def order() :
	content = request.json
	targetState = content.get('targetState', '')
	if targetState == True :
		switchOn()
	else:
		switchOff()
	return make_response( jsonify({'currentState': getStatus() }) )


@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
