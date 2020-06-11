# EoT_testbed
# Run this command to capture MQTT packets

sudo tshark -T json -f "src port 1883" -i lo >> workspace/EoT_testbed/packets.json
