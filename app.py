from flask import render_template,url_for,Flask,request
from connection_dbModel import *
from io import StringIO
import pandas as pd

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/app/<int:id>')
def rount2(id):
    return

@app.route('/tt2/csv-submit',methods=['POST','GET'])
def tt2_csv_submit():
    if request.method=="GET":
        return render_template('tt2-csv-submit.html')
    elif request.method=="POST":
        start_time_total = datetime.datetime.now()
        print(f"project start at: {start_time_total}")
        csvInput=request.form.get('csvInput').strip()
        issuerInput=request.form.get('issuerInput')
        inputFRaid_Finished_date=request.form.get('inputFRaid_Finished_date')
        inputClan_Code=request.form.get('inputClan_Code')

        data = StringIO(csvInput)
        df1 = pd.read_csv(data, header=0, names=header_list)
        each_csv_instances = []

        def add_new_CSV_instance(df):
            CSV_T_new_instance = CSV(
                Data=csvInput,
                Issuer=issuerInput,
                Raid_Finished_Date=inputFRaid_Finished_date,
                MaxRaidAttacks=df['TotalRaidAttacks'].max(),
                NumberParticipants=df1.groupby("PlayerCode").count().shape[0],
                TotalTitanNumber=df1['TitanNumber'].max(),
            )
            return CSV_T_new_instance
        CSV_T_new_instance=add_new_CSV_instance(df1)
        db.session.add(CSV_T_new_instance)
        db.session.commit()
        csv_id=CSV_T_new_instance.CSV_ID

        playerName_playerCode = df1.groupby(["PlayerName", "PlayerCode"]).count().reset_index()[
            ["PlayerName", "PlayerCode"]]
        each_csv_instances=[]
        def add_new_Clan_instance(row):
            #global each_csv_instances
            Clan_T_new_instance = Clan(
                PlayerCode=row['PlayerCode'],
                CSV_ID=csv_id,
                Clan_Code=inputClan_Code,
                Issuer=issuerInput)
            each_csv_instances.append(Clan_T_new_instance)
        playerName_playerCode.apply(add_new_Clan_instance, axis=1, args=())

        def add_new_Attack_Detail_instance(row):
            #global each_csv_instances
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
            #global each_csv_instances
            Player_Name_T_new_instance = PlayerName(
                PlayerCode=row['PlayerCode'],
                PlayerName=row['PlayerName'],
                CSV_ID=csv_id,
            )
            each_csv_instances.append(Player_Name_T_new_instance)
        playerName_playerCode.apply(add_new_Player_Name_instance, axis=1, args=())

        parts_sign = []
        def add_new_CSVRules_instance(row):
            #global parts_sign
            #global each_csv_instances
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
            #global parts_sign
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
        df1_sum = df1.groupby(["PlayerCode", "TotalRaidAttacks"]).sum().reset_index()

        def add_new_PersonalDetailPerCSV_instance(row):
            #global each_csv_instances
            PersonalDetailPerCSV_T_new_instance = PersonalDetailPerCSV(
                PlayerCode=row['PlayerCode'],
                CSV_ID=csv_id,
                RaidAttacks=row['TotalRaidAttacks'],
                EffectiveDMG=row['EffectiveDMG'],
                WrongDMG=row['WrongDMG'],
                EffectivePercentage=row['EffectiveDMG'] / row['TitanDamage'] if row['TitanDamage'] != 0 else 0,
                AverageDMG=row['TitanDamage'] / row['TotalRaidAttacks'] if row['TitanDamage'] != 0 else 0,
            )

            each_csv_instances.append(PersonalDetailPerCSV_T_new_instance)

        df1_sum.apply(add_new_PersonalDetailPerCSV_instance, axis=1, args=())
        df1_sum['EffectiveDMG_Rank'] = df1['EffectiveDMG'].rank(method='max')
        df1_sum['EffectiveDMG_RankFromLast'] = df1['EffectiveDMG'].rank(method='max', ascending=False)
        df1_sum['RaidAttacks_RankFromLast'] = df1['TotalRaidAttacks'].rank(method='max', ascending=False)

        def add_new_PersonalRankPerCSV_instance(row):
            #global each_csv_instances
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

        return {"csvInput":csvInput,"issuerInput":issuerInput,"inputFRaid_Finished_date":inputFRaid_Finished_date,"inputClan_Code":inputClan_Code}



if __name__ == '__main__':
    app.run(debug=True)
