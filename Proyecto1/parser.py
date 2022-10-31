from configparser import ConfigParser
import json
config = ConfigParser()

config["DEFAULT"] = {
    "port" : 8080,
    "max_conn": 5,
    "buffer_size": 8192,
    "ttl":180,
    "ip_server1": '54.152.81.179',
    "ip_server2": '52.23.107.62',
    "ip_server3": '3.232.160.126'
}

with open("parser.ini","w") as f:
    config.write(f)
