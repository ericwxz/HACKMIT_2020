from flask import Flask, session, request, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')