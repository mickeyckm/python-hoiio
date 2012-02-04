from hoiio.rest.resources import Resource

class Account(Resource):

    name = 'user'
    
    def get_balance(self, params={}):
        cleaned_params = self.sanitize(params)
        method_uri = self.get_method_uri('get_balance')
        return self.request(method='get', uri=method_uri, data=cleaned_params)
        
    def get_info(self, params={}):
        cleaned_params = self.sanitize(params)
        method_uri = self.get_method_uri('get_info')
        return self.request(method='get', uri=method_uri, data=cleaned_params)