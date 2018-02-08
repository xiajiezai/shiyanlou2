from flask import render_template, Flask

app=Flask(__name__)
@app.route('/')
def index():
	return('Hello, shiyanlou')

@app.route('/user/<username>')
def user_index(username):
	return render_template('user_index.html', username=username)
if __name__=='__main__':
	app.run()