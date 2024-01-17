
from more_itertools import first
import pandas as pd
from load_config import config
import glob, os, shutil
from tqdm import tqdm
from itertools import islice
import gzip

username, password, authen_base_url, czds_base_url, working_directory = config()
data_dir = os.path.join(working_directory, "split_zonefiles")

file_list = glob.glob(data_dir + "/*")

TLD = 'com'
SORTBY = 'alpha'

output_dir = os.path.join(working_directory, f'{TLD}_{SORTBY}')
shutil.rmtree(output_dir, ignore_errors=True)
os.makedirs(output_dir, exist_ok=True)

for file_name in tqdm(file_list):
    batch_size = 10000000
    with gzip.open(file_name, 'r') as f:
        while True:
            batch = list(islice(f, batch_size))
            if not batch:
                break
            
            len_dict = {}
            
            if SORTBY == 'alpha':
                
                for line in tqdm(batch, desc='Sorting batch'):
                    ch = line[0]
                    if ch not in len_dict:
                        len_dict[ch] = []
                    len_dict[ch].append(line)
                    
            elif SORTBY == 'length':
                
                for line in tqdm(batch, desc='Sorting batch'):
                    if len(line) not in len_dict:
                        len_dict[len(line)] = []
                    len_dict[len(line)].append(line)
            
            for key in len_dict:
            
                with gzip.open(os.path.join(output_dir, f'{key}_{TLD}.txt.gz'), 'a') as f2:
                    f2.writelines(len_dict[key])

