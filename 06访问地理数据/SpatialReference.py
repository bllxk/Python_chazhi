# -*- coding:cp936 -*-
import arcpy, os

#   ���Ե�������ϵ
print u"���Ե�������ϵ"
spatialReference = arcpy.SpatialReference(4326)
arcpy.CreateFeatureclass_management(os.getcwd(), "TestGeographicSpatialReference.shp",
                                    spatial_reference=spatialReference)
desc = arcpy.Describe(os.getcwd() + os.sep + "TestGeographicSpatialReference.shp")
desc_spatialReference = desc.spatialReference
print u"�ռ�ο����ƣ�{0}\n�ռ�ο����ͣ�{1}\n�������룺{2}".format(desc_spatialReference.name, desc_spatialReference.type,
                                                 desc_spatialReference.factoryCode)

#   ����ͶӰ����ϵ
print u"����ͶӰ����ϵ"
spatialReference = arcpy.SpatialReference(4545)
arcpy.CreateFeatureclass_management(os.getcwd(), "TestProjectedSpatialReference.shp",
                                    spatial_reference=spatialReference)
desc = arcpy.Describe(os.getcwd() + os.sep + "TestProjectedSpatialReference.shp")
desc_spatialReference = desc.spatialReference
print u"�ռ�ο����ƣ�", desc_spatialReference.name
print u"�ռ�ο����ͣ�", desc_spatialReference.type
print u"�������룺", desc_spatialReference.factoryCode
print u"��������ϵ���룺", desc_spatialReference.GCSCode
print u"��������ϵ���ƣ�", desc_spatialReference.GCSName
print u"ͶӰ����ϵ���룺", desc_spatialReference.PCSCode
print u"ͶӰ����ϵ���ƣ�", desc_spatialReference.PCSName
print u"ͶӰ����ϵ���뾭�ߣ�", desc_spatialReference.centralMeridian
print u"ͶӰ���룺", desc_spatialReference.projectionCode
print u"ͶӰ���ƣ�", desc_spatialReference.projectionName
