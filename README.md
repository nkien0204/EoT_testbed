# EoT_testbed

# Run db_data.py for inserting packets to database.
python db_data.py
# Run this command to capture MQTT packets.
sudo tshark -T json -f "src port 1883" -i lo >> workspace/EoT_testbed/packets.json
