# -*- coding: cp936 -*-
import arcpy,os
# �ڻ�����ʱ�ļ����´�����ʱ�ļ�
scratch_name = arcpy.CreateScratchName("temp",data_type="Shapefile",workspace=arcpy.env.scratchFolder)
print scratch_name
# �ڻ�����ʱGDB�´�����ʱ�ļ�
scratch_name = arcpy.CreateScratchName("temp",data_type="Shapefile",workspace=arcpy.env.scratchGDB)
print scratch_name




