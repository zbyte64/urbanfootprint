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
from pydantic import BaseModel, Field, validator
from typing import Optional


class ImportPlacetypeComponent(BaseModel):
    category: Optional[str] = Field(default="")
    btid: Optional[int] = Field(default=0)
    color: Optional[str] = Field(default="")
    name: Optional[str] = Field(default="")


CROP_TYPES = {}
