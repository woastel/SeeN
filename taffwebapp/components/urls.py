from django.conf.urls import url
from . import views


app_name = 'components'

urlpatterns = [
    # incomming tag is /eut/

    url(r'^index/$',                     views.MainView.as_view() , name='index'),
    url(r'^complist/$',                  views.List_Component_View.as_view() , name='component_list'),
    url(r'^comp/(?P<pk>[0-9]+)/$',       views.Detail_Component_View.as_view(), name='component_detail'),

    # Create types (only used by admin )
    url(r'^comp/componentType/add/$',   views.Create_Component_Type_View.as_view() ,       name='create_componentType'),
    url(r'^comp/Vendor/add/$',          views.Create_Vendor_View.as_view() ,  name='create_vendor'),

    # Create urls
    url(r'^comp/chassis/add/$',         views.Create_Chassis_View.as_view() ,       name='create_chassis'),
    url(r'^comp/chassisAddOn/add/$',    views.Create_ChassisAddOn_View.as_view() ,  name='create_chassisAddOn'),
    url(r'^comp/motherboard/add/$',     views.Create_Motherboard_View.as_view() ,   name='create_motherboard'),
    url(r'^comp/cpu/add/$',             views.Create_CPU_View.as_view() ,           name='create_cpu'),
    url(r'^comp/memory/add/$',          views.Create_Memory_View.as_view() ,        name='create_memory'),
    url(r'^comp/psu/add/$',             views.Create_PSU_View.as_view() ,           name='create_psu'),
    url(r'^comp/hdd/add/$',             views.Create_HDD_View.as_view() ,           name='create_hdd'),
    url(r'^comp/heatsink/add/$',        views.Create_HeatSink_View.as_view() ,      name='create_heatsink'),
    url(r'^comp/fan/add/$',             views.Create_Fan_View.as_view() ,           name='create_fan'),
    url(r'^comp/cable/add/$',           views.Create_Cable_View.as_view() ,         name='create_cable'),
    url(r'^comp/pcba/add/$',            views.Create_Pcba_View.as_view() ,          name='create_pcba'),
    url(r'^comp/pciectrl/add/$',        views.Create_PcieCtrl_View.as_view() ,      name='create_pciectrl'),
    ]
