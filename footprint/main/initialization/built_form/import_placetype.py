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

from pydantic import BaseModel, Field
from typing import Optional


class ImportedPlacetype(BaseModel):
    name: Optional[str] = Field(default="")
    clean_name: Optional[str] = Field(default="")
    color: Optional[str] = Field(default="")
    intersection_density: Optional[float] = Field(default=0.0)
