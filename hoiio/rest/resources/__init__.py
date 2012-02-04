import requests
from urllib import urlencode

class Resource(object):
    """ 
    A REST Resource 
    """
    
    name = 'resource'
    
    def __init__(self, base_uri, auth):
        self.base_uri = base_uri
        self.auth = auth
        
    def request(self, method, uri, data={}):
        data = dict(data.items() + self.auth.items())
        
        if method == 'get':
            resp = requests.get(uri, params=urlencode(data))
        elif method == 'post':
            resp = requests.post(uri, data=data)    
        
        return resp.content
        
    def get_method_uri(self, method):
        return '%s/%s' % (self.uri, method) 
        
    def sanitize(self, params):
        p = {}
        for k,v in params.iteritems():
            if v:
                p[k] = v
        return p
        
    @property
    def uri(self):
        format = (self.base_uri, self.name)
        return '%s/%s' % format
        
        
from .account import Account
from .ivr import IVR
from .number import Number
from .sms import SMS
from .voice import Voice