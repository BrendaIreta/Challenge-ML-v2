import db
from models import Credenciales

def run():
    jose = Credenciales('Jose', 'B123')
    db.session.add(jose)
    print(jose.id)
    bren = Credenciales('Bren', 'E123')
    db.session.add(bren)
    db.session.commit()
    print(jose.id)


if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    run()