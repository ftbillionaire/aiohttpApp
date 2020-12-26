import yaml
import pathlib

BASE_DIR = pathlib.Path(__file__).parent.parent
path_config = BASE_DIR / 'config' / 'blogdb.yaml'

def get_config(path):
    with open(path) as f:
        config = yaml.safe_load(f)
    return config

config = get_config(path_config)