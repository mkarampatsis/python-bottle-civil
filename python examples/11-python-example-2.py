import numpy as np
from bottle import route, run, request

@route('/')
def qerm(lams1=(), ds1=(), U=None, terr=""):
  "Get the data from the user."
  lams = [""]*9
  ds = [""]*9
  n = min(len(lams1), len(lams))
  lams[:n] = lams1[:n]
  n = min(len(ds1), len(ds))
  ds[:n] = ds1[:n]
  html = []
  html.append("<html>")
  html.append("<head><title>Υπολογισμός θερμοπερατότητας</title></head>")
  html.append("<body>")
  html.append("<h2>Υπολογισμός θερμοπερατότητας επιφανειακού στοιχείου</h2>")
  html.append('''<form action="/" method="post">''')
  for i in range(9):
    html.append("<b>Στρώση {:2d}:</b>".format(i+1))
    html.append('''&nbsp αγωγιμότητα (W/(m K)) <input name="lam" type="number" min="0.0001" max="100.0" step="0.0001" value={} />'''.format(lams[i]))
    html.append('''&nbsp πάχος (m) <input name="d"   type="number" min="0.0001" max="100.0" step="0.0001" value={} />'''.format(ds[i]))
    html.append("<br><br>")
  html.append("<br>")
  html.append('''<a href="/"> Καθαρισμός </a> &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp''')
  html.append('''<input value="Υπολογισμός" type="submit" />''')
  html.append("</form>")
  if U is not None:
    html.append('''<font color="darkgreen">Θερμοπερατότητα U={:.3f} W/(m<sup>2</sup> K) </font><br><br>'''.format(U))
  if terr != "":
    html.append('''<font color="darkred">''')
    html.append(terr)
    html.append("<br>Διορθώστε και προσπαθείστε πάλι.</font>")
  html.append("</body>")
  html.append("</html>")
  html = "\n".join(html)
  #print(html)
  return html

@route('/', method="POST")
def calc():
  "Compute the U-value."
  lams = request.forms.getall('lam')
  ds = request.forms.getall('d')
  print(lams)
  print(ds)
  nlams = len(lams)
  while nlams > 0:
    if lams[nlams-1].strip() != "": break
    nlams -= 1
  nds = len(ds)
  while nds > 0:
    if ds[nds-1].strip() != "": break
    nds -= 1
  for i in range(nlams):
    if lams[i].strip() == "":
      return qerm(lams, ds, None, "Δεν δόθηκε η αγωγιμότητα της στρώσης {}.".format(i+1))
    lams[i] = float(lams[i].replace(",", "."))
  for i in range(nds):
    if ds[i].strip() == "":
      return qerm(lams, ds, None, "Δεν δόθηκε το πάχος της στρώσης {}.".format(i+1))
    ds[i] = float(ds[i].replace(",", "."))
  if nds != nlams:
    return qerm(lams, ds, None, "Το πλήθος των αγωγιμοτήτων και των παχών πρέπει να είναι το ίδιο.")
  if nlams == 0:
    return qerm(lams, ds, None, "Δεν δόθηκε καμμία στρώση.")
  s = 0.0
  for i in range(nlams):
    s += ds[i]/lams[i]
  U = 1/s
  return qerm(lams, ds, U, "")

run(host='localhost', port=8080)