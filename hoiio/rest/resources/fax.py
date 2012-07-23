from hoiio.rest.resources import Resource

import base64

class Fax(Resource):

    name = 'fax'
    
    def send(self, params={}):
        cleaned_params = self.sanitize(params)
        method_uri = self.get_method_uri('send')
        print '>>'*20
        return self.request(method='post', uri=method_uri, data=cleaned_params)
    
    def send(self, filename, params={}):
        # Encode the pdf in base64
        f = open(filename, "r")
        data = f.read()
        str_data = base64.b64encode(data)
        params['file'] = str_data

        cleaned_params = self.sanitize(params)
        method_uri = self.get_method_uri('send')
        return self.request(method='post', uri=method_uri, data=cleaned_params)
    
    def get_history(self, params={}):
        cleaned_params = self.sanitize(params)
        method_uri = self.get_method_uri('get_history')
        return self.request(method='get', uri=method_uri, data=cleaned_params)
    
    def get_rate(self, params={}):
        cleaned_params = self.sanitize(params)
        method_uri = self.get_method_uri('get_rate')
        return self.request(method='get', uri=method_uri, data=cleaned_params)
    
    def query_status(self, params={}):
        cleaned_params = self.sanitize(params)
        method_uri = self.get_method_uri('query_status')
        return self.request(method='get', uri=method_uri, data=cleaned_params)
    