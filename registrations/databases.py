from decouple import config
def connect_to_db(app):
    db_connection = 'postgresql://postgres:iphone21@127.0.0.1:5432/postgres'
    app.config['SQLALCHEMY_DATABASE_URI'] = db_connection
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    return app