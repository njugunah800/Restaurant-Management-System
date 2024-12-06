from django import forms
from cityapp.models import Bookings,Contact
from cityapp.models import Feedback

class BookingsForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'occupation', 'rating', 'message','image']

