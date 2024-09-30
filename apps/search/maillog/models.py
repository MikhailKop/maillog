from django.db import models


class Log(models.Model):
    created = models.DateTimeField()
    int_id = models.CharField()
    str = models.CharField(blank=True, null=True)
    address = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log'


class Message(models.Model):
    created = models.DateTimeField()
    id = models.CharField(primary_key=True)
    int_id = models.CharField()
    str = models.CharField()
    status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message'
