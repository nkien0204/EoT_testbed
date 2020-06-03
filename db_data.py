import pymongo
import json
import db_utils

conn = "mongodb://localhost:27017"
database = "fil_testbed"
collection = "fil_tb_col"

mongo_col, check_conn = db_utils.CheckConnDB(conn, database, collection)

if check_conn:
  print("Database was connected!")
else:
  print("Could not connect to database")

packet = db_utils.GetPacket("/home/kn/Documents/FIL_EOT/packets.json")

# mongo_col.insert(packet)

x = mongo_col.find().next()
print(x["_source"])