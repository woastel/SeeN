from django.conf.urls import url
from . import views
from .views import measurement_climatic

app_name = 'measurement'

urlpatterns = [
    # /euts/
    url(r'^measurement/$', measurement_climatic.MainView.as_view() , name='mc_index'),

]
