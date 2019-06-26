#!/usr/bin/env python

import time
import json
import automationhat

from flask import Flask, jsonify, make_response, request


app = Flask(__name__)

def switchOn() :
	if automationhat.is_automation_hat():
		automationhat.relay.one.on()
		return True
	else:
		return False

def switchOff() :
	if automationhat.is_automation_hat():
		automationhat.relay.one.off()
		return True
	else:
		return False

def getStatus() :
	if automationhat.relay.one.is_on():
		return True
	else:
		return False

@app.route('/api/status', methods=['GET'])
def status() :
	return jsonify({'currentState': getStatus() })

@app.route('/api/order', methods=['POST'])
def order() :
	content = request.json
	targetState = content.get('targetState', '')
	print(targetState)
	if targetState == True :
		switchOn()
		print('on')
	else:
		switchOff()
		print('off')
	return jsonify({'currentState': getStatus() })


@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
