from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import pandas as pd
from io import StringIO
from datetime import datetime,date
import datetime


app = Flask(__name__)
mysql_password = "hodson2003"
mysql_instance_name = "test3"
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:' + mysql_password + '@aws-mytt2db.cssuvkukhmkq.us-east-2.rds.amazonaws.com/' + mysql_instance_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'xxx'
db = SQLAlchemy(app)


class CSV(db.Model):
    __tablename__ = 'CSV'
    CSV_ID = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    Upload_TimeStamp = db.Column(db.DateTime, nullable=False)
    Data = db.Column(db.Text, nullable=False)
    Issuer = db.Column(db.String(50), nullable=True)
    Raid_Finished_Date = db.Column(db.DateTime, nullable=True,default=datetime.datetime.now())


class Clan(db.Model):
    __tablename__ = 'Clan'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    PlayerCode = db.Column(db.String(10), nullable=False)
    CSV_ID = db.Column(db.Integer, nullable=False, autoincrement=True)
    Clan_Code = db.Column(db.String(10), nullable=True)
    Issuer = db.Column(db.String(50), nullable=True)


class Personal_Detail_Per_CSV(db.Model):
    __tablename__ = 'Personal_Detail_Per_CSV'
    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    PlayerCode = db.Column(db.String(10), nullable=False)
    CSV_ID = db.Column(db.Integer, nullable=False, autoincrement=True)
    TotalRaidAttacks = db.Column(db.Integer, nullable=False)
    TotalTitanNumber = db.Column(db.Integer, nullable=False)


class Player_Name(db.Model):
    __tablename__ = 'Player_Name'
    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    PlayerCode = db.Column(db.String(10), nullable=False)
    PlayerName = db.Column(db.String(50), nullable=False)
    CSV_ID = db.Column(db.Integer, nullable=False, autoincrement=True)


class Attak_Detail(db.Model):
    __tablename__ = 'Attak_Detail'
    id = db.Column(db.Integer, nullable=False, autoincrement=True, unique=True, primary_key=True)
    PlayerCode = db.Column(db.String(10), nullable=False)
    CSV_ID = db.Column(db.Integer, nullable=False, autoincrement=True)
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


header_list = ['PlayerName', 'PlayerCode', 'TotalRaidAttacks', 'TitanNumber', 'TitanName', 'TitanDamage', 'ArmorHead',
               'ArmorTorso', 'ArmorLeftArm', 'ArmorRightArm', 'ArmorLeftHand', 'ArmorRightHand', 'ArmorLeftLeg',
               'ArmorRightLeg',
               'BodyHead', 'BodyTorso', 'BodyLeftArm', 'BodyRightArm', 'BodyLeftHand', 'BodyRightHand', 'BodyLeftLeg',
               'BodyRightLeg', 'SkeletonHead', 'SkeletonTorso', 'SkeletonLeftArm', 'SkeletonRightArm',
               'SkeletonLeftHand',
               'SkeletonRightHand', 'SkeletonLeftLeg', 'SkeletonRightLeg']

filePath = 'D:\\github\\TT2-Clan-Raid\\sample_csv\\'
filename_list = os.listdir(filePath)

datasets_string_list = []
datasets_string_timestamp = []
Issuer = "Shen Shu"
Clan_Code = "qnex2"

for file in filename_list:
    if file[-3:] == "csv":

        file_year = file[:4]  # STR
        file_month = file[4:6]
        file_day = file[6:8]
        file_object = open(f"{filePath}{file}", encoding='UTF-8')
        try:
            datasets_string = file_object.read()
            datasets_string_list.append(datasets_string)
            datasets_string_timestamp.append(pd.Timestamp(file_year + "-" + file_month + "-" + file_day))
        finally:
            file_object.close()

start_time_total = datetime.datetime.now()
print(f"project start at: {start_time_total}")


