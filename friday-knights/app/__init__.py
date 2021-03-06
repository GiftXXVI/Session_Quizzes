from flask import Flask
from flask_migrate import Migrate
from api.sessions import sessions_bp
from model import cfg, db

app = Flask(__name__)
app.config.update({'SQLALCHEMY_DATABASE_URI': cfg.db_url,
                   'SQLALCHEMY_TRACK_MODIFICATIONS': cfg.db_track_mods,
                   'SECRET_KEY': cfg.sec_key})
db.init_app(app)
migrate = Migrate(app, db)
#CORS(app, resources=r'*',origins=r'*',methods=['POST','PUT','DELETE'])
app.register_blueprint(sessions_bp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
