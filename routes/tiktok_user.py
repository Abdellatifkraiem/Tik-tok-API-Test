from flask import Blueprint
from TikTokApi import TikTokApi
from utils.db import db
from flask import jsonify

tiktok = Blueprint('tiktok',__name__)
TiKtok_user = Blueprint('TiKtok_user',__name__)
Tiktok_user_data = Blueprint('Tiktok_user_data',__name__)
def set_data_tiktok(user):
    try:
        WEB_ID = "verify_khr3jabg_V7ucdslq_Vrw9_4KPb_AJ1b_Ks706M8zIJTq" #s_v_web_id
        with TikTokApi(verifyFp=WEB_ID, use_test_endpoints=True) as api:
            user_video = api.user(username='therock')
            new_user=TiKtok_user(name='therock')
            db.session.add(new_user)
            db.session.commit()
            id_user = TiKtok_user.query.filter_by(name='therock').first()
            for data in user_video.info_full():
                new_Tiktok_user_data=Tiktok_user_data(titok_user_id=id_user.id,video=data)
                db.session.add(new_Tiktok_user_data)
                db.session.commit()
        return "ok"
    except:
        return "Data not found"
             


@tiktok.route('/tiktok_user_data', methods=['POST'])
def set_all_data():
    request_data = request.get_json()
    user_tiktok = request_data['user']
    return get_data_tiktok(user_tiktok)


@tiktok.route('/GetData', methods=['POST'])
def get_all_data_user():
    request_data = request.get_json()
    user_tiktok = request_data['user']
    id_user = TiKtok_user.query.filter_by(name=user_tiktok).first()
    tiktok_user_data = Tiktok_user_data.query.filter_by(titok_user_id=id_user.id).all
    return jsonify ( {"user":user_tiktok,"data":tiktok_user_data})