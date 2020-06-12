# EoT_testbed

# Run db_data.py for inserting packets to database.
python db_data.py

# Set variable env for directory of packet.json in '.bashrc'
sudo nano ~/.bashrc
PACKET_PATH=(your path)

# Run this command to capture MQTT packets.
sudo tshark -T json -f "src port 1883" -i lo >> PACKET_PATH/packets.json
