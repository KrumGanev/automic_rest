import os
import json
from automic_rest import config
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class system:
   def __init__(self):
       self.response = None

   def json(self):
       return  json.loads(self.response)

   def text(self):
       return  self.response

   def listAgentgroups(self, **kwargs):
       # Summary: 
       path = config().setArgs('/{client_id}/system/agentgroups', **kwargs)
       r = requests.get(
           config().url+path,
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def listAgents(self, **kwargs):
       # Summary: Lists all agents that are defined in the system. The returned list contains running and stopped agents.
       path = config().setArgs('/{client_id}/system/agents', **kwargs)
       r = requests.get(
           config().url+path,
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def getAgentDetails(self, **kwargs):
       # Summary: Returns detailed agent information
       path = config().setArgs('/{client_id}/system/agents/{object_name}', **kwargs)
       r = requests.get(
           config().url+path,
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def listClients(self, **kwargs):
       # Summary: List of clients in the system.
       path = config().setArgs('/{client_id}/system/clients', **kwargs)
       r = requests.get(
           config().url+path,
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def deleteClients(self, **kwargs):
       # Summary: Delete a client
       path = config().setArgs('/{client_id}/system/clients/{client_id}', **kwargs)
       r = requests.delete(
           config().url+path,
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def getFeatureList(self, **kwargs):
       # Summary: Retrieve system feature information.
       path = config().setArgs('/{client_id}/system/features', **kwargs)
       r = requests.get(
           config().url+path,
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def healthCheck(self, **kwargs):
       # Summary: Can be used to determine if the automation system is in a healthy state. A system is healthy if there is a PWP and at least one instance of CP and JWP respectively. When healthy, HTTP 200 is returned. When unhealthy, HTTP 503. Note: only use the HTTP status code to determine the health status since the response body is optional.
       path = config().setArgs('/{client_id}/system/health', **kwargs)
       r = requests.get(
           config().url+path,
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

