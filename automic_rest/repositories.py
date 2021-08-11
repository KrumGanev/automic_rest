import os
import json
from automic_rest import config
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class repositories:
   def __init__(self):
       self.response = None

   def json(self):
       return  json.loads(self.response)

   def text(self):
       return  self.response

   def getRepository(self, **kwargs):
       # Summary: Retrieves repository information for the given client.
       path = config().setArgs('/{client_id}/repositories', **kwargs)
       r = requests.get(
           config().url+path,
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def createRepository(self, **kwargs):
       # Summary: Initializes the repository for the specified client.
       headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
       data = kwargs.get('data',"{}")
       path = config().setArgs('/{client_id}/repositories', **kwargs)
       r = requests.post(
           config().url+path,
           headers=headers,
           data=json.dumps(data),
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def listBranches(self, **kwargs):
       # Summary: Retrieves a list of branches.
       path = config().setArgs('/{client_id}/repositories/branches', **kwargs)
       r = requests.get(
           config().url+path,
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def createBranch(self, **kwargs):
       # Summary: Create a new branch.
       headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
       data = kwargs.get('data',"{}")
       path = config().setArgs('/{client_id}/repositories/branches', **kwargs)
       r = requests.post(
           config().url+path,
           headers=headers,
           data=json.dumps(data),
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def branchDiff(self, **kwargs):
       # Summary: Get content of two files to see their differences.
       path = config().setArgs('/{client_id}/repositories/branches/{branch_name}/diff', **kwargs)
       r = requests.get(
           config().url+path,
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def branchLog(self, **kwargs):
       # Summary: Retrieves the history of the repository for max_results entries.
       path = config().setArgs('/{client_id}/repositories/branches/{branch_name}/log', **kwargs)
       r = requests.get(
           config().url+path,
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def getChanges(self, **kwargs):
       # Summary: Returns a list of objects that have uncommitted changes.
       path = config().setArgs('/{client_id}/repositories/changes', **kwargs)
       r = requests.get(
           config().url+path,
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def commitChanges(self, **kwargs):
       # Summary: Commits only changed objects for client to repository.
       headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
       data = kwargs.get('data',"{}")
       path = config().setArgs('/{client_id}/repositories/commits', **kwargs)
       r = requests.post(
           config().url+path,
           headers=headers,
           data=json.dumps(data),
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def moveHead(self, **kwargs):
       # Summary: Imports version of provided GIT Hash to automation engine.
       headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
       data = kwargs.get('data',"{}")
       path = config().setArgs('/{client_id}/repositories/commits/{commit_id}', **kwargs)
       r = requests.post(
           config().url+path,
           headers=headers,
           data=json.dumps(data),
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def mergeBranchIntoActive(self, **kwargs):
       # Summary: Merge another branch in active branch.
       headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
       data = kwargs.get('data',"{}")
       path = config().setArgs('/{client_id}/repositories/merge', **kwargs)
       r = requests.post(
           config().url+path,
           headers=headers,
           data=json.dumps(data),
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def delete(self, **kwargs):
       # Summary: Abort merging so we get out of merging state.
       path = config().setArgs('/{client_id}/repositories/merge', **kwargs)
       r = requests.delete(
           config().url+path,
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

   def pull(self, **kwargs):
       # Summary: Pull changes from repository for active branch.
       headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
       data = kwargs.get('data',"{}")
       path = config().setArgs('/{client_id}/repositories/pull', **kwargs)
       r = requests.post(
           config().url+path,
           headers=headers,
           data=json.dumps(data),
           auth=(config().userid, config().password),
           verify=config().sslverify
       )

       self.response = r.text
       return self

