import os, sys, json

def config():

    try:
        if 'CZDS_CONFIG' in os.environ:
            config_data = os.environ['CZDS_CONFIG']
            config = json.loads(config_data)
        else:
            config_file = open("config.json", "r")
            config = json.load(config_file)
            config_file.close()
    except:
        sys.stderr.write("Error loading config.json file.\n")
        exit(1)

    # The config.json file must contain the following data:
    username = config['icann.account.username']
    password = config['icann.account.password']
    authen_base_url = config['authentication.base.url']
    czds_base_url = config['czds.base.url']

    # This is optional. Default to current directory
    working_directory = config.get('working.directory', '.') # Default to current directory

    if not username:
        sys.stderr.write("'icann.account.username' parameter not found in the config.json file\n")
        exit(1)

    if not password:
        sys.stderr.write("'icann.account.password' parameter not found in the config.json file\n")
        exit(1)

    if not authen_base_url:
        sys.stderr.write("'authentication.base.url' parameter not found in the config.json file\n")
        exit(1)

    if not czds_base_url:
        sys.stderr.write("'czds.base.url' parameter not found in the config.json file\n")
        exit(1)
        
    return username, password, authen_base_url, czds_base_url, working_directory