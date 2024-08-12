import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('mysql+pymysql://root:Pricila33@127.0.0.1:3306/pruebaDB')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
