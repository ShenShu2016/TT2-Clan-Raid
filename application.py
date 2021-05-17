from flask import render_template, url_for, Flask, request
from flask_sqlalchemy import SQLAlchemy
from io import StringIO
import pandas as pd
import datetime
application = app = Flask(__name__)
# mysql_username="root"
# mysql_password = "dddd"
# ip_address="localhost"
# mysql_instance_name = "tt5"
mysql_username="admin"
mysql_password = "hodson2003"
mysql_instance_name = "AWS-TT2"
ip_address="aws-mytt2db.cssuvkukhmkq.us-east-2.rds.amazonaws.com"
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{mysql_username}:' + mysql_password + f'@{ip_address}/' + mysql_instance_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class CSV(db.Model):
    __tablename__ = 'CSV'
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
    __tablename__ = 'Clan'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    PlayerCode = db.Column(db.String(10), nullable=False)
    CSV_ID = db.Column(db.Integer, nullable=False, autoincrement=True)
    Clan_Code = db.Column(db.String(10), nullable=True)
    Issuer = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return '<Task %r>' % self.id


class PersonalDetailPerCSV(db.Model):
    __tablename__ = 'PersonalDetailPerCSV'
    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    PlayerCode = db.Column(db.String(10), nullable=False)
    CSV_ID = db.Column(db.Integer, nullable=False, autoincrement=True)
    RaidAttacks = db.Column(db.Integer, nullable=False)
    EffectiveDMG = db.Column(db.Integer, nullable=False)
    WrongDMG = db.Column(db.Integer, nullable=False)
    EffectivePercentage = db.Column(db.Float, nullable=False)
    AverageDMG = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.id


class PlayerName(db.Model):
    __tablename__ = 'PlayerName'
    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    PlayerCode = db.Column(db.String(10), nullable=False)
    PlayerName = db.Column(db.String(50), nullable=False)
    CSV_ID = db.Column(db.Integer, nullable=False, autoincrement=True)

    def __repr__(self):
        return '<Task %r>' % self.id


class AttackDetail(db.Model):
    __tablename__ = 'AttackDetail'
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

    def __repr__(self):
        return '<Task %r>' % self.id


class CSVRules(db.Model):
    __tablename__ = 'CSVRules'
    id = db.Column(db.Integer, nullable=False, autoincrement=True, unique=True, primary_key=True)
    CSV_ID = db.Column(db.Integer, nullable=False)
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
    __tablename__ = 'PersonalRankPerCSV'
    id = db.Column(db.Integer, nullable=False, autoincrement=True, unique=True, primary_key=True)
    PlayerCode = db.Column(db.String(10), nullable=False)
    CSV_ID = db.Column(db.Integer, nullable=False)
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
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/app/<int:id>')
def rount2(id):
    return


