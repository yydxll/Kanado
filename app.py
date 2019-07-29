import time
def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)
    return [('==HELLO from a simple WSGI application!--->%s\n' % time.ctime()).encode(' utf-8')]

