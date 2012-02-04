from hoiio.rest.resources import Resource

class IVR(Resource):

    name = 'ivr'
    
    # Start
    
    def dial(self, params={}):
        cleaned_params = self.sanitize(params)
        method_uri = self.get_method_uri('start/dial')
        return self.request(method='get', uri=method_uri, data=cleaned_params)
    
    # Middle
        
    def play(self, params={}):
        cleaned_params = self.sanitize(params)
        method_uri = self.get_method_uri('middle/play')
        return self.request(method='get', uri=method_uri, data=cleaned_params)

    def gather(self, params={}):
        cleaned_params = self.sanitize(params)
        method_uri = self.get_method_uri('middle/gather')
        return self.request(method='get', uri=method_uri, data=cleaned_params)
        
    def record(self, params={}):
        cleaned_params = self.sanitize(params)
        method_uri = self.get_method_uri('middle/record')
        return self.request(method='get', uri=method_uri, data=cleaned_params)
        
    # End
    
    def transfer(self, params={}):
        cleaned_params = self.sanitize(params)
        method_uri = self.get_method_uri('end/transfer')
        return self.request(method='get', uri=method_uri, data=cleaned_params)
        
    def hangup(self, params={}):
        cleaned_params = self.sanitize(params)
        method_uri = self.get_method_uri('end/hangup')
        return self.request(method='get', uri=method_uri, data=cleaned_params)