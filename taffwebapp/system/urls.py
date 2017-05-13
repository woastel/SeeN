from django.conf.urls import url
from . import views

app_name = 'system'

urlpatterns = [
    # incomming tag is /eut/

    #
    #  Eut URLs
    # ~~~~~~~~~~~~~~~
    url(r'^system_list/$',              views.Main_View.as_view(),                  name='system_index'),

    # Create Views
    url(r'^create/system/$',            views.Create_System_View.as_view(),         name="create_system"),
    url(r'^create/systemModel/$',       views.Create_SystemModel_View.as_view(),    name="create_system_model"),
    url(r'^create/milestone/$',         views.Create_Milestone_View.as_view(),      name="create_milestone"),
    url(r'^create/MSDBConnection/$',    views.Create_MSDBConnection_View.as_view(), name="create_msdb_connection"),


    ]
