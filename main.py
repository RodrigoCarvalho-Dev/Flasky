from flask import Flask, render_template
from flask_bootstrap import Bootstrap as Style


app = Flask(__name__)
bootstrap = Style(app)

@app.route('/')
def main():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return (
        render_template('404.html'), e==404
        )
        
if __name__ == '__main__':
    app.run( debug=True)