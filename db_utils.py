import pymongo
import json

def CheckConnDB(addr, database, collection):
  try:
    mongo_conn = pymongo.MongoClient(addr)
    if database in mongo_conn.list_database_names():
      mongo_db = mongo_conn[database]
      if collection in mongo_db.list_collection_names():
        mongo_col = mongo_db[collection]
        return mongo_col, True
  except:
    return None, False

def GetPacket(packet_path):
  packet_file = open(packet_path, "r")
  json_packet_list = []
  packet = []
  str_packet = ""
  begin = 1
  end = 0

  lines = packet_file.readlines()
  packet_file.close()
  for end in range(end, len(lines)):
    if lines[end] == "\n":
      packet = lines[begin:end]
      for index in packet:
        str_packet += index
      str_packet = str_packet.replace(".", "-")
      json_packet_list.append(json.loads(str_packet))
      begin = end + 2
      str_packet = ""

  return json_packet_list