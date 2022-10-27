from configparser import ConfigParser

config = ConfigParser()

config["DEFAULT"] = {
    "port" : 8080,
    "max_conn": 5,
    "buffer_size": 8192,
    "ttl":180,
    "ip_server": ['34.204.107.148', '3.92.231.50', '44.201.131.175']
}

with open("parser.json","w") as f:
    config.write(f)