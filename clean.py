import pandas as pd
from load_config import config

username, password, authen_base_url, czds_base_url, working_directory = config()

data_dir = working_directory + "/zonefiles"

import glob

file_list = glob.glob(data_dir + "/*")

df = pd.read_csv(file_list[0], sep='\t', header=None, names=['domain', 'ttl', 'in', 'type', 'value'])
print(df)