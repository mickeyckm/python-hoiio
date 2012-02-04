# Python-Hoiio

A python module for using Hoiio REST API.

## Requirements

* Python >= 2.6

## Installation

Install from PyPi using pip, a package manager for Python.

```terminal    
$ pip install python-hoiio
```   
   
you can [download the source code (ZIP)](https://github.com/mickeyckm/python-hoiio/zipball/master "python-hoiio source code") for `python-hoiio`, and then run:

```terminal
$ python setup.py install
```

You may need to run the above commands with `sudo`.

## Getting Started

Getting started with the Hoiio API couldn't be easier. Create a HoiioRestClient and you're ready to go.

### API Credential

The HoiioRestClient needs your Hoiio credentials. You can either pass these directly to the constructor (see the code below) or via environment variables.

```python
from hoiio.rest import HoiioRestClient

appId = 'YOUR_APP_ID_HERE'
token = 'YOUR_TOKEN_HERE'
client = HoiioRestClient(appId, token)
```

### Make a call

```python
from hoiio.rest import HoiioRestClient

appId = 'YOUR_APP_ID_HERE'
token = 'YOUR_TOKEN_HERE'
client = HoiioRestClient(appId, token)

resp = client.voice.call(dest='+6512345678', dest2='+6554326547', caller_id='Hoiio')
```


### Send a sms

```python
from hoiio.rest import HoiioRestClient

appId = 'YOUR_APP_ID_HERE'
token = 'YOUR_TOKEN_HERE'
client = HoiioRestClient(appId, token)

resp = client.sms.send(dest='+6565123476', message='Hello World')
```

### Subcribe a number

```python
from hoiio.rest import HoiioRestClient

appId = 'YOUR_APP_ID_HERE'
token = 'YOUR_TOKEN_HERE'
client = HoiioRestClient(appId, token)

resp = client.number.subscribe(number='+6567589405', duration=60)
```

### Get account balance

```python
from hoiio.rest import HoiioRestClient

appId = 'YOUR_APP_ID_HERE'
token = 'YOUR_TOKEN_HERE'
client = HoiioRestClient(appId, token)

resp = client.account.balance()
```

## License

This project is under [MIT License](http://en.wikipedia.org/wiki/MIT_License).
See LICENSE file for details.




