from linkedin_api import Linkedin
from flask import request, Flask, jsonify
import waitress
import os
app = Flask(__name__)
print('entered')
# @app.route('/externalapihandler/socialhandle' ,methods=['POST'])
# def create_task():
#     print('task')
#     username = request.json.get('linkedin')
#     auth = Linkedin('cruz.thepal@gmail.com', 'iwbah@77')
#     profile = auth.get_company('riversand')
#     print('return')
#     return jsonify({"count" : profile.get('followingInfo').get('followerCount')})


@app.route('/', methods=['POST'])
def create_task():
    print('task')
    return jsonify({'test': 'worked'})

port = int(os.environ.get('PORT', 33507))
waitress.serve(app, port=port)
app.run()

