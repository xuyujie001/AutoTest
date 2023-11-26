import configparser

class ConfigReader:
       def __init__(self, config_file="./config/config.ini"):
           self.config = configparser.ConfigParser()
           self.config.read(config_file)

       def get_value(self, section, key):
           return self.config.get(section, key)