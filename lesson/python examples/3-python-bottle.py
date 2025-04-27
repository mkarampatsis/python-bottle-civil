from bottle import route, run

@route('/hello/world')
def index():
  return 'Hello world!'

run(host='localhost', port=8080)

# http://127.0.0.1:8080/hello/world