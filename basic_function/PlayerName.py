class PlayerName(db.Model):
    __tablename__ = 'PlayerName'
    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    PlayerCode = db.Column(db.String(10), nullable=False)
    PlayerName = db.Column(db.String(50), nullable=False)
    CSV_ID = db.Column(db.Integer, nullable=False, autoincrement=True)