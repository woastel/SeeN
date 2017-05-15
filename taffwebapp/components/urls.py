from django.conf.urls import url
from . import views


app_name = 'components'

urlpatterns = [
    # incomming tag is /eut/

    url(r'^index/$',                     views.MainView.as_view() , name='index'),
    url(r'^complist/$',                  views.MainView.as_view() , name='component_list'),
    url(r'^comp/add/$',                  views.Create_Chassis_View.as_view() , name='component_add'),
    url(r'^comp/(?P<pk>[0-9]+)/$',       views.MainView.as_view(), name='component_detail'),

    ]
