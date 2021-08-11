import os
import json
from automic_rest import config
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class scripts:
   def __init__(self):
       self.response = None

   def json(self):
       return  json.loads(self.response)

   def text(self):
       return  self.response

   def activateScript(self, **kwargs):
       # Summary: Runs scripts written in the Automation Engine scripting language.
       headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
       data = kwargs.get('data',"{}")
       path = config().setArgs('/{client_id}/scripts', **kwargs)
       r = requests.post(
           config().url+path,
           headers=headers,
           data=json.dumps(data),
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

