# -*- coding: cp936 -*-
import arcpy,os
# �ڻ�����ʱ�ļ����´���Ψһ����ʱ�ļ���
scratch_name = arcpy.CreateUniqueName("temp.shp",arcpy.env.scratchFolder)
print scratch_name
arcpy.CreateFeatureclass_management(arcpy.env.scratchFolder,"temp.shp","POLYGON")
scratch_name = arcpy.CreateUniqueName("temp.shp",arcpy.env.scratchFolder)
print scratch_name
# �ڻ�����ʱGDB�´���Ψһ����ʱ�ļ���
scratch_name = arcpy.CreateUniqueName("temp",arcpy.env.scratchGDB)
print scratch_name




