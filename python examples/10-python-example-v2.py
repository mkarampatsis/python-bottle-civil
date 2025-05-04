from pathlib import Path
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
from bottle import route, run, static_file, template

@route('/static/<filename>')
def server_static(filename):
  return static_file(filename, root='./static')

@route('/')
def show_template():
  mu = np.arange(0, 0.36, 0.01)
  w = 0.84*(1-np.sqrt(1-2.4*mu))
  plt.figure()
  plt.plot(mu, w)
  plt.xlabel("Ανηγμένη ροπή")
  plt.ylabel("Ποσοστό οπλισμού")
  plt.savefig("static/temp.jpg")
  return template('example1.html', muData=mu, wData=w)

run(host='localhost', port=8080)

# http://127.0.0.1:8080/