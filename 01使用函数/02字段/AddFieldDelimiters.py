import arcpy,os
field_name="Id"

#�����ռ�Ϊ�ļ���
workspace=os.getcwd()
print arcpy.AddFieldDelimiters(workspace,field_name)

##ʵ��֤����ӷָ��ʱ��ֻ���ļ���·���ͺ�׺�йأ������Ƿ���ڡ��������г��ԡ�
# �����ռ�Ϊ���˵������ݿ⣬ע�͵���Ϊ����һ�����˵������ݿ�
#arcpy.CreatePersonalGDB_management (os.getcwd(), "test.mdb")
workspace=os.getcwd()+os.sep+"test.mdb"
print arcpy.AddFieldDelimiters(workspace,field_name)

# �����ռ�Ϊ�ļ��������ݿ⣬ע�͵���Ϊ����һ���ļ��������ݿ�
#arcpy.CreateFileGDB_management (os.getcwd(), "test.gdb")
workspace=os.getcwd()+os.sep+"test.gdb"
print arcpy.AddFieldDelimiters(workspace,field_name)

