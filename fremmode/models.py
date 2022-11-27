from django.db import models

# pylint: disable=missing-class-docstring

class Fremmode(models.Model):
    'Fremmode'
    Date = models.DateField()
    Medlem = models.IntegerField()
    State = models.IntegerField()
    Reason = models.IntegerField()
    class Meta:
        db_table = "Fremmode"

class Medlemmer(models.Model):
    'medlemmer'
    Medlemsnummer = models.IntegerField(primary_key=True)
    Status = models.IntegerField()
    Fornavn = models.CharField(max_length=50)
    Efternavn = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Mobil = models.CharField(max_length=12)
    Text = models.CharField(max_length=100)
    Onsdag = models.IntegerField()
    BetalingsDato = models.DateField()
    Lordag = models.IntegerField()
    Tirsdag = models.IntegerField()

    class Meta:
        db_table = "medlemmer"

class States(models.Model):
    'states'
    StateID = models.IntegerField()
    State = models.CharField(max_length=20)
    HandOvertext = models.CharField(max_length=30)
    Image = models.CharField(max_length=30)
    class Meta:
        db_table = "States"
 