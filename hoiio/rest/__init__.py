from hoiio.exceptions import HoiioException

from hoiio.rest.resources import Account
from hoiio.rest.resources import IVR
from hoiio.rest.resources import Number
from hoiio.rest.resources import SMS
from hoiio.rest.resources import Voice

class HoiioRestClient(object):

    def __init__(self, appid=None, token=None):
            
        if not appid or not token:
            raise HoiioException("""
                Hoiio could not find your application credentials. Pass them into HoiioRestClient constructor like this:
                
                    client = HoiioRestClient(appid='TnsL1P6ggsZGIsNW', token='MmwkKinHK47brUwc') 
                """)
                
        api_uri = 'https://secure.hoiio.com/open'
        auth = { 'app_id': appid, 'access_token': token }  
                
        self.account = Account(api_uri, auth)
        self.ivr = IVR(api_uri, auth)
        self.number = Number(api_uri, auth)        
        self.sms = SMS(api_uri, auth)
        self.voice = Voice(api_uri, auth)
        
        self.api_uri = api_uri
        self.auth = auth