from django.forms import ModelForm, SelectDateWidget
from meetings.models import Meeting

class MeetingCreateForm(ModelForm):

    class Meta:
        model = Meeting
        fields = ['date', 'time', 'book', 'place']
        widgets = {
            'date': SelectDateWidget()
        }
