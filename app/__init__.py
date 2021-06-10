from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES #upload set defines the type of file we are uploading Image
from flask_mail import Mail
from flask_simplemde import SimpleMDE # help create simple markdown editor to write our review in markdown


login_manager = LoginManager() # instance of LoginManager
login_manager.session_protection = 'strong' # provides different security level
login_manager.login_view = 'auth.login' #We prefix the login endpoint with the blueprint name because it is located inside a blueprint.


photos = UploadSet('photos', IMAGES)
bootstrap = Bootstrap()
db = SQLAlchemy()
mail =  Mail()
simple = SimpleMDE()

def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    
    # Initializing flask extensions
    bootstrap.init_app(app) # bootstrap
    db.init_app(app) # for db
    login_manager.init_app(app) # for login
    mail.init_app(app)
    simple.init_app(app)

    # Will add the views and forms

    # register blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix= '/authenticate') # will add a prefix to all routers that folloe the routes eg 'localhost:5000/authenticate/login'

    # setting config
    from .request import configure_request
    configure_request(app)

    # configure Uploadset
    configure_uploads(app,photos)

    return app
    