import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# mysql_username="root"
# mysql_password = "dddd"
# ip_address="localhost"
# mysql_instance_name = "tt5"
mysql_username="admin"
mysql_password = "hodson2003"
mysql_instance_name = "ssaca"
ip_address="aws-mytt2db.cssuvkukhmkq.us-east-2.rds.amazonaws.com"
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{mysql_username}:' + mysql_password + f'@{ip_address}/' + mysql_instance_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class CSV(db.Model):
    __tablename__ = 'tt2_csv'
    CSV_ID = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    Upload_TimeStamp = db.Column(db.DateTime, nullable=False,default=datetime.datetime.now())
    Data = db.Column(db.Text, nullable=False)
    Issuer = db.Column(db.String(50), nullable=True)
    Raid_Finished_Date = db.Column(db.DateTime, nullable=True)
    MaxRaidAttacks = db.Column(db.Integer, nullable=False)
    NumberParticipants = db.Column(db.Integer, nullable=False)
    TotalTitanNumber = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.CSV_ID


class Clan(db.Model):
    __tablename__ = 'tt2_clan'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    PlayerCode = db.Column(db.String(10), nullable=False)
    CSV_ID_id = db.Column(db.Integer, nullable=False, autoincrement=True)
    Clan_Code = db.Column(db.String(10), nullable=True)
    Issuer = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return '<Task %r>' % self.id


class PersonalDetailPerCSV(db.Model):
    __tablename__ = 'tt2_personaldetailperCSV'
    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    PlayerCode = db.Column(db.String(10), nullable=False)
    CSV_ID_id = db.Column(db.Integer, nullable=False, autoincrement=True)
    RaidAttacks = db.Column(db.Integer, nullable=False)
    EffectiveDMG = db.Column(db.Integer, nullable=False)
    WrongDMG = db.Column(db.Integer, nullable=False)
    EffectivePercentage = db.Column(db.Float, nullable=False)
    AverageDMG = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.id


class PlayerName(db.Model):
    __tablename__ = 'tt2_playername'
    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    PlayerCode = db.Column(db.String(10), nullable=False)
    PlayerName = db.Column(db.String(50), nullable=False)
    CSV_ID_id = db.Column(db.Integer, nullable=False, autoincrement=True)

    def __repr__(self):
        return '<Task %r>' % self.id


class AttackDetail(db.Model):
    __tablename__ = 'tt2_attackdetail'
    id = db.Column(db.Integer, nullable=False, autoincrement=True, unique=True, primary_key=True)
    PlayerCode = db.Column(db.String(10), nullable=False)
    CSV_ID_id = db.Column(db.Integer, nullable=False, autoincrement=True)
    TitanNumber = db.Column(db.Integer, nullable=False)
    TitanName = db.Column(db.String(20), nullable=False)
    TitanDamage = db.Column(db.Integer, nullable=False)
    ArmorHead = db.Column(db.Integer, nullable=False)
    ArmorTorso = db.Column(db.Integer, nullable=False)
    ArmorLeftArm = db.Column(db.Integer, nullable=False)
    ArmorRightArm = db.Column(db.Integer, nullable=False)
    ArmorLeftHand = db.Column(db.Integer, nullable=False)
    ArmorRightHand = db.Column(db.Integer, nullable=False)
    ArmorLeftLeg = db.Column(db.Integer, nullable=False)
    ArmorRightLeg = db.Column(db.Integer, nullable=False)
    BodyHead = db.Column(db.Integer, nullable=False)
    BodyTorso = db.Column(db.Integer, nullable=False)
    BodyLeftArm = db.Column(db.Integer, nullable=False)
    BodyRightArm = db.Column(db.Integer, nullable=False)
    BodyLeftHand = db.Column(db.Integer, nullable=False)
    BodyRightHand = db.Column(db.Integer, nullable=False)
    BodyLeftLeg = db.Column(db.Integer, nullable=False)
    BodyRightLeg = db.Column(db.Integer, nullable=False)
    SkeletonHead = db.Column(db.Integer, nullable=False)
    SkeletonTorso = db.Column(db.Integer, nullable=False)
    SkeletonLeftArm = db.Column(db.Integer, nullable=False)
    SkeletonRightArm = db.Column(db.Integer, nullable=False)
    SkeletonLeftHand = db.Column(db.Integer, nullable=False)
    SkeletonRightHand = db.Column(db.Integer, nullable=False)
    SkeletonLeftLeg = db.Column(db.Integer, nullable=False)
    SkeletonRightLeg = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.id


class CSVRules(db.Model):
    __tablename__ = 'tt2_csvrules'
    id = db.Column(db.Integer, nullable=False, autoincrement=True, unique=True, primary_key=True)
    CSV_ID_id = db.Column(db.Integer, nullable=False)
    TitanNumber = db.Column(db.Integer, nullable=False)
    TitanName = db.Column(db.String(20), nullable=False)
    ArmorHead = db.Column(db.Boolean, default=True, nullable=False)
    ArmorTorso = db.Column(db.Boolean, default=True, nullable=False)
    ArmorLeftArm = db.Column(db.Boolean, default=True, nullable=False)
    ArmorRightArm = db.Column(db.Boolean, default=True, nullable=False)
    ArmorLeftHand = db.Column(db.Boolean, default=True, nullable=False)
    ArmorRightHand = db.Column(db.Boolean, default=True, nullable=False)
    ArmorLeftLeg = db.Column(db.Boolean, default=True, nullable=False)
    ArmorRightLeg = db.Column(db.Boolean, default=True, nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.id


class PersonalRankPerCSV(db.Model):
    __tablename__ = 'tt2_personalrankpercsv'
    id = db.Column(db.Integer, nullable=False, autoincrement=True, unique=True, primary_key=True)
    PlayerCode = db.Column(db.String(10), nullable=False)
    CSV_ID_id = db.Column(db.Integer, nullable=False)
    EffectiveDMG_Rank = db.Column(db.Integer, nullable=False)
    EffectiveDMG_RankFromLast = db.Column(db.Integer, nullable=False)
    RaidAttacks_RankFromLast = db.Column(db.Integer, nullable=False)

header_list = ['PlayerName', 'PlayerCode', 'TotalRaidAttacks', 'TitanNumber', 'TitanName', 'TitanDamage', 'ArmorHead',
               'ArmorTorso', 'ArmorLeftArm', 'ArmorRightArm', 'ArmorLeftHand', 'ArmorRightHand', 'ArmorLeftLeg',
               'ArmorRightLeg',
               'BodyHead', 'BodyTorso', 'BodyLeftArm', 'BodyRightArm', 'BodyLeftHand', 'BodyRightHand', 'BodyLeftLeg',
               'BodyRightLeg', 'SkeletonHead', 'SkeletonTorso', 'SkeletonLeftArm', 'SkeletonRightArm',
               'SkeletonLeftHand',
               'SkeletonRightHand', 'SkeletonLeftLeg', 'SkeletonRightLeg']