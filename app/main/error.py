# use @main.app_errothandler(error code) for application wide error handling
from flask import render_template 
from . import main # import blueprint instance main & use it to define our decorator

@main.app_errorhandler(404)
def four_Ow_four(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('fourOwfour.html'),404