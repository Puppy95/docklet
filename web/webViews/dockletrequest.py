import requests
import json
from flask import abort, session
from webViews.log import logger


endpoint = "http://0.0.0.0:9000"

class dockletRequest():

    @classmethod
    def post(self, url = '/', data = {}):
        #try:
        data = dict(data)
        data['token'] = session['token']
        logger.info ("Docklet Request: user = %s data = %s, url = %s"%(session['username'], data, url))

        result = requests.post(endpoint + url, data = data).json()
        if (result.get('success', None) == "false" and (result.get('reason', None) == "Unauthorized Action" or result.get('Unauthorized', None) == 'True')):
            abort(401)
        logger.info ("Docklet Response: user = %s result = %s, url = %s"%(session['username'], result, url))
        return result
        #except:
            #abort(500)

    @classmethod
    def unauthorizedpost(self, url = '/', data = None):
        data = dict(data)
        data_log = {'user': data['user']}
        logger.info("Docklet Unauthorized Request: data = %s, url = %s" % (data_log, url))
        result = requests.post(endpoint + url, data = data).json()
        logger.info("Docklet Unauthorized Response: result = %s, url = %s"%(result, url))
        return result
