from connection_dbModel import CSV, Clan, PersonalDetailPerCSV, PlayerName, AttackDetail, header_list, db
import os
import pandas as pd
from io import StringIO
import datetime

file = 'D:\\github\\TT2-Clan-Raid\\sample_csv\\20201119.csv'
Issuer = "Shen Shu"
Clan_Code = "qnex2"


def get_csv():
    file_year = file[-12:-8]  # STR
    file_month = file[4-12:6-12]
    file_day = file[6-12:8-12]
    file_object = open(f"{file}", encoding='UTF-8')
    try:
        dataset_string = file_object.read()
        dataset_timestamp = pd.Timestamp(file_year + "-" + file_month + "-" + file_day)
    finally:
        file_object.close()
    return dataset_string, dataset_timestamp


dataset_string, dataset_timestamp = get_csv()

start_time_total = datetime.datetime.now()
print(f"project start at: {start_time_total}")

start_time_each = datetime.datetime.now()
timestamp_now = dataset_timestamp
data = StringIO(dataset_string)
df1 = pd.read_csv(data, header=1, names=header_list)


def add_new_csv_instance(df):
    csv_t_new_instance = CSV(
        Data=dataset_string,
        Issuer=Issuer if Issuer else None,
        Raid_Finished_Date=dataset_timestamp,
    )
    return csv_t_new_instance
csv_t_new_instance=add_new_csv_instance(df1)
db.session.add(csv_t_new_instance)
db.session.commit()
print(f"add_new_csv_instance cost: {(datetime.datetime.now() - start_time_each)}")
csv_id = csv_t_new_instance.CSV_ID
print(csv_id)

playerName_playerCode = df1.groupby(["PlayerName", "PlayerCode"]).count().reset_index()[
    ["PlayerName", "PlayerCode"]]

clan_t_new_instances = []

each_csv_instances=[]
def add_new_clan_instance(row):
    global each_csv_instances
    global clan_t_new_instances
    clan_t_new_instance = Clan(
        PlayerCode=row['PlayerCode'],
        CSV_ID=csv_id,
        Clan_Code=Clan_Code if Clan_Code else None,
        Issuer=Issuer if Issuer else None)
    each_csv_instances.append(clan_t_new_instance)


playerName_playerCode.apply(add_new_clan_instance, axis=1, args=())

print(f"add_new_clan_instance time cost: {(datetime.datetime.now() - start_time_each)}")

attack_detail_t_new_instances = []


def add_new_attack_detail_instance(row):
    global each_csv_instances
    global attack_detail_t_new_instances
    attack_detail_t_new_instance = AttackDetail(
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
    each_csv_instances.append(attack_detail_t_new_instance)


df1.apply(add_new_attack_detail_instance, axis=1, args=())

player_name_t_new_instances = []


def add_new_player_name_instance(row):
    global each_csv_instances
    global player_name_t_new_instances
    player_name_t_new_instance = PlayerName(
        PlayerCode=row['PlayerCode'],
        PlayerName=row['PlayerName'],
        CSV_ID=csv_id,
    )

    each_csv_instances.append(player_name_t_new_instance)


playerName_playerCode.apply(add_new_player_name_instance, axis=1, args=())

db.session.add_all(each_csv_instances)
db.session.commit()
end_time_each = datetime.datetime.now()
print(f'{dataset_timestamp} time used: {(end_time_each - start_time_each)}')

end_time_total = datetime.datetime.now()
print(f'total time used: {(end_time_total - start_time_total)}')
