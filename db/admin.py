from EheApp.db.models import Kandidat, Interview, Mitglied, Protokoll, Teilnehmer, Paarvorschlag
from django.contrib import admin

class InterviewAdmin (admin.ModelAdmin):
	date_hierarchy = 'datum'
admin.site.register(Interview, InterviewAdmin)
admin.site.register(Mitglied)
#admin.site.register(Teilnehmer)

class PaarvorschlagAdmin (admin.ModelAdmin):
	search_fields = ['mann__name','frau__name']
admin.site.register(Paarvorschlag, PaarvorschlagAdmin)

class TeilnehmerInline (admin.TabularInline):
	model = Teilnehmer
	extra = 3
class ProtokollAdmin (admin.ModelAdmin):
	inlines = [TeilnehmerInline]
admin.site.register(Protokoll, ProtokollAdmin)

class FrauvorschlagInline (admin.TabularInline):
	model = Paarvorschlag
	fk_name = 'mann'
	extra = 0
	#readonly_fields = ['mann','protokoll','bemerkungen','erfolg','datum_vorschlag_erfolgt']
class MannvorschlagInline (admin.TabularInline):
	model = Paarvorschlag
	fk_name = 'frau'
	extra = 0
	#readonly_fields = ['frau','protokoll','bemerkungen','erfolg','datum_vorschlag_erfolgt']
class KandidatAdmin (admin.ModelAdmin):
	list_display = ('name', 'geburtsdatum', 'stadt')
	list_filter = ['geschlecht','status']
	search_fields = ['name']
	inlines = [MannvorschlagInline, FrauvorschlagInline]
	def get_formsets(self, request, obj=None):
		if obj:
			if obj.geschlecht=='M':
				for inline in self.inline_instances:
					if isinstance(inline, FrauvorschlagInline):
						yield inline.get_formset(request, obj)
			else:
				for inline in self.inline_instances:
					if isinstance(inline, MannvorschlagInline):
						yield inline.get_formset(request, obj)
admin.site.register(Kandidat, KandidatAdmin)
