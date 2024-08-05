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

from pydantic import BaseModel, Field
from typing import Optional


#    BTID,Building_Type,
# Urban Mixed Use,Urban Residential,Urban Commercial,City Mixed Use,City Residential,City Commercial,
# Town Mixed Use,Town Residential,Town Commercial,Village Mixed Use,Village Residential,Village Commercial,
# Neighborhood Residential,Neighborhood Low,Office Focus,Mixed Office and R&D,Office/Industrial,Industrial Focus,
# Low-Density Employment Park,High Intensity Activity Center,Mid Intensity Activity Center,
# Low Intensity Retail-Centered N'Hood,Retail: Strip Mall/ Big Box,Industrial/Office/Res Mixed High,
# Industrial/Office/Res Mixed Low,Suburban Multifamily,Suburban Mixed Residential,Residential Subdivision,
# Large Lot Residential Area,Rural Residential,Rural Ranchettes,Rural Employment,Campus/ University,
# Institutional,Parks & Open Space,BuildingType Name,Gross_Net_Flag
class ImportPlacetypeComponent(BaseModel):
    category: str = Field(default="")
    btid: int = Field(default=0)
    color: str = Field(default="")
    name: str = Field(default="")
    urban_mixed_use: float = Field(default=0.0)
    urban_residential: float = Field(default=0.0)
    urban_commercial: float = Field(default=0.0)
    city_mixed_use: float = Field(default=0.0)
    city_residential: float = Field(default=0.0)
    city_commercial: float = Field(default=0.0)
    town_mixed_use: float = Field(default=0.0)
    town_residential: float = Field(default=0.0)
    town_commercial: float = Field(default=0.0)
    village_mixed_use: float = Field(default=0.0)
    village_residential: float = Field(default=0.0)
    village_commercial: float = Field(default=0.0)
    neighborhood_residential: float = Field(default=0.0)
    neighborhood_low: float = Field(default=0.0)
    office_focus: float = Field(default=0.0)
    mixed_office_and_r_and_d: float = Field(default=0.0)
    office_industrial: float = Field(default=0.0)
    industrial_focus: float = Field(default=0.0)
    low_density_employment_park: float = Field(default=0.0)
    high_intensity_activity_center: float = Field(default=0.0)
    mid_intensity_activity_center: float = Field(default=0.0)
    low_intensity_retail_centered_neighborhood: float = Field(default=0.0)
    retail_strip_mall_big_box: float = Field(default=0.0)
    industrial_office_residential_mixed_high: float = Field(default=0.0)
    industrial_office_residential_mixed_low: float = Field(default=0.0)
    suburban_multifamily: float = Field(default=0.0)
    suburban_mixed_residential: float = Field(default=0.0)
    residential_subdivision: float = Field(default=0.0)
    large_lot_residential: float = Field(default=0.0)
    rural_residential: float = Field(default=0.0)
    rural_ranchettes: float = Field(default=0.0)
    rural_employment: float = Field(default=0.0)
    campus_or_university: float = Field(default=0.0)
    institutional: float = Field(default=0.0)
    parks_and_open_space: float = Field(default=0.0)
    blank: float = Field(default=0.0)
