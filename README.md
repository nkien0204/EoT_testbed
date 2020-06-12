# EoT_testbed

# Run db_data.py for inserting packets to database.
python db_data.py

# Move to directory of project
cd (your dir)

# Run 'db_run.sh' and then, 'db_capture.sh'
./db_run.sh
./db_capture.sh

# Run this command to capture MQTT packets.
sudo tshark -T json -f "src port 1883" -i lo >> PACKET_PATH/packets.json
