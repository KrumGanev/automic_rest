import os
import json
from automic_rest import config
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class objects:
   def __init__(self):
       self.response = None

   def json(self):
       return  json.loads(self.response)

   def text(self):
       return  self.response

   def postObjects(self, **kwargs):
       # Summary: Can be used to import single objects
       headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
       data = kwargs.get('data',"{}")
       path = config().setArgs('/{client_id}/objects', **kwargs)
       r = requests.post(
           config().url+path,
           headers=headers,
           data=json.dumps(data),
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def getObjects(self, **kwargs):
       # Summary: Can be used to export single objects by name
       path = config().setArgs('/{client_id}/objects/{object_name}', **kwargs)
       r = requests.get(
           config().url+path,
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def listObjectInputs(self, **kwargs):
       # Summary: List all inputs for a given object.
       path = config().setArgs('/{client_id}/objects/{object_name}/inputs', **kwargs)
       r = requests.get(
           config().url+path,
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def getTimezoneInfo(self, **kwargs):
       # Summary: Returns the time zone used by an object definition or defaults if the object or time zone does not exist.
       path = config().setArgs('/{client_id}/objects/{object_name}/timezone', **kwargs)
       r = requests.get(
           config().url+path,
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def usage(self, **kwargs):
       # Summary: Returns a list of objects with a reference name, a boolean to show if the actual result has hidden objects due to acl conflicts, for the given objectname
       path = config().setArgs('/{client_id}/objects/{object_name}/usage', **kwargs)
       r = requests.get(
           config().url+path,
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def usageForCalendarEvents(self, **kwargs):
       # Summary: Returns a list of objects with a reference name, a boolean to show if the actual result has hidden objects due to acl conflicts, for the given objectname
       path = config().setArgs('/{client_id}/objects/{object_name}/usage/calendarevent/{event_name}', **kwargs)
       r = requests.get(
           config().url+path,
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

