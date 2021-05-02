from django.contrib import admin
from . import models

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['name','email','picture_tag','presenter','topic_to_Present']
class CommitteeMemberAdmin(admin.ModelAdmin):
    list_display = ['name','role','picture_tag']

class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name','location','picture_tag']

class ProgramAdmin(admin.ModelAdmin):
    list_display = ['name','day','speaker','start_time','end_time','picture_tag']

class EventAdmin(admin.ModelAdmin):
    list_display = ['name','venue','Start_date','End_date','picture_tag']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','message']


# Register your models here.

admin.site.register(models.Partner,PartnerAdmin)
admin.site.register(models.Event,EventAdmin)
admin.site.register(models.CommitteeMember,CommitteeMemberAdmin)
admin.site.register(models.Participant,ParticipantAdmin)
admin.site.register(models.Day)
admin.site.register(models.Program,ProgramAdmin)
admin.site.register(models.Contact,ContactAdmin)

