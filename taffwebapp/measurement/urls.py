from django.conf.urls import url
from . import views

from .views import measurement
from .views import measurement_climatic
from .views import measurement_emi

app_name = 'measurement'

urlpatterns = [
    # /euts/
    url(r'^measurement/$',          measurement.IndexView.as_view() ,           name='m_index'),

    url(r'^measurement_climatic/$', measurement_climatic.IndexView.as_view() ,  name='mc_index'),

    url(r'^measurement_emi/$',      measurement_emi.IndexView.as_view() ,       name='memi_index'),


]
