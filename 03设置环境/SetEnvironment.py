# -*- coding: cp936 -*-
import arcpy, os

#  ��ȡ���Ľ������Ϊ��
print arcpy.GetSystemEnvironment("TEMP")
print arcpy.GetSystemEnvironment("TMP")
print arcpy.GetSystemEnvironment("MW_TMPDIR")

# ��ȡĬ�ϵ�overwriteOutput����ֵ������overwriteOutput��ΪTrue
print arcpy.env.overwriteOutput
arcpy.env.overwriteOutput = True
print arcpy.env.overwriteOutput

# ���浱ǰ�������ã�����overwriteOutput��ΪFalse
arcpy.SaveSettings(os.path.join(os.path.expanduser("~"), "Desktop", "MyCustomSettings.xml"))
arcpy.env.overwriteOutput = False
print arcpy.env.overwriteOutput

# ���¶�ȡ�����Ļ��������ļ�
arcpy.LoadSettings(os.path.join(os.path.expanduser("~"), "Desktop", "MyCustomSettings.xml"))
print arcpy.env.overwriteOutput
