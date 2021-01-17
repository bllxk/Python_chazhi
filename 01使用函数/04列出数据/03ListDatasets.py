import arcpy,os

# �������˵������ݿ�
arcpy.CreatePersonalGDB_management (os.getcwd(), "test.mdb")
# ����MyFeatureDataset1��MyFeatureDataset2��FeatureDataset3Ҫ�����ݼ�
arcpy.CreateFeatureDataset_management (os.getcwd()+os.sep+"test.mdb", "MyFeatureDataset1")
arcpy.CreateFeatureDataset_management (os.getcwd()+os.sep+"test.mdb", "MyFeatureDataset2")
arcpy.CreateFeatureDataset_management (os.getcwd()+os.sep+"test.mdb", "FeatureDataset3")
# ��MyFeatureDataset1Ҫ�����ݼ��д�������
arcpy.CreateTopology_management (os.getcwd()+os.sep+"test.mdb"+os.sep+"MyFeatureDataset1", "MyTopology")

# �оٴ����ĸ��˵������ݿ��е�Ҫ�����ݼ�
arcpy.env.workspace = os.getcwd()+os.sep+"test.mdb"
datasets = arcpy.ListDatasets("","Feature")
for dataset in datasets :
    print(dataset)
print("")

# �оٴ����ĸ��˵������ݿ��е�Ҫ�����ݼ���ʹ��ͨ�����ֻ�о���My��ͷ�ģ�
datasets = arcpy.ListDatasets("My*","Feature")
for dataset in datasets :
    print(dataset)
print("")

# �о�MyFeatureDataset1Ҫ�����ݼ��е�����    
arcpy.env.workspace = os.getcwd()+os.sep+"test.mdb"+os.sep+"MyFeatureDataset1"
datasets = arcpy.ListDatasets("","Topology")
for dataset in datasets :
    print(dataset)
arcpy.Delete_management(os.getcwd()+os.sep+"test.mdb")
