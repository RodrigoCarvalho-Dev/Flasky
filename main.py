from flask import Flask, render_template
from flask_bootstrap import Bootstrap as Style


app = Flask(__name__)
bootstrap = Style(app)

@app.route('/')
def main():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    return (
        render_template('404.html'), error == 404
        )

@app.errorhandler(500)
def server_error(error):
    return (
        render_template('500.html') , error == 500 
    )

@app.route('/about')
def about():
    
    return render_template('about.html')

@app.route('/user/<username>')
def user(username):
    return (
        render_template('user.html', name = username)
    )
        
if __name__ == '__main__':

    app.run( debug=True , port = 3000)