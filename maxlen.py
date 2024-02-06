
from load_config import config
import glob, os, shutil
from tqdm import tqdm
import gzip

TLD = 'app'
SORTBY = 'alpha'
MAXLEN = 31

working_directory = 'data'

data_dir = os.path.join(working_directory, f'{TLD}_{SORTBY}_sorted')
print(data_dir)
output_dir = os.path.join(working_directory, f'{TLD}_{SORTBY}_sorted_{MAXLEN}')
shutil.rmtree(output_dir, ignore_errors=True)
os.makedirs(output_dir, exist_ok=True)

file_list = glob.glob(data_dir + "/*")

print(file_list)

for file_name in tqdm(file_list):
    with gzip.open(file_name, 'r') as f:
        lines = f.readlines()
        lines = [line for line in lines if len(line) <= MAXLEN]
        with gzip.open(os.path.join(output_dir, os.path.basename(file_name)), 'w') as f2:
            f2.writelines(lines)

