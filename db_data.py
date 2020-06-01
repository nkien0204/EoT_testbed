import pymongo
import json

mongo_conn = pymongo.MongoClient("mongodb://localhost:27017")
mongo_db = mongo_conn["fil_testbed"]
mongo_col = mongo_db["fil_tb_col"]

wireshark_file = open("/home/iot_team/Documents/EoT_testbed/packets.json", "r")

# x = '{"name": "kien nguyen", "age": 22}'
# y = json.loads(x)

data = wireshark_file.readlines()
# data = wireshark_file.readlines()[0][1]
# data = data[1:]

print(data[8])
# print(len(data))
# y = json.loads(data)

# mongo_col.insert_one(wireshark_file)