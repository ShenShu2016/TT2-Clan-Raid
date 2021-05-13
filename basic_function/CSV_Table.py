class CSV(db.Model):
    __tablename__ = 'CSV'
    CSV_ID = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    Upload_TimeStamp = db.Column(db.DateTime, nullable=False,default=datetime.datetime.now())
    Data = db.Column(db.Text, nullable=False)
    Issuer = db.Column(db.String(50), nullable=True)
    Raid_Finished_Date = db.Column(db.DateTime, nullable=True)