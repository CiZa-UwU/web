def test (environ,start_response):
    data =  "\n".join(environ.get('QUERY_STRING').split("&"))
    status = "200 OK"
    response_headers = [
        ('Content-Type','text/plain')
        ('Content-Length', str(len(data)))
    ]
    start_response(status,response_headers)
    return iter ([data.encode('utf-8')])
    #Ввернуть заголовки, только хз как#

