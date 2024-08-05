# UrbanFootprint v1.5
# Copyright (C) 2017 Calthorpe Analytics
#
# This file is part of UrbanFootprint version 1.5
#
# UrbanFootprint is distributed under the terms of the GNU General
# Public License version 3, as published by the Free Software Foundation. This
# code is distributed WITHOUT ANY WARRANTY, without implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License v3 for more details; see <http://www.gnu.org/licenses/>.


from django.urls import include, path as url
from django.contrib import admin
from django.conf import settings
from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = []

if settings.DEBUG:
    urlpatterns += [
        (
            r"^media/(?P<path>.*)$",
            "django.views.static.serve",
            {"document_root": settings.STATIC_DOC_ROOT},
        ),
    ]

urlpatterns += [
    # ('^$', redirect_to,  {'url': '/main/', 'permanent': False}),
    # url(r'^grappelli/', include('grappelli.urls')),
    url(r"^admin/doc/", include("django.contrib.admindocs.urls")),
    url(r"^admin/", admin.site.urls),
    url(r"^footprint/", include("footprint.main.urls")),
    # url(r"^draft/", include("draft.urls")),
    # url(r"^accounts/login/$", include("django.contrib.auth.views.login")),
    # url(r"^accounts/logout/$", include("django.contrib.auth.views.logout")),
    url(r"^$", RedirectView.as_view(url="footprint/")),
]
