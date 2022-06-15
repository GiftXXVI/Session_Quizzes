from flask import Flask
from model import cfg, db
app = Flask(__name__)
app.config.update({'SQLALCHEMY_DATABASE_URI': cfg.db_url,
                   'SQLALCHEMY_TRACK_MODIFICATIONS': cfg.db_track_mods,
                   'SECRET_KEY': cfg.sec_key})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
