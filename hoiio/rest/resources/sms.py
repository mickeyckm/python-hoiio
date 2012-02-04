from hoiio.rest.resources import Resource

class SMS(Resource):

    name = 'sms'
    
    def send(self, params={}):
        cleaned_params = self.sanitize(params)
        method_uri = self.get_method_uri('send')
        return self.request(method='get', uri=method_uri, data=cleaned_params)

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