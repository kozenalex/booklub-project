from datetime import datetime

from meetings.models import Meeting
from articles.models import Article

class HomeContextMixin():

    def get_next_meeting():
        m = Meeting.objects.filter(date__gte=datetime.now().date())
        return m[0] if m else m
    
    def get_last_article():
        try:
            last_article = Article.objects.latest('id')
        except:
            last_article = None
        return last_article