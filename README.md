# Python-Hoiio

A python module for using Hoiio REST API.

## Requirements

* Python >= 2.6
* Requests >= 0.10.2 

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

appid = 'YOUR_APPID_HERE'
token = 'YOUR_TOKEN_HERE'
client = HoiioRestClient(appid, token)
```

### Make a call

```python
from hoiio.rest import HoiioRestClient

appid = 'YOUR_APPID_HERE'
token = 'YOUR_TOKEN_HERE'
client = HoiioRestClient(appid, token)

resp = client.voice.call(params={ dest:'+6512345678', dest2:'+6554326547', caller_id:'Mickey Cheong' })
```


### Send a sms

```python
from hoiio.rest import HoiioRestClient

appid = 'YOUR_APPID_HERE'
token = 'YOUR_TOKEN_HERE'
client = HoiioRestClient(appid, token)

resp = client.sms.send({ dest:'+6565123476', message:'Hello, Mickey' })
```

### Subcribe a number

```python
from hoiio.rest import HoiioRestClient

appid = 'YOUR_APPID_HERE'
token = 'YOUR_TOKEN_HERE'
client = HoiioRestClient(appid, token)

resp = client.number.subscribe({ number:'+6567589405', duration:60 })
```

### Get account balance

```python
from hoiio.rest import HoiioRestClient

appid = 'YOUR_APPID_HERE'
token = 'YOUR_TOKEN_HERE'
client = HoiioRestClient(appid, token)

resp = client.account.balance()
```

## License

Copyright (c) Mickey Cheong and individual contributors.
All rights reserved.
 
Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:
 
1. Redistributions of source code must retain the above copyright notice, 
       this list of conditions and the following disclaimer.
    
2. Redistributions in binary form must reproduce the above copyright 
       notice, this list of conditions and the following disclaimer in the
       documentation and/or other materials provided with the distribution.
 
3. Neither the name of python-hoiio nor the names of its contributors
       may be used to endorse or promote products derived from this software
       without specific prior written permission.
 
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.




