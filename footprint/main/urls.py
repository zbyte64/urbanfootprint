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
from django.views.generic import TemplateView
from django.conf import settings

from footprint.main.admin.views import ufadmin, config_entities
from footprint.main.publishing.data_export_publishing import (
    export_layer,
    get_export_result,
    export_query_results,
    export_query_summary,
    export_result_table,
)
from footprint.main.user_management.views import users, user, add_user, login, logout
from footprint.upload_manager.views import upload, upload_test, upload_results
from footprint.main.views import get_project_data, get_scenario_data

urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="footprint/index.html")),
    url(r"^(?P<api_key>[^/]+)/export_layer/(?P<layer_id>[^/]+)", export_layer),
    url(r"^(?P<api_key>[^/]+)/get_export_result/(?P<hash_id>[^/]+)", get_export_result),
    url(
        r"^(?P<api_key>[^/]+)/export_query_results/(?P<layer_selection_unique_id>[^/]+)",
        export_query_results,
    ),
    url(
        r"^(?P<api_key>[^/]+)/export_query_summary/(?P<layer_selection_unique_id>[^/]+)",
        export_query_summary,
    ),
    url(
        r"^(?P<api_key>[^/]+)/export_result_table/(?P<result_id>[^/]+)",
        export_result_table,
    ),
    # User Management
    url(r"^users/$", users),
    url(r"^user/(?P<user_id>\d*)", user),
    url(r"^add_user/$", add_user),
    # Authentication
    url(r"^logout/$", logout),
    url(r"^login/$", login),
    # Administration
    url(r"^ufadmin/", include("footprint.main.admin.urls")),
    # File Upload
    url(r"^upload/", upload),
    url(r"^upload_test/", upload_test),
    url(r"^upload_results/", upload_results),
    # Manual API urls
    url(r"^api/v2/project/", get_project_data),
    url(r"^api/v2/scenario/", get_scenario_data),
]
# Cross-domain proxying if we need it
# urlpatterns += patterns('',
#    (r'^(?P<url>.*)$', 'httpproxy.views.proxy'),
# )
# urlpatterns += staticfiles_urlpatterns() #this is meant for debug only

# from celery.task import PingTask
# from djcelery import views as celery_views

# celery webhook
# urlpatterns += patterns("",
#    url(r'^apply/(?P<task_name>.+?)/', celery_views.apply),
#    url(r'^ping/', celery_views.task_view(PingTask)),
#    url(r'^(?P<task_id>[\w\d\-]+)/done/?$', celery_views.is_task_successful,
#        name="celery-is_task_successful"),
#    url(r'^(?P<task_id>[\w\d\-]+)/status/?$', celery_views.task_status,
#        name="celery-task_status"),
# )
