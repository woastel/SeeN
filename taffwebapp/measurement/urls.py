from django.conf.urls import url
from . import views
from .views import climaticmeasurement

app_name = 'measurement'

urlpatterns = [
    # /euts/
    url(r'^measurement/$', climaticmeasurement.MainView.as_view() , name='cm_index'),

]
