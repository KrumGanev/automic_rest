import os 
from urllib.parse import urlparse

_userid = None
_password = None
_baseurl = None
_url = None
_sslverify = None
_timeout = None 


class connection(object): 
    def __init__(self, userid="", password="", url="", noproxy=True, sslverify=False, timeout=3600): 
        #self.userid = kwargs.get('userid','') 
        #self.password = kwargs.get('password','') 
        #self.system = kwargs.get('system','').lower() 
        #self.baseurl = kwargs.get('url','')
        #self.noproxy = kwargs.get('noproxy',False)
        #self.sslverify = kwargs.get('sslverify',True)
        #self.timeout = kwargs.get('timeout',3600)
        self.userid     = userid
        if self.userid == "":
            self.userid = _userid
        self.password   = password
        if self.password == "":
            self.password = _password
        self.baseurl    = url
        if self.baseurl == "":
            self.baseurl = _baseurl
        
        self.noproxy    = noproxy
        self.sslverify  = sslverify
        self.timeout    = timeout
        
        self.domain = urlparse(self.baseurl).netloc 
        self.basepath = '/api/v1'
        self.url = self.baseurl+'/ae'+self.basepath 
        if self.noproxy: 
            os.environ['NO_PROXY'] = self.domain 
        
        self.init() 
 
    def init(self): 
        global _userid, _password, _url, _sslverify, _timeout, _baseurl 
        _userid = self.userid 
        _password = self.password 
        _url = self.url 
        _sslverify = self.sslverify
        _timeout = self.timeout
        _baseurl = self.baseurl
 
class config(object): 
    def __init__(self): 
        self.url = _url 
        self.userid = _userid 
        self.password = _password 
        self.sslverify = _sslverify
        self.timeout = _timeout

    def setArgs(self, path, args):
        for key, value in args.items():
            if key != 'self':
                path = path.replace('{'+key+'}', str(value))
        return path

