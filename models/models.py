from utils.db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    number_subscriptions = db.Column(db.Integer)
    number_subscribers = db.Column(db.Integer)
    number_like = db.Column(db.Integer)

    def __init__(self,name, number_subscriptions,number_subscribers,number_like):
        self.name = name
        self.number_subscriptions = number_subscriptions
        self.number_subscribers = number_subscribers
        self.number_like = number_like 
       
class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer)
    video_desc = db.Column(db.String(100))
    video_length = db.Column(db.Integer)
    video_link = db.Column(db.String(100))
    video_nb_shares = db.Column(db.Integer)
    video_nb_likes = db.Column(db.Integer)
    video_nb_comments = db.Column(db.Integer)

    def __init__(self,id_user,video_desc,video_length,video_link,video_nb_shares,video_nb_likes,video_nb_comments):
        self.id_user = id_user
        self.video_desc = video_desc
        self.video_length = video_length
        self.video_link = video_link
        self.video_nb_shares = video_nb_shares
        self.video_nb_likes = video_nb_likes
        self.video_nb_comments = video_nb_comments

