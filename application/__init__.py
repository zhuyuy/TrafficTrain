from flask import Flask
from config import Config

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='')
app.config.from_object(Config)

from application import routes
