class PersonalDetailPerCSV(db.Model):
    __tablename__ = 'PersonalDetailPerCSV'
    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    PlayerCode = db.Column(db.String(10), nullable=False)
    CSV_ID = db.Column(db.Integer, nullable=False, autoincrement=True)
    TotalRaidAttacks = db.Column(db.Integer, nullable=False)
    TotalTitanNumber = db.Column(db.Integer, nullable=False)