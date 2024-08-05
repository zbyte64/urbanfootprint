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

#    BTID,Building_Type,
# Urban Mixed Use,Urban Residential,Urban Commercial,City Mixed Use,City Residential,City Commercial,
# Town Mixed Use,Town Residential,Town Commercial,Village Mixed Use,Village Residential,Village Commercial,
# Neighborhood Residential,Neighborhood Low,Office Focus,Mixed Office and R&D,Office/Industrial,Industrial Focus,
# Low-Density Employment Park,High Intensity Activity Center,Mid Intensity Activity Center,
# Low Intensity Retail-Centered N'Hood,Retail: Strip Mall/ Big Box,Industrial/Office/Res Mixed High,
# Industrial/Office/Res Mixed Low,Suburban Multifamily,Suburban Mixed Residential,Residential Subdivision,
# Large Lot Residential Area,Rural Residential,Rural Ranchettes,Rural Employment,Campus/ University,
# Institutional,Parks & Open Space,BuildingType Name,Gross_Net_Flag
from pydantic import BaseModel, Field
from typing import Optional


class ImportPlacetypeComponent(BaseModel):
    category: Optional[str] = Field(default="")
    btid: Optional[int] = Field(default=0)
    color: Optional[str] = Field(default="")
    name: Optional[str] = Field(default="")
    urban_mixed_use: Optional[float] = Field(default=0.0)
    urban_residential: Optional[float] = Field(default=0.0)
    urban_commercial: Optional[float] = Field(default=0.0)
    city_mixed_use: Optional[float] = Field(default=0.0)
    city_residential: Optional[float] = Field(default=0.0)
    city_commercial: Optional[float] = Field(default=0.0)
    town_mixed_use: Optional[float] = Field(default=0.0)
    town_residential: Optional[float] = Field(default=0.0)
    town_commercial: Optional[float] = Field(default=0.0)
    village_mixed_use: Optional[float] = Field(default=0.0)
    village_residential: Optional[float] = Field(default=0.0)
    village_commercial: Optional[float] = Field(default=0.0)
    neighborhood_residential: Optional[float] = Field(default=0.0)
    neighborhood_low: Optional[float] = Field(default=0.0)
    office_focus: Optional[float] = Field(default=0.0)
    mixed_office_and_r_and_d: Optional[float] = Field(default=0.0)
    office_industrial: Optional[float] = Field(default=0.0)
    industrial_focus: Optional[float] = Field(default=0.0)
    low_density_employment_park: Optional[float] = Field(default=0.0)
    high_intensity_activity_center: Optional[float] = Field(default=0.0)
    mid_intensity_activity_center: Optional[float] = Field(default=0.0)
    low_intensity_retail_centered_neighborhood: Optional[float] = Field(default=0.0)
    retail_strip_mall_big_box: Optional[float] = Field(default=0.0)
    industrial_office_residential_mixed_high: Optional[float] = Field(default=0.0)
    industrial_office_residential_mixed_low: Optional[float] = Field(default=0.0)
    suburban_multifamily: Optional[float] = Field(default=0.0)
    suburban_mixed_residential: Optional[float] = Field(default=0.0)
    residential_subdivision: Optional[float] = Field(default=0.0)
    large_lot_residential: Optional[float] = Field(default=0.0)
    rural_residential: Optional[float] = Field(default=0.0)
    rural_ranchettes: Optional[float] = Field(default=0.0)
    rural_employment: Optional[float] = Field(default=0.0)
    campus_or_university: Optional[float] = Field(default=0.0)
    institutional: Optional[float] = Field(default=0.0)
    parks_and_open_space: Optional[float] = Field(default=0.0)
