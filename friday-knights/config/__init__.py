from os import getenv

db_name = getenv('DB_NAME')
db_user = getenv('DB_USER')
db_passwd = getenv('DB_PASSWD')
db_host = getenv('DB_HOST')
db_port = getenv('DB_PORT')
app_key = getenv('APP_KEY')
db_credentials = f'{db_user}:{db_pass}'
db_socket = f'{db_host}:{db_port}'

# loaded config 
conf = { 
'SQLALCHEMY_DATABASE_URI' : f'postgresql://{db_credentials}@{db_socket}/{db_name}',
'SQLALCHEMY_TRACK_MODIFICATIONS' : False,
'SECRET_KEY' : app_key         
}

class Config(object):
    @property
    def db_url(self):
        return self.get_property('SQLALCHEMY_DATABASE_URI')

    @property
    def db_track_mods(self):
        return self.get_property('SQLALCHEMY_TRACK_MODIFICATIONS')

    @property
    def sec_key(self):
        return self.get_property('SECRET_KEY')
      
    def __init__(self):
        self._config = conf # set it to conf

    def get_property(self, property_name):
        if property_name not in self._config.keys(): # we don't want KeyError
            return None  # just return None if not found
        return self._config[property_name]