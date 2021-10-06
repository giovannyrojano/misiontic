from flask import Flask  

#main = blueprints.Blueprint('main',__name__)


#@main.route('/')
#def index():
# return render_template('index.html')

def create_app():
    app = Flask(__name__)

    from views import main
    app.register_blueprint(main)
    

    return app