for i in range(len(datasets_string_list)):
    start_time_each = datetime.datetime.now()
    timestamp_now = datasets_string_timestamp[i]
    data = StringIO(datasets_string_list[i])
    df1 = pd.read_csv(data, header=1, names=header_list)
    each_csv_instances=[]
    def add_new_CSV_instance(df):

        CSV_T_new_instance = CSV(
            Upload_TimeStamp=start_time_each.strftime('%Y-%m-%d %H:%M:%S'),
            Data=datasets_string_list[0],
            Issuer=Issuer if Issuer else None,
            Raid_Finished_Date=datasets_string_timestamp[i],
        )
        each_csv_instances.append(CSV_T_new_instance)
        db.session.add(CSV_T_new_instance)
        db.session.commit()
    add_new_CSV_instance(df1)
    print(f"add_new_CSV_instance cost: {(datetime.datetime.now() - start_time_each)}")
    csv_id = CSV.query.filter(CSV.Upload_TimeStamp == start_time_each.strftime('%Y-%m-%d %H:%M:%S')).first().CSV_ID
    print(csv_id)

    playerName_playerCode = df1.groupby(["PlayerName", "PlayerCode"]).count().reset_index()[
        ["PlayerName", "PlayerCode"]]

    Clan_T_new_instances = []
    def add_new_Clan_instance(row):
        global each_csv_instances
        global Clan_T_new_instances
        Clan_T_new_instance = Clan(
            PlayerCode=row['PlayerCode'],
            CSV_ID=csv_id,
            Clan_Code=Clan_Code if Clan_Code else None,
            Issuer=Issuer if Issuer else None)
        #Clan_T_new_instances.append(Clan_T_new_instance)
        each_csv_instances.append(Clan_T_new_instance)
    playerName_playerCode.apply(add_new_Clan_instance, axis=1, args=())

    # db.session.add_all(Clan_T_new_instances)
    # db.session.commit()
    print(f"add_new_Clan_instance time cost: {(datetime.datetime.now() - start_time_each)}")

    Attak_Detail_T_new_instances=[]
    def add_new_Attack_Detail_instance(row):
        global each_csv_instances
        global Attak_Detail_T_new_instances
        Attak_Detail_T_new_instance = Attak_Detail(
            PlayerCode=row['PlayerCode'],
            CSV_ID=csv_id,
            TitanNumber=row['TitanNumber'],
            TitanName=row['TitanName'],
            TitanDamage=row['TitanDamage'],
            ArmorHead=row['ArmorHead'],
            ArmorTorso=row['ArmorTorso'],
            ArmorLeftArm=row['ArmorLeftArm'],
            ArmorRightArm=row['ArmorRightArm'],
            ArmorLeftHand=row['ArmorLeftHand'],
            ArmorRightHand=row['ArmorRightHand'],
            ArmorLeftLeg=row['ArmorLeftLeg'],
            ArmorRightLeg=row['ArmorRightLeg'],
            BodyHead=row['BodyHead'],
            BodyTorso=row['BodyTorso'],
            BodyLeftArm=row['BodyLeftArm'],
            BodyRightArm=row['BodyRightArm'],
            BodyLeftHand=row['BodyLeftHand'],
            BodyRightHand=row['BodyRightHand'],
            BodyLeftLeg=row['BodyLeftLeg'],
            BodyRightLeg=row['BodyRightLeg'],
            SkeletonHead=row['SkeletonHead'],
            SkeletonTorso=row['SkeletonTorso'],
            SkeletonLeftArm=row['SkeletonLeftArm'],
            SkeletonRightArm=row['SkeletonRightArm'],
            SkeletonLeftHand=row['SkeletonLeftHand'],
            SkeletonRightHand=row['SkeletonRightHand'],
            SkeletonLeftLeg=row['SkeletonLeftLeg'],
            SkeletonRightLeg=row['SkeletonRightLeg'],
        )
        # Attak_Detail_T_new_instances.append(Attak_Detail_T_new_instance)
        each_csv_instances.append(Attak_Detail_T_new_instance)

    df1.apply(add_new_Attack_Detail_instance, axis=1, args=())
    # db.session.add_all(Attak_Detail_T_new_instances)
    # db.session.commit()
    # print(f"add_new_Attack_Detail_instance time cost: {(datetime.datetime.now() - start_time_each)}")

    Player_Name_T_new_instances=[]
    def add_new_Player_Name_instance(row):
        global each_csv_instances
        global Player_Name_T_new_instances
        Player_Name_T_new_instance = Player_Name(
            PlayerCode=row['PlayerCode'],
            PlayerName=row['PlayerName'],
            CSV_ID=csv_id,
        )
        # Player_Name_T_new_instances.append(Player_Name_T_new_instance)
        each_csv_instances.append(Player_Name_T_new_instance)
    playerName_playerCode.apply(add_new_Player_Name_instance, axis=1, args=())
    # db.session.add_all(Player_Name_T_new_instances)
    # db.session.commit()
    # print(f"add_new_Player_Name_instance time cost: {(datetime.datetime.now() - start_time_each)}")
    db.session.add_all(each_csv_instances)
    db.session.commit()
    end_time_each = datetime.datetime.now()
    print(f'{datasets_string_timestamp[i]} time used: {(end_time_each - start_time_each)}')
    break


end_time_total = datetime.datetime.now()
print(f'total time used: {(end_time_total - start_time_total)}')