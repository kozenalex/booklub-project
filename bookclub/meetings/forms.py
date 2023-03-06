from django.forms import ModelForm, SelectDateWidget, TimeInput
from meetings.models import Meeting

class MeetingCreateForm(ModelForm):

    class Meta:
        model = Meeting
        fields = ['date', 'time', 'book', 'place']
        widgets = {
            'date': SelectDateWidget(),
            'time': TimeInput(format='%H:%M', attrs={'type': 'time'})
        }
