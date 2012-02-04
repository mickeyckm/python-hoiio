A python module for using Hoiio REST API.

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

account = "ACXXXXXXXXXXXXXXXXX"
token = "YYYYYYYYYYYYYYYYYY"
client = HoiioRestClient(account, token)
```

