import arcpy,os

# �������˵������ݿ�
arcpy.CreatePersonalGDB_management (os.getcwd(), "test.mdb")
# ����MyFeatureclass1��Featureclass2��Featureclass3Ҫ�����ݼ�
arcpy.CreateFeatureclass_management (os.getcwd()+os.sep+"test.mdb", "MyFeatureclass1","POLYGON")
arcpy.CreateFeatureclass_management (os.getcwd()+os.sep+"test.mdb", "Featureclass2","POLYGON")
arcpy.CreateFeatureclass_management (os.getcwd()+os.sep+"test.mdb", "Featureclass3","POINT")

# �оٴ����ĸ��˵������ݿ��е�Ҫ����
arcpy.env.workspace = os.getcwd()+os.sep+"test.mdb"
fcs = arcpy.ListFeatureClasses()
print("All Featureclasses :")
for fc in fcs :
    print(fc)

# �оٴ����ĸ��˵������ݿ��е�Ҫ���ࣨʹ��ͨ�����ֻ�о���My��ͷ��Ҫ������Ϊ��ģ�
fcs = arcpy.ListFeatureClasses("My*","Polygon")
print("Starts with My and Polygon :")
for fc in fcs :
    print(fc)


# �оٴ����ĸ��˵������ݿ��еĵ�Ҫ���� 
fcs = arcpy.ListFeatureClasses("","Point")
print("Point Featureclasses :")
for fc in fcs :
    print(fc)
arcpy.Delete_management(os.getcwd()+os.sep+"test.mdb")
