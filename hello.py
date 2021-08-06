def test (environ,start_response):
    status = "200 OK"
    headers = [
        ('Content-Type','text/plain')
    ]
    start_response(status,headers)
    body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    return iter(body)
    #Ввернуть заголовки, только хз как#

