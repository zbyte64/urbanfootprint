# coding=utf-8

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

__author__ = "calthorpe_analytics"


from django.contrib.gis.db import models
from footprint.main.models.built_form.urban.building_attribute_set import (
    BuildingAttributeSet,
)


class BuildingAttributeSetMixin(models.Model):
    class Meta:
        abstract = True
        app_label = "main"

    building_attribute_set = models.ForeignKey(
        BuildingAttributeSet, null=True, on_delete=models.PROTECT
    )
