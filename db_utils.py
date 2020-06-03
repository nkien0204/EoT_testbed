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
  str_packet = packet_file.read()[1:-2]
  str_packet = str_packet.replace(".", "-")
  json_packet = json.loads(str_packet)
  return json_packet