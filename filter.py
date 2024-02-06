
import string
from load_config import config
import glob, os, shutil
from tqdm import tqdm
import gzip

TLD = 'app'
SORTBY = 'alpha'
MAXLEN = 31

working_directory = 'data'

data_dir = os.path.join(working_directory, f'{TLD}_{SORTBY}_sorted_{MAXLEN}_combined')
print(data_dir)
output_dir = os.path.join(working_directory, f'{TLD}_{SORTBY}_sorted_{MAXLEN}_filtered')
shutil.rmtree(output_dir, ignore_errors=True)
os.makedirs(output_dir, exist_ok=True)

file_list = glob.glob(data_dir + "/*")

print(file_list)

def is_valid(line):
    for char in line[:-1]:
        if char < 97 or char > 122:
            return False
    return True

for file_name in file_list:
    with gzip.open(file_name, 'r') as f:
        out_lines = []
        for line in f:
            if is_valid(line):
                out_lines.append(line)
        with gzip.open(os.path.join(output_dir, f'{TLD}.txt.gz'), 'a') as f2:
            f2.writelines(out_lines)

