
import pandas as pd
from load_config import config
import glob, os, shutil
from tqdm import tqdm

username, password, authen_base_url, czds_base_url, working_directory = config()
data_dir = os.path.join(working_directory, "zonefiles")
output_dir = os.path.join(working_directory, "cleaned_zonefiles")
shutil.rmtree(output_dir)
os.makedirs(output_dir, exist_ok=True)

file_list = glob.glob(data_dir + "/*")

for file_name in tqdm(file_list):
    print(file_name)
    tld = os.path.basename(file_name).split('.')[0]
    df = pd.read_csv(file_name, sep='\t', header=None, 
                     names=['domain', 'ttl', 'in', 'type', 'value'], 
                     dtype={'domain': str, 'ttl': str, 'in': str, 'type': str, 'value': str})
    domain = df['domain'].str.rsplit('.', expand=True, n=2)
    domain.columns = ['domain', 'tld', 'empty']
    domain = domain.drop(columns=['empty'])
    domain = domain.drop_duplicates()
    domain.to_csv(os.path.join(output_dir, tld+'.tsv.gz'), index=False, header=False, sep='\t')
    os.remove(file_name)