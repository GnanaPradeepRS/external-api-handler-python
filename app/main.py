# from linkedin_api import Linkedin
# from flask import request, Flask, jsonify

# app = Flask(__name__)
# # print('entered234')
# # @app.route('/externalapihandler/socialhandle' , methods=['POST'])
# # def create_task():
# #     print('task')
# #     username = request.json.get('linkedin')
# #     auth = Linkedin('cruz.thepal@gmail.com', 'iwbah@77')
# #     profile = auth.get_company('riversand')
# #     print('return')
# #     return jsonify({"count" : profile.get('followingInfo').get('followerCount')})

# @app.route('/externalapihandler/socialhandle' ,  methods=['POST'])
# def index():
#     return "<h1>Welcome to our server !!</h1>"

# if __name__ == '__main__':
#     app.run(threaded=True, port=5000)

from flask import Flask 
  
app = Flask(__name__) 
  
@app.route("/") 
def home_view(): 
        return "<h1>Welcome to Geeks for Geeks</h1>"