@app.route('/tt2/csv-submit', methods=['POST', 'GET'])
def tt2_csv_submit():
    if request.method == "GET":
        return render_template('tt2-csv-submit.html')
    elif request.method == "POST":
        start_time_total = datetime.datetime.now()
        print(f"project start at: {start_time_total}")
        csvInput = request.form.get('csvInput').strip()
        issuerInput = request.form.get('issuerInput')
        inputFRaid_Finished_date = request.form.get('inputFRaid_Finished_date')
        print(inputFRaid_Finished_date)
        print(type(inputFRaid_Finished_date))
        inputClan_Code = request.form.get('inputClan_Code')

        data = StringIO(csvInput)
        df1 = pd.read_csv(data, header=0, names=header_list)
        each_csv_instances = []


        def add_new_CSV_instance(df):
            CSV_T_new_instance = CSV(
                Upload_TimeStamp=datetime.datetime.now(),
                Data=csvInput,
                Issuer=issuerInput,
                Raid_Finished_Date=inputFRaid_Finished_date if inputFRaid_Finished_date else None,
                MaxRaidAttacks=df['TotalRaidAttacks'].max(),
                NumberParticipants=df1.groupby("PlayerCode").count().shape[0],
                TotalTitanNumber=df1['TitanNumber'].max(),
            )
            return CSV_T_new_instance

        try:
            CSV_T_new_instance = add_new_CSV_instance(df1)
            db.session.add(CSV_T_new_instance)
            db.session.commit()
        except:
            return render_template('tt2-csv-submit.html')
        csv_id = CSV_T_new_instance.CSV_ID

        playerName_playerCode = df1.groupby(["PlayerName", "PlayerCode"]).count().reset_index()[
            ["PlayerName", "PlayerCode"]]
        each_csv_instances = []

        def add_new_Clan_instance(row):
            Clan_T_new_instance = Clan(
                PlayerCode=row['PlayerCode'],
                CSV_ID=csv_id,
                Clan_Code=inputClan_Code,
                Issuer=issuerInput)
            each_csv_instances.append(Clan_T_new_instance)

        playerName_playerCode.apply(add_new_Clan_instance, axis=1, args=())

        def add_new_Attack_Detail_instance(row):
            Attak_Detail_T_new_instance = AttackDetail(
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
            each_csv_instances.append(Attak_Detail_T_new_instance)

        df1.apply(add_new_Attack_Detail_instance, axis=1, args=())

        def add_new_Player_Name_instance(row):
            Player_Name_T_new_instance = PlayerName(
                PlayerCode=row['PlayerCode'],
                PlayerName=row['PlayerName'],
                CSV_ID=csv_id,
            )
            each_csv_instances.append(Player_Name_T_new_instance)

        playerName_playerCode.apply(add_new_Player_Name_instance, axis=1, args=())

        parts_sign = []

        def add_new_CSVRules_instance(row):

            body_TF = [True, True, True, True, True, True, True, True, row['TitanNumber']]
            body = ['BodyHead', 'BodyTorso', 'BodyLeftArm', 'BodyRightArm', 'BodyLeftHand', 'BodyRightHand',
                    'BodyLeftLeg',
                    'BodyRightLeg']
            for i in range(len(body)):
                if row[body[i]] <= 5000000:
                    body_TF[i] = False
            parts_sign.append(body_TF)

            CSVRules_t_new_instance = CSVRules(
                TitanNumber=row['TitanNumber'],
                TitanName=row['TitanName'],
                CSV_ID=csv_id,
                ArmorHead=body_TF[0],
                ArmorTorso=body_TF[1],
                ArmorLeftArm=body_TF[2],
                ArmorRightArm=body_TF[3],
                ArmorLeftHand=body_TF[4],
                ArmorRightHand=body_TF[5],
                ArmorLeftLeg=body_TF[6],
                ArmorRightLeg=body_TF[7],
            )
            each_csv_instances.append(CSVRules_t_new_instance)

        bodys = ['BodyHead', 'BodyTorso', 'BodyLeftArm', 'BodyRightArm', 'BodyLeftHand', 'BodyRightHand', 'BodyLeftLeg',
                 'BodyRightLeg']
        no_attacks = df1.groupby(['TitanNumber', 'TitanName'])[bodys].sum()
        no_attacks = no_attacks.reset_index()
        no_attacks.apply(add_new_CSVRules_instance, axis=1, args=())

        def get_WrongDMG(row):
            # global parts_sign
            armor = ['ArmorHead', 'ArmorTorso', 'ArmorLeftArm', 'ArmorRightArm', 'ArmorLeftHand', 'ArmorRightHand',
                     'ArmorLeftLeg', 'ArmorRightLeg']
            WrongDMG_per_titan = 0
            for i in parts_sign:
                if row['TitanNumber'] == i[8]:
                    for j in range(len(i) - 1):
                        if i[j] == False:
                            WrongDMG_per_titan += row[armor[j]]
            return WrongDMG_per_titan

        df1['WrongDMG'] = df1.apply(get_WrongDMG, axis=1, args=())

        df1['EffectiveDMG'] = df1['TitanDamage'] - df1['WrongDMG']
        df1_sum = df1.groupby(['PlayerName', "PlayerCode", "TotalRaidAttacks"]).sum().reset_index()
        df1_sum['AverageDMG'] = df1_sum['TitanDamage'] / df1_sum['TotalRaidAttacks']
        df1_sum['EffectivePercentage'] = df1_sum['EffectiveDMG'] / df1_sum['TitanDamage']

        def add_new_PersonalDetailPerCSV_instance(row):
            EffectivePercentage = row['EffectiveDMG'] / row['TitanDamage'] if row['TitanDamage'] != 0 else 0
            AverageDMG = row['TitanDamage'] / row['TotalRaidAttacks'] if row['TitanDamage'] != 0 else 0
            PersonalDetailPerCSV_T_new_instance = PersonalDetailPerCSV(
                PlayerCode=row['PlayerCode'],
                CSV_ID=csv_id,
                RaidAttacks=row['TotalRaidAttacks'],
                EffectiveDMG=row['EffectiveDMG'],
                WrongDMG=row['WrongDMG'],
                EffectivePercentage=EffectivePercentage,
                AverageDMG=AverageDMG,
            )

            each_csv_instances.append(PersonalDetailPerCSV_T_new_instance)

        df1_sum.apply(add_new_PersonalDetailPerCSV_instance, axis=1, args=())
        df1_sum['EffectiveDMG_Rank'] = df1_sum['EffectiveDMG'].rank(method='max').map(lambda x: int(x))
        df1_sum['EffectiveDMG_RankFromLast'] = df1_sum['EffectiveDMG'].rank(method='max', ascending=False).map(
            lambda x: int(x))
        df1_sum['RaidAttacks_RankFromLast'] = df1_sum['TotalRaidAttacks'].rank(method='max', ascending=False).map(
            lambda x: int(x))

        def add_new_PersonalRankPerCSV_instance(row):
            PersonalRankPerCSV_T_new_instance = PersonalRankPerCSV(
                PlayerCode=row['PlayerCode'],
                CSV_ID=csv_id,
                EffectiveDMG_Rank=row['EffectiveDMG_Rank'],
                EffectiveDMG_RankFromLast=row['EffectiveDMG_RankFromLast'],
                RaidAttacks_RankFromLast=row['RaidAttacks_RankFromLast']
            )
            each_csv_instances.append(PersonalRankPerCSV_T_new_instance)

        df1_sum.apply(add_new_PersonalRankPerCSV_instance, axis=1, args=())

        db.session.add_all(each_csv_instances)
        db.session.commit()
        end_time_total = datetime.datetime.now()
        print(f'total time used: {(end_time_total - start_time_total)}')

        print(df1_sum)
        return render_template("csv-detail.html", datasets=df1_sum)


if __name__ == '__main__':
    app.run(debug=True)
