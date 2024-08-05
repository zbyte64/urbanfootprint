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


class ImportPrimaryComponent(BaseModel):
    id: Optional[int] = Field(default=0)
    source: Optional[str] = Field(default="")
    website: Optional[str] = Field(default="")
    placetype_component: Optional[str] = Field(default="")
    name: Optional[str] = Field(default="")
    address: Optional[str] = Field(default="")

    vacancy_rate: Optional[float] = Field(default=0.0)
    household_size: Optional[float] = Field(default=0.0)

    percent_single_family_large_lot: Optional[float] = Field(default=0.0)
    percent_single_family_small_lot: Optional[float] = Field(default=0.0)
    percent_attached_single_family: Optional[float] = Field(default=0.0)
    percent_multifamily_2_to_4: Optional[float] = Field(default=0.0)
    percent_multifamily_5_plus: Optional[float] = Field(default=0.0)

    percent_office_services: Optional[float] = Field(default=0.0)
    percent_education_services: Optional[float] = Field(default=0.0)
    percent_medical_services: Optional[float] = Field(default=0.0)
    percent_public_admin: Optional[float] = Field(default=0.0)

    percent_retail_services: Optional[float] = Field(default=0.0)
    percent_restaurant: Optional[float] = Field(default=0.0)
    percent_accommodation: Optional[float] = Field(default=0.0)
    percent_arts_entertainment: Optional[float] = Field(default=0.0)
    percent_other_services: Optional[float] = Field(default=0.0)

    percent_manufacturing: Optional[float] = Field(default=0.0)
    percent_transport_warehouse: Optional[float] = Field(default=0.0)
    percent_wholesale: Optional[float] = Field(default=0.0)
    percent_construction_utilities: Optional[float] = Field(default=0.0)

    percent_agriculture: Optional[float] = Field(default=0.0)
    percent_extraction: Optional[float] = Field(default=0.0)

    percent_of_placetype_component: Optional[float] = Field(default=0.0)
    lot_size_square_feet: Optional[float] = Field(default=0.0)
    floors: Optional[float] = Field(default=0.0)

    total_far: Optional[float] = Field(default=0.0)

    residential_efficiency: Optional[float] = Field(default=0.0)
    residential_square_feet_per_unit: Optional[float] = Field(default=0.0)

    retail_efficiency: Optional[float] = Field(default=0.0)
    retail_square_feet_per_unit: Optional[float] = Field(default=0.0)

    office_efficiency: Optional[float] = Field(default=0.0)
    office_square_feet_per_unit: Optional[float] = Field(default=0.0)

    industrial_efficiency: Optional[float] = Field(default=0.0)
    industrial_square_feet_per_unit: Optional[float] = Field(default=0.0)

    average_parking_space_square_feet: Optional[float] = Field(default=0.0)
    surface_parking_spaces: Optional[float] = Field(default=0.0)
    above_ground_parking_spaces: Optional[float] = Field(default=0.0)
    below_ground_parking_spaces: Optional[float] = Field(default=0.0)

    building_footprint_square_feet: Optional[float] = Field(default=0.0)
    surface_parking_square_feet: Optional[float] = Field(default=0.0)
    hardscape_other_square_feet: Optional[float] = Field(default=0.0)

    irrigated_softscape_square_feet: Optional[float] = Field(default=0.0)
    nonirrigated_softscape_square_feet: Optional[float] = Field(default=0.0)

    irrigated_percent: Optional[float] = Field(default=0.0)

    id2: Optional[int] = Field(default=0)
