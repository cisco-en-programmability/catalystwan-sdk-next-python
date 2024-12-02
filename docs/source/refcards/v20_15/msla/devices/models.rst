======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class GetSingleMslaDevicePayload:
        configured_system_ip: Optional[str]
        device_model: Optional[str]
        host_name: Optional[str]
        hsec_compatible: Optional[str]
        hsec_status: Optional[str]
        license_status: Optional[str]
        license_type: Optional[str]
        licenses: Optional[List[str]]
        msla: Optional[str]
        sa_account: Optional[str]
        sa_namme: Optional[str]
        subscription_id: Optional[List[str]]
        tag: Optional[List[str]]
        template_name: Optional[str]
        uuid: Optional[str]
        va_account: Optional[List[str]]
        va_name: Optional[str]


    class GetMslaDevicesPayload:
        data: Optional[List[GetSingleMslaDevicePayload]]


    class ReleaseLicensesRequest:
        # List of device UUIDs
        devices: Optional[List[str]]


    class GetDeviceLicensesInner:
        billing_model: Optional[str]
        billing_type: Optional[str]
        display_name: Optional[str]
        end_date: Optional[str]
        in_use: Optional[str]
        license_category: Optional[str]
        license_type: Optional[str]
        saname: Optional[str]
        start_date: Optional[str]
        subscription_id: Optional[str]
        tag: Optional[str]
        vaname: Optional[str]


