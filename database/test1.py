# from pymongo import MongoClient
# from bson import ObjectId

# # Kết nối đến MongoDB
# client = MongoClient("mongodb://localhost:27017/123456")
# db = client["QLSV"]

# # ID của sinh viên và phụ huynh cần liên kết
# student_id = ObjectId('6572b26d7600aa78f740cdac')
# parent_id = ObjectId('65733417d537adb10cb300eb')


# student = db.SinhVien.find_one({'_id': student_id})
# if student:
#     # Kiểm tra xem sinh viên đã có thông tin phụ huynh hay chưa
#     if 'MaPH' in student and student['MaPH']:
#         print("Sinh viên đã có thông tin phụ huynh.")
#     else:
#         # Cập nhật bản ghi của sinh viên để thêm trường MaPH chứa ID của phụ huynh
#         db.SinhVien.update_one({'MaSV': student_id}, {'$set': {'MaPH': parent_id}})
#         print(f"Sinh viên có ID {student_id} đã được liên kết với phụ huynh có ID {parent_id}")
# else:
#     print(f"Không tìm thấy sinh viên có ID {student_id}")

# # Đóng kết nối
# client.close()

from pymongo import MongoClient
from bson import ObjectId

# Kết nối đến MongoDB
client = MongoClient("mongodb://localhost:27017/123456")
db = client["QLSV"]

# ID của sinh viên cần kiểm tra
student_id_to_check = ObjectId('6572b26d7600aa78f740cdac')

# Lấy thông tin chi tiết của sinh viên
student_info = db.SinhVien.find_one({'_id': student_id_to_check})

# Kiểm tra xem trường liên kết (ví dụ: MaPH) có giá trị hay không
if student_info and 'MaPH' in student_info and student_info['MaPH']:
    print(f"Sinh viên có ID {student_id_to_check} đã được liên kết với phụ huynh.")
else:
    print(f"Sinh viên có ID {student_id_to_check} chưa được liên kết với phụ huynh hoặc thông tin không tồn tại.")

# Đóng kết nối
client.close()
