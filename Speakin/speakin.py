import urllib.request
import urllib.error
import urllib.parse
import ssl
import datetime
import hmac
import base64
import hashlib
import json


host = 'service-mu94zm7e-1256142414.ap-guangzhou.apigateway.myqcloud.com'
url = 'https://service-mu94zm7e-1256142414.ap-guangzhou.apigateway.myqcloud.com/release'
path = '/num/vecforregister'
source = 'source'
method = 'POST'
GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'

SecretId = 'AKIDe3Dx8IhdM4og08XK9fF5r6sKs0k2qpyge7bv'
SecretKey = 'c7BwQ3BzlMhAGeQgXI0j3zy4b0Y5sI71y2VJ1U5X'

dateTime = datetime.datetime.utcnow().strftime(GMT_FORMAT)
auth = "hmac id=\"" + SecretId + \
    "\", algorithm=\"hmac-sha1\", headers=\"date source\", signature=\""
signStr = "date: " + dateTime + "\n" + "source: " + source
sign = hmac.new(bytes(SecretKey.encode('utf8')), bytes(signStr.encode('utf8')), hashlib.sha1).digest()
sign = base64.b64encode(sign)
sign = auth + str(sign, encoding='utf8') + "\""

url = url + path


# postData = "{\"file1\": \"e1.wav\", \"file2\": \"e2.wav\", \"file3\": \"e3.wav\"}"

postData = {"file1": "e1.wav", "file2": "e2.wav", "file3": "e3.wav"}
request = urllib.request.Request(
    url, json.dumps(postData).encode('utf8'))

request.add_header('Authorization', sign)
request.add_header('Host', host)
request.add_header('Source', 'source')
request.add_header('Date', dateTime)
request.add_header('Content-Type', 'application/json')
request.add_header('X-Requested-With', 'XMLHttpRequest')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urllib.request.urlopen(request, context=ctx)
content = response.read()
if (content):
    print(str(content, encoding='utf8'))
