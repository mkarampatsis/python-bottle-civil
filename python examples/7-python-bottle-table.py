from bottle import route, run
from random import random

@route('/')
def index():
  array = [[int(random()*10+1) for i in range(15)] for j in range(5)]
  html = '<table border=1>'
  for row in array:
    html += '<tr>'
    for element in row:
      html += '<td align=right>' + str(element) + '</td>'
    html += '</tr>'
  return html
          
run(host='localhost', port=8080)

# http://127.0.0.1:8080/