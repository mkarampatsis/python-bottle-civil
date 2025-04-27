from bottle import route, run

sithlords = ['Darth Bane', 'Darth Maul', 'Darth Vader']

@route('/sithlords/<lord>/append')
def index(lord):
  sithlords.append(lord)
  listoflords = ['<li>' + lord + '</li>' for lord in sithlords ]
  html = 'Famous Sith Lords <br> <ul>' + ''.join(listoflords) + '</ul>'
  return html

run(host='localhost', port=8080)

# http://127.0.0.1:8080/sithlords/Darth%20Cidious/append