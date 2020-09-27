from flask import Flask, request

app = Flask(__name__, static_url_path='', static_folder='')

@app.route('/')
def root():
    return app.send_static_file('index.html')
@app.route('/Gallery')
def Gallery():
    return app.send_static_file('Gallery.html')
@app.route('/About')
def About():
    return app.send_static_file('About.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)