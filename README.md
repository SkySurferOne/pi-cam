## Pi-cam

Realtime image processing with web application.

# Requirements
To run you have to install this python packages:
- opencv2
- numpy
- flask
- jinja2
- Flask-Mail

# Configuration
To have a mail service available you have to provide valid mail credentials.
To do that create ```config.py``` file in the root folder and write MAIL_USERNAME and MAIL_PASSWORD variable, for example: 
```
MAIL_USERNAME = 'user@mail.com'
MAIL_PASSWORD = 'password'

``` 
Then you have to export environment variable PICAM_CONFIG with path to that file, for example:

```export PICAM_CONFIG=/path/to/config.py```

# How to run?
```python3 main.py -s 192.168.0.20 -p 7000```

```-s``` is optional, as default it starts server on 127.0.0.1

```-p``` is optional, as default it uses port 5000

