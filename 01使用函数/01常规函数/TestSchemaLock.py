# -*- coding: cp936 -*-
import arcpy,os
# ��������Ҫ����
arcpy.CreateFeatureclass_management(os.getcwd(),"test.shp","POLYGON")

# ���Ҫ����Gis�д򿪻�õ�else�Ľ��
if arcpy.TestSchemaLock(os.getcwd()+os.sep+"test.shp"):
    print "���Ի�ȡ����������ΪҪ������ֶΣ�"
    arcpy.AddField_management(os.getcwd()+os.sep+"test.shp","TESTFIELD","TEXT")
else :
    print "�޷���ȡ������������"

# ɾ�����ڲ��Ե�Ҫ����
#arcpy.Delete_management(os.getcwd()+os.sep+"test.shp")
