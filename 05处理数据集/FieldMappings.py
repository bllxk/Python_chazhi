# -*- coding: cp936 -*-
import arcpy, os, random

#   ���������
arcpy.CreateTable_management(os.getcwd(), "TestFieldMap.dbf")
in_table = os.getcwd() + os.sep + "TestFieldMap.dbf"

#   ���RoadID������ֶ�
arcpy.AddField_management(in_table, "RoadID", "TEXT", field_length=20)
for i in range(2009, 2020):
    arcpy.AddField_management(in_table, "Y" + str(i), "SHORT")

#   ����в�����
rows = arcpy.InsertCursor(in_table)
field_list = arcpy.ListFields(in_table, "Y*")
for i in range(1, 100):
    row = rows.newRow()
    row.setValue("RoadID", "Road" + str(i))
    for field in field_list:
        row.setValue(field.name, random.choice(range(30, 1000)))
    rows.insertRow(row)
    del row
del rows

#   ����FieldMap���󣬲����������ֶΡ��ϲ���������ֶ�
fm1 = arcpy.FieldMap()
fm1.mergeRule = "Mean"
for field in field_list:
    fm1.addInputField(in_table, field.name)
f_name = fm1.outputField
f_name.name = "MeanCount"
fm1.outputField = f_name

#   ��fm1��fm1��ӵ�������FieldMap����fms��
fms = arcpy.FieldMappings()
fm2 = arcpy.FieldMap()
fm2.addInputField(in_table, "RoadID")
fms.addFieldMap(fm2)
fms.addFieldMap(fm1)

#   ʹ�ñ������߲��������õ��ֶ�ӳ�佫��ת��
arcpy.TableToTable_conversion(in_table, os.getcwd(), "TestFieldMapOut.dbf", "", fms)
