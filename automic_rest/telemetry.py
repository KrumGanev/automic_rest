import os
import json
from automic_rest import config
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class telemetry:
   def __init__(self):
       self.response = None

   def json(self):
       return  json.loads(self.response)

   def text(self):
       return  self.response

   def export(self, **kwargs):
       # Summary: Retrieve telemetry data per month as json for the last n months, including the current month. Only works for client 0.
       path = config().setArgs('/{client_id}/telemetry/export/{start_from}', **kwargs)
       r = requests.get(
           config().url+path,
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def productList(self, **kwargs):
       # Summary: Retrieve available products
       path = config().setArgs('/{client_id}/telemetry/products', **kwargs)
       r = requests.get(
           config().url+path,
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

