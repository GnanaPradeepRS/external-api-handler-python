from linkedin_api import Linkedin
from flask import request, Flask, jsonify

app = Flask(__name__)

@app.route("/externalapihandler/socialhandle",  methods=['POST'])
def home_view():
    try:
        username = request.json.get('linkedin')
        auth = Linkedin('cruz.thepal@gmail.com', 'iwbah@77')
        profile = auth.get_company('riversand')
        print(profile)
        return jsonify({"count" : profile.get('followingInfo').get('followerCount')})
    except Exception as error :
        print(error)
if __name__ == "__main__": 
        app.run() 
