from django.conf.urls import url
from . import views

app_name = 'system'

urlpatterns = [
    # incomming tag is /eut/

    #
    #  Eut URLs
    # ~~~~~~~~~~~~~~~
    url(r'^mainView/$',                 views.Main_View.as_view(),                  name='system_index'),


    url(r'^systemlist/$',                   views.List_All_Systems.as_view(),           name='system_list'),
    url(r'^systemdetail/(?P<pk>[0-9]+)/$',  views.Detail_System_View.as_view(),         name='system_detail'),

    # Create Views
    url(r'^create/system/$',                    views.Create_System_View.as_view(),         name="create_system"),
    url(r'^update/system/(?P<pk>[0-9]+)/$',     views.Update_System_View.as_view(),         name="update_system"),
    url(r'^delete/system/(?P<pk>[0-9]+)/$',     views.Delete_System_View.as_view(),         name="delete_system"),


    url(r'^create/systemModel/$',       views.Create_SystemModel_View.as_view(),    name="create_system_model"),
    url(r'^create/milestone/$',         views.Create_Milestone_View.as_view(),      name="create_milestone"),
    url(r'^create/MSDBConnection/$',    views.Create_MSDBConnection_View.as_view(), name="create_msdb_connection"),


    ]
