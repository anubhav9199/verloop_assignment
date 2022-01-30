import os
from configparser import ConfigParser

current_dir = os.getcwd()
cfg_path = os.path.join(current_dir, "MasterConfig.ini")
cfg_parser = ConfigParser()
cfg_parser.read(cfg_path)


def get_map_key(config_data=cfg_parser):
    maps_key = config_data['config']['maps_key']
    return maps_key


if __name__ == "__main__":
    current_dir = os.getcwd()
    cfg_path = os.path.join(current_dir, "MasterConfig.ini")
    cfg_parser = ConfigParser()
    cfg_parser.read(cfg_path)
