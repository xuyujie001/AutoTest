import yaml
from config.Conf import get_config_path
def getdata():
    f = open(get_config_path()+"/data.yaml", encoding="utf-8")
    data = yaml.safe_load(f)
    return data
if __name__ == '__main__':
    r = getdata()['mobile_params']
    print(r)


