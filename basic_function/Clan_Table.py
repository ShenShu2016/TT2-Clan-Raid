class Clan(db.Model):
    __tablename__ = 'Clan'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    PlayerCode = db.Column(db.String(10), nullable=False)
    CSV_ID = db.Column(db.Integer, nullable=False, autoincrement=True)
    Clan_Code = db.Column(db.String(10), nullable=True)
    Issuer = db.Column(db.String(50), nullable=True)