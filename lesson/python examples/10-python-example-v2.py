from pathlib import Path
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
from bottle import route, run, static_file

# @route("/static/<fn>")
# def server_files(fn):
#   "The static files are in current directory."
#   return static_file(fn, root=str(Path.cwd()))

@route('/')
def showMoments():
  "Make and show table and diagram of beam reinforcement."
  mu = np.arange(0, 0.36, 0.01)
  w = 0.84*(1-np.sqrt(1-2.4*mu))
  matplotlib.rc('font', family='serif')
  plt.figure()
  plt.plot(mu, w)
  plt.xlabel("Ανηγμένη ροπή")
  plt.ylabel("Ποσοστό οπλισμού")
  plt.savefig("temp.jpg")
  html = []
  html.append("<html>")
  html.append("<head><title>Οπλισμός δοκού</title></head>")
  html.append("<body>")
  html.append("""<table border=2 align="left">""")
  html.append("<tr>")
  html.append("<td>")
  html.extend(table_numbers(mu, w))
  html.append("</td>")
  html.append("<td>")
  html.append("""<img src="/static/temp.jpg" alt="image not found">""")
  html.append("</td>")
  html.append("</tr>")
  html.append("</table>")
  html.append("</body>")
  html.append("</html>")
  html = "\n".join(html)
  print(html)
  return html

def table_numbers(mu, w):
  "Return the table in html format."
  t = []
  t.append("""<table border=1 align="left" style="font-size:0.8em">""")
  t.append("<tr>")
  t.append("<th><div>Ανηγμένη</div><div>ροπή</div></th>")
  t.append("<th><div>Ποσοστό</div><div>οπλισμού</div></th>")
  t.append("</tr>")
  for mu1, w1 in zip(mu, w):
      t.append("<tr>")
      t.append("""<td align="center">{:.3f}</td>"""
          """<td align="center">{:.3f}</th>""".format(mu1, w1))
      t.append("</tr>")
  t.append("</table>")
  return t
  
run(host='localhost', port=8080)

# http://127.0.0.1:8080/