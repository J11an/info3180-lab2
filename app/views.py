"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, flash
import datetime

def format_date_joined(unformatted_date):


    formatted_date = unformatted_date.strftime("%B, %Y")

    return formatted_date


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/profile')
def profile():

    unformatted_date = datetime.datetime.now()
    date = format_date_joined(unformatted_date)

    name = "James Iverson"
    username = "@jiverson"
    parish, country = "Kingston", "Jamaica"
    bio = "I am smart and talented young man who loves website design and development. Contact me if you'd like to work together on a new project."
    num_posts, num_followers, num_follows = 24,824,248    

    return render_template('profile.html',name=name, username=username, parish=parish, country=country, bio=bio, num_posts=num_posts,num_followers=num_followers, num_follows = num_follows,date_joined=date)



###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
