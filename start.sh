sudo /opt/lampp/lampp start
mosquitto -c ~/flurry/mosquitto/mosquitto.conf
cd ~/flurry
conda activate flurryenv
python3 webserver.py
