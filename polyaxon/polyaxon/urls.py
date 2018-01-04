# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from polyaxon import views


API_V1 = 'api/v1'

api_patterns = [
    url(r'', include('clusters.urls', namespace='clusters')),
    url(r'', include('versions.urls', namespace='versions')),
    url(r'', include('users.api_urls', namespace='users')),
    # always include project last because of it's patterns
    url(r'', include('experiments.urls', namespace='experiments')),
    url(r'', include('repos.urls', namespace='repos')),
    url(r'', include('projects.urls', namespace='projects')),
]

urlpatterns = [
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^_admin/', include(admin.site.urls)),
    url(r'^_health/?$', views.HealthView.as_view(), name='health_check'),
    url(r'^{}/'.format(API_V1), include(api_patterns, namespace='v1')),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^app/.*/', views.ReactIndexView.as_view(), name='react-index'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
