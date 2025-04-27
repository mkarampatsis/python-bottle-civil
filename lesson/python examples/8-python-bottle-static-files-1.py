from bottle import get, run, template, static_file, debug

@get('/')
def index(name='World'):
  # return "I/O I/O it's off to hack we go"
  return template('file1.html')

@get('/static/<filename:path>')
def get_static(filename):
  print(filename)
  return static_file(filename, root='static')

debug(mode=True)
run(host='localhost', port=8080, reloader=True)