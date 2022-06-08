
from utils.db import db
class TiKtok_user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    #number_flower = db.Column(db.Integer)
    def __init__(self,name):
        self.name = name
        #self.number_flower = number_flower

class Tiktok_user_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titok_user_id = db.Column(db.Integer, db.ForeignKey('Titok_user.id'))
    Video = db.Column(db.String(50))
    #number_liks = db.Column(db.Integer)
    def __init__(self, titok_user_id,video):
        self.titok_user_id = titok_user_id
        self.video = video
        #self.number_liks = number_liks
