from flask import Flask, request
from flask_cors import CORS
from modules import auth, crawler

app = Flask(__name__)
CORS(app)  # 支持跨域

@app.route('/login', methods=['POST'])
def login():
    return auth.login(request.get_json())

@app.route('/crawl', methods=['POST'])
def crawl():
    return crawler.crawl(request.get_json())  # ⭐ 模块调用

if __name__ == '__main__':
    app.run(port=5000)
