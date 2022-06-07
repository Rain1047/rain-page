import os
import configparser

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))
# print(os.path.abspath(os.path.join("app_ini")))
print(config)