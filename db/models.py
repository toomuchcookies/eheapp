from django.db import models

# Create your models here.
class Kandidat (models.Model):
	name = models.CharField (max_length=200)
	geburtsdatum = models.DateField ('geburtstag', blank=True)
	email = models.EmailField (blank=True)
	facebook = models.CharField (max_length=100, blank=True)
	beruf = models.CharField (max_length=100, blank=True)
	stadt = models.CharField (max_length=100, blank=True)
	bemerkungen = models.TextField (blank=True)
	beschreibung = models.TextField (blank=True)
	vorgeschlagen_von = models.ForeignKey ('Mitglied')
	geschlecht = models.CharField(max_length=1, choices=(('M', 'Mann'), ('F', 'Frau')))
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		verbose_name_plural = "kandidaten"

class Interview (models.Model):
	kandidat = models.ForeignKey ('Kandidat')
	interviewer = models.ForeignKey ('Mitglied')
	interview = models.TextField ()
	datum = models.DateTimeField ()
	
	def __unicode__(self):
		return 'Interview: %s, %s' % (str(self.kandidat), str(self.interviewer))
	
	class Meta:
		verbose_name_plural = "Interviews"

class Mitglied (models.Model):
	name = models.CharField (max_length=200)
	email = models.EmailField ()
	facebook = models.CharField (max_length=100, blank=True)
	skype = models.CharField (max_length=100)
	telefon1 = models.CharField (max_length=30, blank=True)
	telefon2 = models.CharField (max_length=30, blank=True)
	aktiv = models.NullBooleanField ()
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		verbose_name_plural = "Mitglieder"

class Protokoll (models.Model):
	protokoll = models.TextField ()
	datum = models.DateTimeField ()
	
	def __unicode__(self):
		return str(self.datum)
	
	class Meta:
		verbose_name_plural = "Protokolle"

class Teilnehmer (models.Model):
	mitglied = models.ForeignKey ('Mitglied')
	protokoll = models.ForeignKey ('Protokoll')
	
	def __unicode__(self):
		return str(self.mitglied)

	class Meta:
		verbose_name_plural = "Teilnehmer"

class Paarvorschlag (models.Model):
	mann = models.ForeignKey ('Kandidat', limit_choices_to={'geschlecht': 'M'}, related_name='mannvorschlaege')
	frau = models.ForeignKey ('Kandidat', limit_choices_to={'geschlecht': 'F'}, related_name='frauvorschlaege')
	datum_vorschlag_erfolgt = models.DateField ()
	erfolg = models.IntegerField (choices=((-1, 'Noch nicht vorgeschlagen'), (0, 'Noch keine Rueckmeldung.'), (1, 'Frau hat abgelehnt.'), (2, 'Mann hat abgelehnt.'), (3, 'Beide haben abgelehnt.'), (4, 'Beide haben zugestimmt.'), (5, 'Verheiratet.')))
	bemerkungen = models.TextField (blank=True)
	protokoll = models.ForeignKey ('Protokoll', blank=True)
	
	def __unicode__(self):
		return 'Paarvorschlag, %s - %s' % (str(self.mann), str(self.frau))
	
	class Meta:
		verbose_name_plural = "Paarvorschlaege"


