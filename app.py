
from flask import Flask,request,json
import os

app = Flask(__name__)
cf_port = os.getenv("PORT", 3000)

@app.route('/')
def hello():
    return 'Webhooks with Python'
  
@app.route('/githubIssue',methods=['POST'])
def githubIssue():
    data = request.json
    print(f'Issue {data["issue"]["title"]} {data["action"]}')
    print(f'{data["issue"]["body"]}')
    print(f'{data["issue"]["url"]}')
    return data  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(cf_port))
