
from curses.ascii import SO
import pandas as pd
from load_config import config
import glob, os, shutil
from tqdm import tqdm
from itertools import islice
import gzip

TLD = 'com'
SORTBY = 'alpha'

username, password, authen_base_url, czds_base_url, working_directory = config()
data_dir = os.path.join(working_directory, f'{TLD}_{SORTBY}')
output_dir = os.path.join(working_directory, f'{TLD}_{SORTBY}_sorted')
shutil.rmtree(output_dir, ignore_errors=True)
os.makedirs(output_dir, exist_ok=True)

file_list = glob.glob(data_dir + "/*")

for file_name in tqdm(file_list):
    print(file_name)
    with gzip.open(file_name, 'r') as f:
        lines = f.readlines()
        lines = sorted(lines)
        with gzip.open(os.path.join(output_dir, os.path.basename(file_name)), 'w') as f2:
            f2.writelines(lines)

