import os
import json
from automic_rest import config
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class executions:
   def __init__(self):
       self.response = None

   def json(self):
       return  json.loads(self.response)

   def text(self):
       return  self.response

   def listExecutions(self, **kwargs):
       # Summary: List executions, ordered descending by activation_time and run_id.
       path = config().setArgs('/{client_id}/executions', **kwargs)
       r = requests.get(
           config().url+path,
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def executeObject(self, **kwargs):
       # Summary: Execute an object with or without input parameters (promptsets variables).
       headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
       data = kwargs.get('data',"{}")
       path = config().setArgs('/{client_id}/executions', **kwargs)
       r = requests.post(
           config().url+path,
           headers=headers,
           data=json.dumps(data),
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def getExecution(self, **kwargs):
       # Summary: Get details of a given execution.
       path = config().setArgs('/{client_id}/executions/{run_id}', **kwargs)
       r = requests.get(
           config().url+path,
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def getChildrenOfExecution(self, **kwargs):
       # Summary: Gets all immediate execution children, ordered descending by activation_time and run_id.
       path = config().setArgs('/{client_id}/executions/{run_id}/children', **kwargs)
       r = requests.get(
           config().url+path,
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def listComments(self, **kwargs):
       # Summary: List all comments for a given execution.
       path = config().setArgs('/{client_id}/executions/{run_id}/comments', **kwargs)
       r = requests.get(
           config().url+path,
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def createComments(self, **kwargs):
       # Summary: Appends a comment to a given execution.
       headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
       data = kwargs.get('data',"{}")
       path = config().setArgs('/{client_id}/executions/{run_id}/comments', **kwargs)
       r = requests.post(
           config().url+path,
           headers=headers,
           data=json.dumps(data),
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def computeErtEstimations(self, **kwargs):
       # Summary: Get ERT estimations for the given workflow.
       path = config().setArgs('/{client_id}/executions/{run_id}/ert', **kwargs)
       r = requests.get(
           config().url+path,
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def listReports(self, **kwargs):
       # Summary: Report list for a given execution.
       path = config().setArgs('/{client_id}/executions/{run_id}/reports', **kwargs)
       r = requests.get(
           config().url+path,
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def listReportContent(self, **kwargs):
       # Summary: Report content pages.
       path = config().setArgs('/{client_id}/executions/{run_id}/reports/{report_type}', **kwargs)
       r = requests.get(
           config().url+path,
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def changeExecutionStatus(self, **kwargs):
       # Summary: Changes the status of an execution.
       headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
       data = kwargs.get('data',"{}")
       path = config().setArgs('/{client_id}/executions/{run_id}/status', **kwargs)
       r = requests.post(
           config().url+path,
           headers=headers,
           data=json.dumps(data),
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def listVariables(self, **kwargs):
       # Summary: List all variables for a given execution.
       path = config().setArgs('/{client_id}/executions/{run_id}/variables', **kwargs)
       r = requests.get(
           config().url+path,
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

