from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'microsite_2015.views.home'),
)
