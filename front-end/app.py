from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson import json_util
from flask_cors import CORS

import json
# Kết nối đến MongoDB (mặc định là localhost, port 27017)
client = MongoClient('mongodb://localhost:27017/123456')

# Tên cơ sở dữ liệu và collection
database = client['QLSV']
collection = database["SinhVien"]

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/123456"
mongo = PyMongo(app)
CORS(app)

@app.route('/students',methods= ['GET','POST'])

def home():
    # Lấy tất cả sinh viên từ MongoDB và sử dụng json_util để chuyển đổi ObjectId
    # Lấy tất cả sinh viên từ MongoDB và sử dụng json_util để chuyển đổi ObjectId
    all_students = list(collection.find())
    converted_students = json_util.dumps(all_students)
    
    # Trả về phản hồi JSON
    return app.response_class(
        response=converted_students,
        status=200,
        mimetype='application/json'
    )
if __name__ == "__main__":
    app.run(debug= True, port= '3000', host= '0.0.0.0')