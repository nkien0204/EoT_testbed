touch packets.json
sudo tshark -T json -f "src port 1883" -i lo >> packets.json