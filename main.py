  
from flask import Flask, render_template, url_for, request, redirect 


app = Flask(__name__)

def home():
    return render_template("")


if __name__ == "__main__":
    app.run(debug=True)