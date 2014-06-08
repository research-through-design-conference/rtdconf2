from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ingledow.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('microsite_2015.urls')),
    url(r'^about/', 'microsite_2015.views.about'),
    url(r'^attending/', 'microsite_2015.views.attending'),
    url(r'^organisation/', 'microsite_2015.views.organisation'),
)
