def application(env, start_response):

    s1 = []
    s2 =  env['QUERY_STRING'].split('&');

    for s in s2:
        s+= '\n'
        s1.append(s.encode('utf-8'))

    start_response('200 OK', [('Content-Type','text/plain')])
    return s1