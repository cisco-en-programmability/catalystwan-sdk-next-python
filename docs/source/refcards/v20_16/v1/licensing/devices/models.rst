======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class DevicesDetailsLicenses:
        billing_type: Optional[str]
        display_name: Optional[str]
        end_date: Optional[str]
        license_category: Optional[str]
        license_type: Optional[str]
        no0f_assigned_licenses: Optional[int]
        sa_name: Optional[str]
        start_date: Optional[str]
        subscription_id: Optional[str]
        tag: Optional[str]
        va_name: Optional[str]


    class DevicesDetailsDevices:
        compliance_status: Optional[str]
        configured_system_ip: Optional[str]
        device_model: Optional[str]
        device_tags: Optional[List[str]]
        host_name: Optional[str]
        hsec_compatible: Optional[str]
        hsec_license_status: Optional[str]
        hsec_status: Optional[str]
        in_compliant_reason: Optional[str]
        licenses: Optional[List[DevicesDetailsLicenses]]
        no_of_tenants_on_boarded: Optional[int]
        uuid: Optional[str]


    class DevicesDetails:
        devices: Optional[List[DevicesDetailsDevices]]


