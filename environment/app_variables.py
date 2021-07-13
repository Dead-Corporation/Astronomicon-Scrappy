from dotenv import dotenv_values
import pathlib
import os
cwd = pathlib.Path(__file__).parent.resolve()
config = dotenv_values(os.path.join(cwd, '.env'))

postgre_user = config.get('POSTGRE_USER')
postgre_password = config.get('POSTGRE_PASSWORD')
postgre_host = config.get('POSTGRE_HOST')
postgre_port = config.get('POSTGRE_PORT')
postgre_name = config.get('POSTGRE_NAME')
base_dir = config.get('BASE_DIR')
