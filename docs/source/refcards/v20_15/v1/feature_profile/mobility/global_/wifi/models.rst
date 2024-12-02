======
Models
======


.. code:: python

    from typing import Literal, Optional, List, Union, Dict, Any

    Type = Literal[
        "cellular",
        "ethernet",
        "globalSettings",
        "networkProtocol",
        "securityPolicy",
        "wifi",
    ]


    class Variable:
        json_path: str
        var_name: str


    class SsidConfig:
        qos_settings: Optional[str]
        security_auth_type: Optional[str]
        ssid: Optional[str]
        visibility: Optional[bool]
        wpa_psk_key: Optional[str]


    class GuestWifi:
        security_auth_type: Optional[str]
        ssid: Optional[str]
        visibility: Optional[bool]
        wpa_psk_key: Optional[str]


    class AaaServerInfo:
        aaa_servers_parcel_id: str
        radius_server_name: str


    class RadiusServer:
        host: str
        port: int
        secret: str


    class CorporateWifi:
        security_auth_type: str
        aaa_server_info: Optional[AaaServerInfo]
        corporate_wlan: Optional[bool]
        radius_server: Optional[RadiusServer]
        ssid: Optional[str]
        visibility: Optional[bool]
        wpa_psk_key: Optional[str]


    class RadioBandSetting24G:
        band: Optional[str]
        channel: Optional[str]
        channel_width: Optional[str]
        transmit_power: Optional[str]


    class RadioBandSetting5G:
        band: Optional[str]
        channel: Optional[str]
        channel_width: Optional[str]
        transmit_power: Optional[str]


    class ChannelPowerSettings:
        radio_band2_dot4_ghz: Optional[RadioBandSetting24G]
        radio_band5_ghz: Optional[RadioBandSetting5G]


    class CountryRegionSettings:
        country_region: Optional[str]
        regulatory_domain: Optional[str]


    class AdvancedRadioSetting:
        channel_power_settings: Optional[ChannelPowerSettings]
        country_region_settings: Optional[CountryRegionSettings]


    class CreateWifiProfileParcelForMobilityPostRequest:
        # Name of the Profile Parcel. Must be unique.
        name: str
        type_: Type
        advanced_radio_setting: Optional[AdvancedRadioSetting]
        corporate_wifi: Optional[CorporateWifi]
        # User who last created this.
        created_by: Optional[str]
        # Timestamp of creation
        created_on: Optional[int]
        # Description of the Profile Parcel.
        description: Optional[str]
        guest_wifi: Optional[GuestWifi]
        # System generated unique identifier of the Profile Parcel in UUID format.
        id: Optional[str]
        # User who last updated this.
        last_updated_by: Optional[str]
        # Timestamp of last update
        last_updated_on: Optional[int]
        ssid_config_list: Optional[List[SsidConfig]]
        variables: Optional[List[Variable]]


