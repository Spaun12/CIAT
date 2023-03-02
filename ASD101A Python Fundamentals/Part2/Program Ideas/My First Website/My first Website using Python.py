#My first Website using Python
from flask import Flask

app = Flask(__name__)

@app.route('/journal')
def journal():
    return 'Welcome to my coding and IT journal!'





