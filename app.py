from flask import Flask
from flask_cors import CORS
# from config import Config
from models import db
from routes import bp

app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Pricila33@@localhost:3306/pruebadb'

CORS(app)
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(bp);
if __name__ =='__main__':
    app.run(debug=True)