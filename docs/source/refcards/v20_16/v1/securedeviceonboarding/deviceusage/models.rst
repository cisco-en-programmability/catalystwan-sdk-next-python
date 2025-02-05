======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class DeviceUsageDetails:
        # Name of the service provider.
        carrier_name: str
        # Name of the communication plan.
        communication_plan: str
        # Controller Id
        controller_id: str
        # Current Data Usage.
        current_data_usage: str
        # Identifier of the eSIM device.
        iccid: str
        # Name of the rate plan.
        rate_plan: str
        # Rate plan type.
        rate_plan_type: str
        # Slot Id
        slot_id: int
        # Details of any error encountered while retrieving device data usage
        error_details: Optional[str]
        # Bootstrap eSim Status
        esim_status: Optional[str]
        # Boolean flag that indicated if ICCID is on bootstrap account
        is_bootstrap: Optional[bool]
        # Total data used by other eSIM devices.
        other_esims_data_usage: Optional[str]
        # Rate plan usage limit.
        rate_plan_data_usage_limit: Optional[str]
        # Total data usage
        total_data_usage: Optional[str]
        # Total value of current data usage and data used by other eSIM devices
        usage_threshold_warning: Optional[List[str]]


