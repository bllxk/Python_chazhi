# -*- coding: cp936 -*-
import arcpy,os

if arcpy.Exists(os.getcwd()+os.sep+"test.shp") :
    print "�ļ��Ѵ���"
else :
    arcpy.CreateFeatureclass_management(os.getcwd(),"test.shp","POLYGON")
    
desc = arcpy.Describe(os.getcwd()+os.sep+"test.shp")

# ����ļ��������ƣ�������׺��ֻ���ļ�����
print desc.baseName
# �������·����ȫ·��+�ļ���+��׺��
print desc.catalogPath
# ����ļ���������
print desc.dataType
# ����ļ���׺
print desc.extension
# ����ļ����ƣ��ļ���+��׺��
print desc.file
# ����ļ���·����ֻ��·����
print desc.path
