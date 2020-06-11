import db_utils
import time

conn = "mongodb://localhost:27017"
database = "fil_testbed"
collection = "fil_tb_col"

packets_list = []

mongo_col, check_conn = db_utils.CheckConnDB(conn, database, collection)

if check_conn:
  print("Database was connected!")
else:
  print("Could not connect to database")

pre_len = len(packets_list)

while True:
  packets_list = db_utils.GetPacket("packets.json")
  cur_len = len(packets_list)
  if pre_len != cur_len:
    for i in range(pre_len, cur_len):
      mongo_col.insert(packets_list[i])
    pre_len = cur_len

    notify = "Inserting {} packet(s) to database...".format(cur_len)
    print(notify)

  time.sleep(10)

# x = mongo_col.find().next()
# print(x["_source"])