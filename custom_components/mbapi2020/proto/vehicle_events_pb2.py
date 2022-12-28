# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vehicle-events.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import custom_components.mbapi2020.proto.service_activation_pb2 as service__activation__pb2
import custom_components.mbapi2020.proto.user_events_pb2 as user__events__pb2
import custom_components.mbapi2020.proto.vehicle_commands_pb2 as vehicle__commands__pb2
import custom_components.mbapi2020.proto.protos_pb2 as protos__pb2
import custom_components.mbapi2020.proto.vehicleapi_pb2 as vehicleapi__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14vehicle-events.proto\x12\x05proto\x1a\x18service-activation.proto\x1a\x11user-events.proto\x1a\x16vehicle-commands.proto\x1a\x0cprotos.proto\x1a\x10vehicleapi.proto\"\x84\x02\n\tVEPUpdate\x12\x17\n\x0fsequence_number\x18\x01 \x01(\x05\x12\x0b\n\x03vin\x18\x02 \x01(\t\x12\x13\n\x0b\x66ull_update\x18\x0f \x01(\x08\x12\x16\n\x0e\x65mit_timestamp\x18\n \x01(\x03\x12\x1c\n\x14\x65mit_timestamp_in_ms\x18\x0e \x01(\x03\x12\x34\n\nattributes\x18\x0b \x03(\x0b\x32 .proto.VEPUpdate.AttributesEntry\x1aP\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x1d.proto.VehicleAttributeStatus:\x02\x38\x01\"\xb1\x14\n\x16VehicleAttributeStatus\x12\x15\n\ttimestamp\x18\x01 \x01(\x03\x42\x02\x18\x01\x12\x17\n\x0ftimestamp_in_ms\x18\n \x01(\x03\x12\x0f\n\x07\x63hanged\x18\x02 \x01(\x08\x12\x0e\n\x06status\x18\x03 \x01(\x05\x12\x13\n\x0bservice_ids\x18\x1e \x03(\x05\x12\x15\n\rdisplay_value\x18\x0b \x01(\t\x12^\n\x1b\x63ombustion_consumption_unit\x18\x0c \x01(\x0e\x32\x37.proto.VehicleAttributeStatus.CombustionConsumptionUnitH\x00\x12P\n\x14gas_consumption_unit\x18\r \x01(\x0e\x32\x30.proto.VehicleAttributeStatus.GasConsumptionUnitH\x00\x12`\n\x1c\x65lectricity_consumption_unit\x18\x0e \x01(\x0e\x32\x38.proto.VehicleAttributeStatus.ElectricityConsumptionUnitH\x00\x12R\n\x13speed_distance_unit\x18\x0f \x01(\x0e\x32/.proto.VehicleAttributeStatus.SpeedDistanceUnitB\x02\x18\x01H\x00\x12=\n\nspeed_unit\x18\x19 \x01(\x0e\x32\'.proto.VehicleAttributeStatus.SpeedUnitH\x00\x12\x43\n\rdistance_unit\x18\x1a \x01(\x0e\x32*.proto.VehicleAttributeStatus.DistanceUnitH\x00\x12I\n\x10temperature_unit\x18\x10 \x01(\x0e\x32-.proto.VehicleAttributeStatus.TemperatureUnitH\x00\x12\x43\n\rpressure_unit\x18\x11 \x01(\x0e\x32*.proto.VehicleAttributeStatus.PressureUnitH\x00\x12=\n\nratio_unit\x18\x12 \x01(\x0e\x32\'.proto.VehicleAttributeStatus.RatioUnitH\x00\x12\x46\n\x0f\x63lock_hour_unit\x18\x13 \x01(\x0e\x32+.proto.VehicleAttributeStatus.ClockHourUnitH\x00\x12\x13\n\tint_value\x18\x04 \x01(\x03H\x01\x12\x14\n\nbool_value\x18\x05 \x01(\x08H\x01\x12\x16\n\x0cstring_value\x18\x06 \x01(\tH\x01\x12\x16\n\x0c\x64ouble_value\x18\x07 \x01(\x01H\x01\x12\x13\n\tnil_value\x18\x08 \x01(\x08H\x01\x12\x1b\n\x11unsupported_value\x18\t \x01(\tH\x01\x12\x41\n\x18temperature_points_value\x18\x14 \x01(\x0b\x32\x1d.proto.TemperaturePointsValueH\x01\x12\x39\n\x14weekday_tariff_value\x18\x15 \x01(\x0b\x32\x19.proto.WeekdayTariffValueH\x01\x12\x39\n\x14weekend_tariff_value\x18\x16 \x01(\x0b\x32\x19.proto.WeekendTariffValueH\x01\x12I\n\x1dstate_of_charge_profile_value\x18\x17 \x01(\x0b\x32 .proto.StateOfChargeProfileValueH\x01\x12M\n\x1fweekly_settings_head_unit_value\x18\x18 \x01(\x0b\x32\".proto.WeeklySettingsHeadUnitValueH\x01\x12N\n\x1fspeed_alert_configuration_value\x18\x1b \x01(\x0b\x32#.proto.SpeedAlertConfigurationValueH\x01\x12\x37\n\x13\x65\x63o_histogram_value\x18\x1c \x01(\x0b\x32\x18.proto.EcoHistogramValueH\x01\x12\x39\n\x14weekly_profile_value\x18\x1d \x01(\x0b\x32\x19.proto.WeeklyProfileValueH\x01\x12;\n\x15\x63harge_programs_value\x18\x1f \x01(\x0b\x32\x1a.proto.ChargeProgramsValueH\x01\"\x87\x01\n\x19\x43ombustionConsumptionUnit\x12+\n\'UNSPECIFIED_COMBUSTION_CONSUMPTION_UNIT\x10\x00\x12\x13\n\x0fLITER_PER_100KM\x10\x01\x12\x10\n\x0cKM_PER_LITER\x10\x02\x12\n\n\x06MPG_UK\x10\x03\x12\n\n\x06MPG_US\x10\x04\"\x99\x01\n\x1a\x45lectricityConsumptionUnit\x12,\n(UNSPECIFIED_ELECTRICITY_CONSUMPTION_UNIT\x10\x00\x12\x11\n\rKWH_PER_100KM\x10\x01\x12\x0e\n\nKM_PER_KWH\x10\x02\x12\x11\n\rKWH_PER_100MI\x10\x03\x12\r\n\tM_PER_KWH\x10\x04\x12\x08\n\x04MPGE\x10\x05\"i\n\x12GasConsumptionUnit\x12$\n UNSPECIFIED_GAS_CONSUMPTION_UNIT\x10\x00\x12\x10\n\x0cKG_PER_100KM\x10\x01\x12\r\n\tKM_PER_KG\x10\x02\x12\x0c\n\x08M_PER_KG\x10\x03\"W\n\x11SpeedDistanceUnit\x12#\n\x1fUNSPECIFIED_SPEED_DISTANCE_UNIT\x10\x00\x12\x0c\n\x08KM_PER_H\x10\x01\x12\x0b\n\x07M_PER_H\x10\x02\x1a\x02\x18\x01\"H\n\tSpeedUnit\x12\x1a\n\x16UNSPECIFIED_SPEED_UNIT\x10\x00\x12\x0f\n\x0bKM_PER_HOUR\x10\x01\x12\x0e\n\nM_PER_HOUR\x10\x02\"H\n\x0c\x44istanceUnit\x12\x1d\n\x19UNSPECIFIED_DISTANCE_UNIT\x10\x00\x12\x0e\n\nKILOMETERS\x10\x01\x12\t\n\x05MILES\x10\x02\"P\n\x0fTemperatureUnit\x12 \n\x1cUNSPECIFIED_TEMPERATURE_UNIT\x10\x00\x12\x0b\n\x07\x43\x45LSIUS\x10\x01\x12\x0e\n\nFAHRENHEIT\x10\x02\"H\n\x0cPressureUnit\x12\x1d\n\x19UNSPECIFIED_PRESSURE_UNIT\x10\x00\x12\x07\n\x03KPA\x10\x01\x12\x07\n\x03\x42\x41R\x10\x02\x12\x07\n\x03PSI\x10\x03\"4\n\tRatioUnit\x12\x1a\n\x16UNSPECIFIED_RATIO_UNIT\x10\x00\x12\x0b\n\x07PERCENT\x10\x01\"D\n\rClockHourUnit\x12\x1f\n\x1bUNSPECIFIED_CLOCK_HOUR_UNIT\x10\x00\x12\x08\n\x04T12H\x10\x01\x12\x08\n\x04T24H\x10\x02\x42\x0e\n\x0c\x64isplay_unitB\x10\n\x0e\x61ttribute_type\"X\n\x13\x43hargeProgramsValue\x12\x41\n\x19\x63harge_program_parameters\x18\x01 \x03(\x0b\x32\x1e.proto.ChargeProgramParameters\"\xe4\x02\n\x17\x43hargeProgramParameters\x12;\n\x0e\x63harge_program\x18\x01 \x01(\x0e\x32\x14.proto.ChargeProgramR\rchargeprogram\x12\x17\n\x07max_soc\x18\x02 \x01(\x05R\x06maxSoc\x12\x1f\n\x0b\x61uto_unlock\x18\x03 \x01(\x08R\nautounlock\x12\x36\n\x17location_based_charging\x18\x04 \x01(\x08R\x15locationbasedcharging\x12%\n\x0eweekly_profile\x18\x05 \x01(\x08R\rweeklyprofile\x12\x1e\n\nclockTimer\x18\x06 \x01(\x08R\nclockTimer\x12\x30\n\x14max_charging_current\x18\x07 \x01(\x05R\x12MaxChargingCurrent\x12!\n\x0c\x65\x63o_charging\x18\x08 \x01(\x08R\x0b\x45\x63oCharging\"\xcd\x03\n\x12WeeklyProfileValue\x12T\n\'single_time_profile_entries_activatable\x18\x01 \x01(\x08R#singleTimeProfileEntriesActivatable\x12R\n\'max_number_of_weekly_time_profile_slots\x18\x02 \x01(\x05R!maxNumberOfWeeklyTimeProfileSlots\x12<\n\x1bmax_number_of_time_profiles\x18\x03 \x01(\x05R\x17maxNumberOfTimeProfiles\x12M\n$current_number_of_time_profile_slots\x18\x04 \x01(\x05R\x1f\x63urrentNumberOfTimeProfileSlots\x12\x44\n\x1f\x63urrent_number_of_time_profiles\x18\x05 \x01(\x05R\x1b\x63urrentNumberOfTimeProfiles\x12:\n\rtime_profiles\x18\x06 \x03(\x0b\x32\x15.proto.VVRTimeProfileR\x0ctimeProfiles\"\xc2\x01\n\x0eVVRTimeProfile\x12\x16\n\nidentifier\x18\x01 \x01(\x05R\x02id\x12\x12\n\x04hour\x18\x02 \x01(\x05R\x04hour\x12\x13\n\x06minute\x18\x03 \x01(\x05R\x03min\x12(\n\x04\x64\x61ys\x18\x04 \x03(\x0e\x32\x15.proto.TimeProfileDayR\x03\x64\x61y\x12\x16\n\x06\x61\x63tive\x18\x05 \x01(\x08R\x06\x61\x63tive\x12-\n\x16\x61pplication_identifier\x18\x06 \x01(\x05R\rapplicationId\"G\n\x11\x45\x63oHistogramValue\x12\x32\n\x12\x65\x63o_histogram_bins\x18\x01 \x03(\x0b\x32\x16.proto.EcoHistogramBin\"2\n\x0f\x45\x63oHistogramBin\x12\x10\n\x08interval\x18\x01 \x01(\x01\x12\r\n\x05value\x18\x02 \x01(\x01\"b\n\x1cSpeedAlertConfigurationValue\x12\x42\n\x1aspeed_alert_configurations\x18\x01 \x03(\x0b\x32\x1e.proto.SpeedAlertConfiguration\"p\n\x17SpeedAlertConfiguration\x12\x1a\n\x12\x65nd_timestamp_in_s\x18\x01 \x01(\x03\x12\x18\n\x10threshold_in_kph\x18\x02 \x01(\x05\x12\x1f\n\x17threshold_display_value\x18\x03 \x01(\t\"L\n\x1bWeeklySettingsHeadUnitValue\x12-\n\x0fweekly_settings\x18\x01 \x03(\x0b\x32\x14.proto.WeeklySetting\"<\n\rWeeklySetting\x12\x0b\n\x03\x64\x61y\x18\x01 \x01(\x05\x12\x1e\n\x16minutes_since_midnight\x18\x02 \x01(\x05\"M\n\x16TemperaturePointsValue\x12\x33\n\x12temperature_points\x18\x01 \x03(\x0b\x32\x17.proto.TemperaturePoint\"X\n\x10TemperaturePoint\x12\x0c\n\x04zone\x18\x01 \x01(\t\x12\x13\n\x0btemperature\x18\x02 \x01(\x01\x12!\n\x19temperature_display_value\x18\x03 \x01(\t\"4\n\x12WeekdayTariffValue\x12\x1e\n\x07tariffs\x18\x01 \x03(\x0b\x32\r.proto.Tariff\"4\n\x12WeekendTariffValue\x12\x1e\n\x07tariffs\x18\x01 \x03(\x0b\x32\r.proto.Tariff\"$\n\x06Tariff\x12\x0c\n\x04rate\x18\x01 \x01(\x05\x12\x0c\n\x04time\x18\x02 \x01(\x05\"K\n\x19StateOfChargeProfileValue\x12.\n\x10states_of_charge\x18\x01 \x03(\x0b\x32\x14.proto.StateOfCharge\"@\n\rStateOfCharge\x12\x16\n\x0etimestamp_in_s\x18\x01 \x01(\x03\x12\x17\n\x0fstate_of_charge\x18\x02 \x01(\x05\"\xa2\x01\n\x0fVEPUpdatesByVIN\x12\x17\n\x0fsequence_number\x18\x02 \x01(\x05\x12\x34\n\x07updates\x18\x01 \x03(\x0b\x32#.proto.VEPUpdatesByVIN.UpdatesEntry\x1a@\n\x0cUpdatesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.proto.VEPUpdate:\x02\x38\x01\"\x1f\n\x0c\x44\x65\x62ugMessage\x12\x0f\n\x07message\x18\x01 \x01(\t\"\xa8\x01\n\rVehicleStatus\x12\x0b\n\x03vin\x18\x01 \x01(\t\x12\x38\n\nattributes\x18\x02 \x03(\x0b\x32$.proto.VehicleStatus.AttributesEntry\x1aP\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x1d.proto.VehicleAttributeStatus:\x02\x38\x01\"\xfa\x06\n\x0bPushMessage\x12\x13\n\x0btracking_id\x18\x05 \x01(\t\x12%\n\tvepUpdate\x18\x01 \x01(\x0b\x32\x10.proto.VEPUpdateH\x00\x12,\n\nvepUpdates\x18\x02 \x01(\x0b\x32\x16.proto.VEPUpdatesByVINH\x00\x12+\n\x0c\x64\x65\x62ugMessage\x18\x03 \x01(\x0b\x32\x13.proto.DebugMessageH\x00\x12\x42\n\x16service_status_updates\x18\t \x01(\x0b\x32 .proto.ServiceStatusUpdatesByVINH\x00\x12;\n\x15service_status_update\x18\r \x01(\x0b\x32\x1a.proto.ServiceStatusUpdateH\x00\x12\x31\n\x10user_data_update\x18\n \x01(\x0b\x32\x15.proto.UserDataUpdateH\x00\x12O\n user_vehicle_auth_changed_update\x18\x0e \x01(\x0b\x32#.proto.UserVehicleAuthChangedUpdateH\x00\x12\x37\n\x13user_picture_update\x18\x0b \x01(\x0b\x32\x18.proto.UserPictureUpdateH\x00\x12/\n\x0fuser_pin_update\x18\x0c \x01(\x0b\x32\x14.proto.UserPINUpdateH\x00\x12\x30\n\x0fvehicle_updated\x18\x0f \x01(\x0b\x32\x15.proto.VehicleUpdatedH\x00\x12?\n\x17preferred_dealer_change\x18\x10 \x01(\x0b\x32\x1c.proto.PreferredDealerChangeH\x00\x12X\n%apptwin_command_status_updates_by_vin\x18\x11 \x01(\x0b\x32\'.proto.AppTwinCommandStatusUpdatesByVINH\x00\x12O\n\x1f\x61pptwin_pending_command_request\x18\x12 \x01(\x0b\x32$.proto.AppTwinPendingCommandsRequestH\x00\x12\x34\n\x11\x61ssigned_vehicles\x18\x13 \x01(\x0b\x32\x17.proto.AssignedVehiclesH\x00\x42\x05\n\x03msgJ\x04\x08\x07\x10\x08J\x04\x08\x08\x10\t\"\xc4\x01\n\rTrackingEvent\x12\x13\n\x0btracking_id\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\x12\x12\n\nevent_type\x18\x03 \x01(\t\x12\x32\n\x07payload\x18\x04 \x03(\x0b\x32!.proto.TrackingEvent.PayloadEntry\x1a\x43\n\x0cPayloadEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\"\n\x05value\x18\x02 \x01(\x0b\x32\x13.proto.PayloadValue:\x02\x38\x01\"p\n\x0cPayloadValue\x12\x16\n\x0cstring_value\x18\x01 \x01(\tH\x00\x12\x13\n\tint_value\x18\x02 \x01(\x05H\x00\x12\x14\n\nbool_value\x18\x03 \x01(\x08H\x00\x12\x16\n\x0c\x64ouble_value\x18\x04 \x01(\x01H\x00\x42\x05\n\x03msg\"4\n\x15\x41\x63knowledgeVEPRequest\x12\x17\n\x0fsequence_number\x18\x01 \x01(\x05:\x02\x18\x01\"5\n\x1a\x41\x63knowledgeVEPUpdatesByVIN\x12\x17\n\x0fsequence_number\x18\x01 \x01(\x05\"1\n\x15\x43onfigurePingInterval\x12\x18\n\x10ping_time_millis\x18\x01 \x01(\x05\"4\n\x19\x41\x63knowledgeVehicleUpdated\x12\x17\n\x0fsequence_number\x18\x01 \x01(\x05\";\n AcknowledgePreferredDealerChange\x12\x17\n\x0fsequence_number\x18\x01 \x01(\x05\"e\n\x0eVehicleUpdated\x12\x17\n\x0fsequence_number\x18\x01 \x01(\x05\x12\x0f\n\x07\x63iam_id\x18\x02 \x01(\t\x12\x0b\n\x03vin\x18\x03 \x01(\t\x12\x1c\n\x14\x65mit_timestamp_in_ms\x18\n \x01(\x03\"l\n\x15PreferredDealerChange\x12\x17\n\x0fsequence_number\x18\x01 \x01(\x05\x12\x0f\n\x07\x63iam_id\x18\x02 \x01(\t\x12\x0b\n\x03vin\x18\x03 \x01(\t\x12\x1c\n\x14\x65mit_timestamp_in_ms\x18\n \x01(\x03*y\n\rChargeProgram\x12\x1a\n\x16\x44\x45\x46\x41ULT_CHARGE_PROGRAM\x10\x00\x12\x1a\n\x16INSTANT_CHARGE_PROGRAM\x10\x01\x12\x17\n\x13HOME_CHARGE_PROGRAM\x10\x02\x12\x17\n\x13WORK_CHARGE_PROGRAM\x10\x03*f\n\x0f\x41ttributeStatus\x12\x0f\n\x0bVALUE_VALID\x10\x00\x12\x16\n\x12VALUE_NOT_RECEIVED\x10\x01\x12\x11\n\rVALUE_INVALID\x10\x03\x12\x17\n\x13VALUE_NOT_AVAILABLE\x10\x04\x42\x1c\n\x1a\x63om.daimler.mbcarkit.protob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vehicle_events_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032com.daimler.mbcarkit.proto'
  _VEPUPDATE_ATTRIBUTESENTRY._options = None
  _VEPUPDATE_ATTRIBUTESENTRY._serialized_options = b'8\001'
  _VEHICLEATTRIBUTESTATUS_SPEEDDISTANCEUNIT._options = None
  _VEHICLEATTRIBUTESTATUS_SPEEDDISTANCEUNIT._serialized_options = b'\030\001'
  _VEHICLEATTRIBUTESTATUS.fields_by_name['timestamp']._options = None
  _VEHICLEATTRIBUTESTATUS.fields_by_name['timestamp']._serialized_options = b'\030\001'
  _VEHICLEATTRIBUTESTATUS.fields_by_name['speed_distance_unit']._options = None
  _VEHICLEATTRIBUTESTATUS.fields_by_name['speed_distance_unit']._serialized_options = b'\030\001'
  _VEPUPDATESBYVIN_UPDATESENTRY._options = None
  _VEPUPDATESBYVIN_UPDATESENTRY._serialized_options = b'8\001'
  _VEHICLESTATUS_ATTRIBUTESENTRY._options = None
  _VEHICLESTATUS_ATTRIBUTESENTRY._serialized_options = b'8\001'
  _TRACKINGEVENT_PAYLOADENTRY._options = None
  _TRACKINGEVENT_PAYLOADENTRY._serialized_options = b'8\001'
  _ACKNOWLEDGEVEPREQUEST._options = None
  _ACKNOWLEDGEVEPREQUEST._serialized_options = b'\030\001'
  _CHARGEPROGRAM._serialized_start=7117
  _CHARGEPROGRAM._serialized_end=7238
  _ATTRIBUTESTATUS._serialized_start=7240
  _ATTRIBUTESTATUS._serialized_end=7342
  _VEPUPDATE._serialized_start=133
  _VEPUPDATE._serialized_end=393
  _VEPUPDATE_ATTRIBUTESENTRY._serialized_start=313
  _VEPUPDATE_ATTRIBUTESENTRY._serialized_end=393
  _VEHICLEATTRIBUTESTATUS._serialized_start=396
  _VEHICLEATTRIBUTESTATUS._serialized_end=3005
  _VEHICLEATTRIBUTESTATUS_COMBUSTIONCONSUMPTIONUNIT._serialized_start=2056
  _VEHICLEATTRIBUTESTATUS_COMBUSTIONCONSUMPTIONUNIT._serialized_end=2191
  _VEHICLEATTRIBUTESTATUS_ELECTRICITYCONSUMPTIONUNIT._serialized_start=2194
  _VEHICLEATTRIBUTESTATUS_ELECTRICITYCONSUMPTIONUNIT._serialized_end=2347
  _VEHICLEATTRIBUTESTATUS_GASCONSUMPTIONUNIT._serialized_start=2349
  _VEHICLEATTRIBUTESTATUS_GASCONSUMPTIONUNIT._serialized_end=2454
  _VEHICLEATTRIBUTESTATUS_SPEEDDISTANCEUNIT._serialized_start=2456
  _VEHICLEATTRIBUTESTATUS_SPEEDDISTANCEUNIT._serialized_end=2543
  _VEHICLEATTRIBUTESTATUS_SPEEDUNIT._serialized_start=2545
  _VEHICLEATTRIBUTESTATUS_SPEEDUNIT._serialized_end=2617
  _VEHICLEATTRIBUTESTATUS_DISTANCEUNIT._serialized_start=2619
  _VEHICLEATTRIBUTESTATUS_DISTANCEUNIT._serialized_end=2691
  _VEHICLEATTRIBUTESTATUS_TEMPERATUREUNIT._serialized_start=2693
  _VEHICLEATTRIBUTESTATUS_TEMPERATUREUNIT._serialized_end=2773
  _VEHICLEATTRIBUTESTATUS_PRESSUREUNIT._serialized_start=2775
  _VEHICLEATTRIBUTESTATUS_PRESSUREUNIT._serialized_end=2847
  _VEHICLEATTRIBUTESTATUS_RATIOUNIT._serialized_start=2849
  _VEHICLEATTRIBUTESTATUS_RATIOUNIT._serialized_end=2901
  _VEHICLEATTRIBUTESTATUS_CLOCKHOURUNIT._serialized_start=2903
  _VEHICLEATTRIBUTESTATUS_CLOCKHOURUNIT._serialized_end=2971
  _CHARGEPROGRAMSVALUE._serialized_start=3007
  _CHARGEPROGRAMSVALUE._serialized_end=3095
  _CHARGEPROGRAMPARAMETERS._serialized_start=3098
  _CHARGEPROGRAMPARAMETERS._serialized_end=3454
  _WEEKLYPROFILEVALUE._serialized_start=3457
  _WEEKLYPROFILEVALUE._serialized_end=3918
  _VVRTIMEPROFILE._serialized_start=3921
  _VVRTIMEPROFILE._serialized_end=4115
  _ECOHISTOGRAMVALUE._serialized_start=4117
  _ECOHISTOGRAMVALUE._serialized_end=4188
  _ECOHISTOGRAMBIN._serialized_start=4190
  _ECOHISTOGRAMBIN._serialized_end=4240
  _SPEEDALERTCONFIGURATIONVALUE._serialized_start=4242
  _SPEEDALERTCONFIGURATIONVALUE._serialized_end=4340
  _SPEEDALERTCONFIGURATION._serialized_start=4342
  _SPEEDALERTCONFIGURATION._serialized_end=4454
  _WEEKLYSETTINGSHEADUNITVALUE._serialized_start=4456
  _WEEKLYSETTINGSHEADUNITVALUE._serialized_end=4532
  _WEEKLYSETTING._serialized_start=4534
  _WEEKLYSETTING._serialized_end=4594
  _TEMPERATUREPOINTSVALUE._serialized_start=4596
  _TEMPERATUREPOINTSVALUE._serialized_end=4673
  _TEMPERATUREPOINT._serialized_start=4675
  _TEMPERATUREPOINT._serialized_end=4763
  _WEEKDAYTARIFFVALUE._serialized_start=4765
  _WEEKDAYTARIFFVALUE._serialized_end=4817
  _WEEKENDTARIFFVALUE._serialized_start=4819
  _WEEKENDTARIFFVALUE._serialized_end=4871
  _TARIFF._serialized_start=4873
  _TARIFF._serialized_end=4909
  _STATEOFCHARGEPROFILEVALUE._serialized_start=4911
  _STATEOFCHARGEPROFILEVALUE._serialized_end=4986
  _STATEOFCHARGE._serialized_start=4988
  _STATEOFCHARGE._serialized_end=5052
  _VEPUPDATESBYVIN._serialized_start=5055
  _VEPUPDATESBYVIN._serialized_end=5217
  _VEPUPDATESBYVIN_UPDATESENTRY._serialized_start=5153
  _VEPUPDATESBYVIN_UPDATESENTRY._serialized_end=5217
  _DEBUGMESSAGE._serialized_start=5219
  _DEBUGMESSAGE._serialized_end=5250
  _VEHICLESTATUS._serialized_start=5253
  _VEHICLESTATUS._serialized_end=5421
  _VEHICLESTATUS_ATTRIBUTESENTRY._serialized_start=313
  _VEHICLESTATUS_ATTRIBUTESENTRY._serialized_end=393
  _PUSHMESSAGE._serialized_start=5424
  _PUSHMESSAGE._serialized_end=6314
  _TRACKINGEVENT._serialized_start=6317
  _TRACKINGEVENT._serialized_end=6513
  _TRACKINGEVENT_PAYLOADENTRY._serialized_start=6446
  _TRACKINGEVENT_PAYLOADENTRY._serialized_end=6513
  _PAYLOADVALUE._serialized_start=6515
  _PAYLOADVALUE._serialized_end=6627
  _ACKNOWLEDGEVEPREQUEST._serialized_start=6629
  _ACKNOWLEDGEVEPREQUEST._serialized_end=6681
  _ACKNOWLEDGEVEPUPDATESBYVIN._serialized_start=6683
  _ACKNOWLEDGEVEPUPDATESBYVIN._serialized_end=6736
  _CONFIGUREPINGINTERVAL._serialized_start=6738
  _CONFIGUREPINGINTERVAL._serialized_end=6787
  _ACKNOWLEDGEVEHICLEUPDATED._serialized_start=6789
  _ACKNOWLEDGEVEHICLEUPDATED._serialized_end=6841
  _ACKNOWLEDGEPREFERREDDEALERCHANGE._serialized_start=6843
  _ACKNOWLEDGEPREFERREDDEALERCHANGE._serialized_end=6902
  _VEHICLEUPDATED._serialized_start=6904
  _VEHICLEUPDATED._serialized_end=7005
  _PREFERREDDEALERCHANGE._serialized_start=7007
  _PREFERREDDEALERCHANGE._serialized_end=7115
# @@protoc_insertion_point(module_scope)
