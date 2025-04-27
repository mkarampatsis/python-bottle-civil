from bottle import route, run, template

@route('/hello/<name>')
def get_hello(name):
  return template('<b>Hello {{name}}</b>!', name=name)
# http://127.0.0.1:8080/hello/markos

@route('/schools')
def get_schools():
  schools = ['Civil', 'Mech', 'Electrical', 'Arch']
  html = '<ul>'
  for school in schools:
    html += '<li>' + school + '</li>'
  html += '</ul>'
  return html

@route('/file2/<name>')
def show_template(name):
  university = 'NTUA'
  schools = ['Civil', 'Mech', 'Electrical', 'Arch']
  return template('file2.html', name=name, school='civil', university=university, schools=schools)
# http://127.0.0.1:8080/hello/markos

run(host='localhost', port=8080)