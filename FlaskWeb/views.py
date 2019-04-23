"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWeb import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    
    return "welcome Azure App"

