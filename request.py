from urllib.parse import urlencode
from urllib.request import urlopen, Request

# GET
httpresponse = urlopen('http://www.naver.com?a=20&b=10')
body = httpresponse.read()
print(body)


# post
data = {
    'email': 'jooyg62@gmail.com',
    'password': '1234',
    'name': '서장규'
}
data = urlencode(data).encode('utf-8')
print(data)

request = Request('http://www.example.com', data)
request.add_header('Content_Type', 'text/html')

httpresponse = urlopen(request)
print(httpresponse.read())
