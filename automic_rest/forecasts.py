import os
import json
from automic_rest import config
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class forecasts:
   def __init__(self):
       self.response = None

   def json(self):
       return  json.loads(self.response)

   def text(self):
       return  self.response

   def listForecasts(self, **kwargs):
       # Summary: List all forecasts, ordered descending by start_time.
       path = config().setArgs('/{client_id}/forecasts', **kwargs)
       r = requests.get(
           config().url+path,
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def createForecast(self, **kwargs):
       # Summary: Create a forecast.
       headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
       data = kwargs.get('data',"{}")
       path = config().setArgs('/{client_id}/forecasts', **kwargs)
       r = requests.post(
           config().url+path,
           headers=headers,
           data=json.dumps(data),
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def deleteForecast(self, **kwargs):
       # Summary: Delete forecasts using ids.
       path = config().setArgs('/{client_id}/forecasts', **kwargs)
       r = requests.delete(
           config().url+path,
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def listForecastAgents(self, **kwargs):
       # Summary: List forecast agents and gaps.
       path = config().setArgs('/{client_id}/forecasts/agents', **kwargs)
       r = requests.get(
           config().url+path,
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def getForecast(self, **kwargs):
       # Summary: Get details of a given forecast.
       path = config().setArgs('/{client_id}/forecasts/{forecast_id}', **kwargs)
       r = requests.get(
           config().url+path,
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def modifyForecast(self, **kwargs):
       # Summary: Changes the title of a forecast item.
       headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
       data = kwargs.get('data',"{}")
       path = config().setArgs('/{client_id}/forecasts/{forecast_id}', **kwargs)
       r = requests.post(
           config().url+path,
           headers=headers,
           data=json.dumps(data),
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

