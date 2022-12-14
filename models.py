# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class ClientDetails(models.Model):
    loginid = models.IntegerField()
    empname = models.CharField(max_length=50)
    empmobile = models.CharField(max_length=50)
    empemailid = models.CharField(max_length=50)
    isactive = models.IntegerField()
    creationdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client_details'


class Clientmaster(models.Model):
    loginid = models.IntegerField()
    client_company_name = models.CharField(max_length=50)
    pan_no = models.CharField(max_length=10)
    registration_no = models.CharField(max_length=50)
    gst_no = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    contact_person_name = models.CharField(max_length=300, blank=True, null=True)
    contact_person_mobileno = models.CharField(max_length=200, blank=True, null=True)
    contact_person_email = models.CharField(max_length=500, blank=True, null=True)
    isactive = models.IntegerField()
    creationdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'clientmaster'


class ContractDocx(models.Model):
    docx_id = models.AutoField(primary_key=True)
    document_summary_id = models.IntegerField(blank=True, null=True)
    document_login_id = models.IntegerField()
    document_path = models.CharField(max_length=255, blank=True, null=True)
    docx_file_path = models.CharField(max_length=255)
    isactive = models.IntegerField(blank=True, null=True)
    creationdate = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contract_docx'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DocTypeMaster(models.Model):
    name = models.CharField(max_length=50)
    isactive = models.IntegerField()
    creationdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'doc_type_master'


class Loginmaster(models.Model):
    companyid = models.IntegerField()
    loginid = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=100)
    normalpwd = models.CharField(max_length=50)
    user_role = models.IntegerField()
    user_permission = models.CharField(max_length=250)
    isactive = models.IntegerField()
    creationdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'loginmaster'


class States(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    isactive = models.IntegerField()
    creationdate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'states'


class UserPermissionDetails(models.Model):
    user_permission_id = models.AutoField(primary_key=True)
    permission_id = models.IntegerField()
    login_id = models.IntegerField()
    permission_status = models.CharField(max_length=1)
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_permission_details'
