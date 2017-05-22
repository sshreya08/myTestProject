from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_world(name):
   return 'Hello %s!' %name

@app.route('/blog/<float:blogNum>')  
def show_blog(blogNum):
   return 'Welcome to blog number: %f!' %blogNum
   
@app.route('/rev/<int:revNum>')  
def show_rev(revNum):
   return 'Welcome to rev number: %d!' %revNum
#app.add_url_rule('/', '', hello_world)

if __name__ == '__main__':
   app.run(debug = True)