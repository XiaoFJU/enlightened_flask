import os
from flask import Flask

def create_application(config=None):
    """create a flask application object. and setting the application route."""
    app = Flask(__name__)    
    if config is not None:
        print('mewo')
        app.config.from_object(config)
    # else:
    #     print(os.environ['APP_SETTINGS'])
    #     app.config.from_object(os.environ['APP_SETTINGS'])

    @app.route('/')
    def example():
        """ a example funciton """
        return 'hello world'

    return app
