from django.db import models
from django.contrib.postgres.fields import JSONField


class OCDSReleaseJSON(models.Model):
    _DATABASE = "bluetail"
    ocid = models.TextField(primary_key=True)
    release_id = models.TextField()
    release_json = JSONField(null=True)

    class Meta:
        app_label = 'bluetail'
        db_table = 'bluetail_ocds_release_json'
        managed = False


class BODSPersonStatementJSON(models.Model):
    """
    Model to store BODS Person Statement JSON.
    http://standard.openownership.org/en/0.2.0/schema/schema-browser.html#person-statement
    """
    _DATABASE = "bluetail"
    statement_id = models.TextField(primary_key=True)
    statement_json = JSONField()

    class Meta:
        app_label = 'bluetail'
        db_table = 'bluetail_bods_personstatement_json'
        managed = False



class BODSEntityStatementJSON(models.Model):
    """
    Model to store BODS Entity Statement JSON.
    http://standard.openownership.org/en/0.2.0/schema/schema-browser.html#entity-statement
    """
    _DATABASE = "bluetail"
    statement_id = models.TextField(primary_key=True)
    statement_json = JSONField()

    class Meta:
        app_label = 'bluetail'
        db_table = 'bluetail_bods_entitystatement_json'
        managed = False


class BODSOwnershipStatementJSON(models.Model):
    """
    Model to store BODS Ownership-or-control Statement JSON.
    http://standard.openownership.org/en/0.2.0/schema/schema-browser.html#ownership-or-control-statement
    """
    _DATABASE = "bluetail"
    statement_id = models.TextField(primary_key=True)
    statement_json = JSONField(null=True)

    class Meta:
        app_label = 'bluetail'
        db_table = 'bluetail_bods_ownershipstatement_json'
        managed = False

