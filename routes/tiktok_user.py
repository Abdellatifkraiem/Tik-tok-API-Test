from flask import Blueprint
from utils.db import db
from flask import jsonify
from flask import  request
from models.models import User,Video
import json
tiktok = Blueprint('tiktok',__name__)


def set_user(user):
    with open('Data.json') as mon_fichier:
        data = json.load(mon_fichier)
        number_subscriptions = data["number_subscriptions"]
        number_subscribers = data["number_subscribers"]
        number_like = data["number_like"]
        new_user = User( user,number_subscriptions,number_subscribers,number_like)
        db.session.add(new_user)
        db.session.commit()
        user_data = User.query.filter_by(name=user).first()
        for item in data["videos"]:
                video_desc = item["video_desc"]
                video_length = item["video_length"]
                video_link = item["video_link"]
                video_nb_shares = item["video_nb_shares"]
                video_nb_likes = item["video_nb_likes"]
                video_nb_comments = item["video_nb_comments"]
                new_video = Video(user_data.id,video_desc ,video_length,video_link,video_nb_shares,video_nb_likes,video_nb_comments)
                db.session.add( new_video)
                db.session.commit()
    return "ok"


@tiktok.route('/SetDataUser', methods=['POST'])
def set_all_data():
    data = json.loads(request.data)
    usertiktok = data['tiktok_username']
    try:
        set_user(usertiktok)
        return jsonify ({"success": "true"})
    except Exception as e:
        return jsonify (e)
       
    


@tiktok.route('/GetData/tiktok_users/<user_tiktok>', methods=['GET'])
def get_all_data_user(user_tiktok):
    try:
        user_data = User.query.filter_by(name=user_tiktok).first()
        video_user_data = Video.query.filter_by(id_user=user_data.id).all
        list=[]
        dict_user = {
        'id':user_data.id,
        'name':user_data.name,
        'number_subscriptions' : user_data.number_subscriptions,
        'number_subscribers' :  user_data.number_subscribers,
        'number_like' : user_data.number_like
        
        }
        for item in video_user_data():
            dict={}
            dict["id"]=item.id
            dict["video_desc"] = item.video_desc
            dict["video_length"] = item.video_length
            dict["video_link"] = item.video_link
            dict["video_nb_shares"] = item.video_nb_shares
            dict["video_nb_likes"] = item.video_nb_likes
            dict["video_nb_comments"] = item.video_nb_comments
            list.append(dict)
        dict_user["Videos"] = list
        return  jsonify (dict_user)
    except:
        return  jsonify ("Data Not Found")

    
    
