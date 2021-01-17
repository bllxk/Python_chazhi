# -*- coding: cp936 -*-
import arcpy, os, csv

arcpy.CreateFeatureclass_management(os.getcwd(), "testListFields.shp")
in_fc = os.getcwd() + os.sep + "testListFields.shp"
arcpy.AddField_management(in_fc, "Short_T", "SHORT")
arcpy.AddField_management(in_fc, "Long_T", "LONG")
arcpy.AddField_management(in_fc, "Float_T", "FLOAT", "7", "4")
arcpy.AddField_management(in_fc, "Double_T", "DOUBLE", "18", "4")
arcpy.AddField_management(in_fc, "Text_T", "TEXT", "", "", 100)

out_csv = os.getcwd() + os.sep + "a.csv"
header = ["�ֶ���", "����", "����", "����", "С��λ��"]
rows = []
try:
    for field in arcpy.ListFields(in_fc):
        row = [field.name, field.type, field.length, field.precision, field.scale]
        # ���о��ֶ���Ϣ��ȡ�����ֶ����ͺʹ����ֶε��ֶ����Ͳ���һ�£�����ӳ���ϵ
        # �ڴ��жϲ�ת�����õ�����Ϣ����ֱ�����ڴ����ֶ�
        if row[1] == "Integer":
            row[1] = "LONG"
        elif row[1] == "SmallInteger":
            row[1] = "SHORT"
        print row
        rows.append(row)
    with open(out_csv, "wb") as f:
        f_csv = csv.writer(f)
        f_csv.writerow(header)
        f_csv.writerows(rows)
except arcpy.ExecuteError:
    print arcpy.GetMessages()

# arcpy.Delete_management(in_fc)
# arcpy.Delete_management(out_csv)
