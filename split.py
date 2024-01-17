
import pandas as pd
from load_config import config
import glob, os, shutil
from tqdm import tqdm
import gzip
from itertools import islice


username, password, authen_base_url, czds_base_url, working_directory = config()
data_dir = os.path.join(working_directory, "zonefiles")
output_dir = os.path.join(working_directory, "split_zonefiles")
shutil.rmtree(output_dir, ignore_errors=True)
os.makedirs(output_dir, exist_ok=True)

file_list = glob.glob(data_dir + "/*")

for file_name in file_list:

    batch_size = 100000000
    file_index = 0
    with gzip.open(file_name, 'r') as f:
        while True:
            batch = list(islice(f, batch_size))
            if not batch:
                break
            print(f'Processing batch {file_index}...')
            batch = map(lambda x: x.split(b'.', 1)[0] + b'\n', batch)
            batch = set(batch)
            with gzip.open(os.path.join(output_dir, f'{file_index}-{os.path.basename(file_name)}'), 'w') as f2:
                f2.writelines(batch)
                print(f'Wrote {len(batch)} lines in file {file_index}')
                file_index += 1
                    
            