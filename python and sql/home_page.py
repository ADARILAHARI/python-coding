from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>hi this lahari</title>
    </head>
    </html>'''

if __name__ == '__main__':
    app.run(debug=True)