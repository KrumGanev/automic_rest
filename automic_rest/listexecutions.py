import os
import json
from automic_rest import config
import requests
from requests.exceptions import HTTPError
from requests.exceptions import Timeout
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)




class listExecutions:
   def __init__(self, client_id:int=0, query=None):
       # Summary: List executions, ordered descending by activation_time and run_id.
       self.response = None 
       self.body = None 
       self.url = None 
       self.headers = None 
       self.content = None 
       self.text = None 
       self.status = None 
       self.path = config().setArgs('/{client_id}/executions', locals())
       if query != None:
            self.query = '?'+query
       else:
            self.query = ''

       self.request() 

   def request(self): 
       try: 
            r = requests.get(
                config().url+self.path+self.query, 
                auth=(config().userid, config().password), 
                verify=config().sslverify, 
                timeout=config().timeout 
            ) 
            # request body  
            self.body = r.request.body 
            # request url 
            self.url = r.request.url 
            # response headers 
            self.headers = r.headers 
            # raw bytes 
            self.content = r.content 
            # converts bytes to string 
            self.text = r.text 
            # convert raw bytes to json_dict 
            self.response = r.json() 
            # http status_code 
            self.status = r.status_code 
            # If the response was successful, no Exception will be raised 
            r.raise_for_status() 
       except HTTPError as http_err: 
            print(f'HTTP error occurred: {http_err}')  # Python 3.6 
       except Exception as err: 
            print(f'Other error occurred: {err}')  # Python 3.6 
       except Timeout: 
            print('The request timed out') 
       else: 
            pass 
 
       
       return  self 
