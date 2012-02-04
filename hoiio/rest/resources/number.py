from hoiio.rest.resources import Resource

class Number(Resource):

    name = 'number'
    
    def get_choices(self, params={}):
        cleaned_params = self.sanitize(params)
        method_uri = self.get_method_uri('get_choices')
        return self.request(method='get', uri=method_uri, data=cleaned_params)

    def subscribe(self, params={}):
        cleaned_params = self.sanitize(params)
        method_uri = self.get_method_uri('subcribe')
        return self.request(method='get', uri=method_uri, data=cleaned_params)
        
    def get_rates(self, params={}):
        cleaned_params = self.sanitize(params)
        method_uri = self.get_method_uri('get_rates')
        return self.request(method='get', uri=method_uri, data=cleaned_params)
        
    def update_forwarding(self, params={}):
        cleaned_params = self.sanitize(params)
        method_uri = self.get_method_uri('update_forwarding')
        return self.request(method='get', uri=method_uri, data=cleaned_params)
        
    def get_active(self, params={}):
        cleaned_params = self.sanitize(params)
        method_uri = self.get_method_uri('get_active')
        return self.request(method='get', uri=method_uri, data=cleaned_params)