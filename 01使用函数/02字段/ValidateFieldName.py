# -*- coding: cp936 -*-
import arcpy,os
## ��������Ҫ����
arcpy.CreateFeatureclass_management(os.getcwd(),"test.shp","POLYGON")
## �����ֶ������淶���������ᱨ��ERROR 000310: �ֶ����Ʋ��������ֿ�ͷ�������г���
##arcpy.AddField_management(os.getcwd()+os.sep+"test.shp","111","TEXT")

validateFieldName=arcpy.ValidateFieldName("x-45",os.getcwd()+os.sep+"test.shp")
arcpy.AddField_management(os.getcwd()+os.sep+"test.shp",validateFieldName,"TEXT")

validateFieldName=arcpy.ValidateFieldName("111",os.getcwd()+os.sep+"test.shp")
arcpy.AddField_management(os.getcwd()+os.sep+"test.shp",validateFieldName,"TEXT")

# ɾ�����ڲ��Ե�Ҫ����
#arcpy.Delete_management(os.getcwd()+os.sep+"test.shp")
