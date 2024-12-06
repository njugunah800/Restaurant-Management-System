from django.contrib import admin
from cityapp.models import User,Contact,Bookings,Member,Feedback

# Register your models here.
admin.site.register(User)
admin.site.register(Contact)
admin.site.register(Bookings)
admin.site.register(Member)
admin.site.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'occupation', 'rating', 'message', 'image')
