from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^stackedrow$', views.stackedrow, name='stackedrow'),
    url(r'^test$', views.test, name='test'),
    url(r'^geo$', views.geo, name='geo'),
    url(r'^graph$', views.graph, name='graph'),
    url(r'^graph2$', views.graph2, name='graph2'),
    url(r'^conversationgraph$', views.allconvograph, name='allconvograph'),
    url(r'^api/graphdata$', views.graphjson, name='graphjson'),
    url(r'^api/getdata$', views.getData, name='getdata'),
    # url(r'^data/fibre.json$', views.fibrejson, name='fibre'),
    # url(r'^data/all_probes.json$', views.allprobes, name='allprobes'),
]
