======
Models
======


.. code:: python

    from typing import List, Dict, Union, Literal, Optional, Any

    Severity = Literal["Critical", "Major", "Medium", "Minor"]


    class AlarmDevices:
        system_ip: Optional[str]


    class GeneralSchema:
        empty: Optional[bool]


    class Alarm:
        """
        Represents any kind of alarm
        """

        acknowledged: Optional[bool]
        active: Optional[bool]
        cleared_by: Optional[str]
        cleared_events: Optional[List[str]]
        cleared_time: Optional[int]
        component: Optional[str]
        consumed_events: Optional[List[Any]]
        devices: Optional[List[AlarmDevices]]
        entry_time: Optional[int]
        eventname: Optional[str]
        id: Optional[str]
        message: Optional[str]
        possible_causes: Optional[List[str]]
        receive_time: Optional[int]
        rule_name_display: Optional[str]
        rulename: Optional[str]
        severity: Optional[Severity]
        severity_number: Optional[int]
        site_id: Optional[int]
        statcycletime: Optional[int]
        suppressed: Optional[bool]
        suppressed_by: Optional[Any]
        system_ip: Optional[str]
        tenant: Optional[str]
        type_: Optional[str]
        uuid: Optional[str]
        values: Optional[List[GeneralSchema]]
        values_short_display: Optional[List[GeneralSchema]]


    class PageInfo:
        # number of alarms to be fetched
        count: Optional[int]
        # end time of alarms to be fetched
        end_time: Optional[int]
        # start time of alarms to be fetched
        start_time: Optional[int]


    class AlarmResponse:
        """
        AlarmResponse is used for GET/POST /alarms call.
        """

        data: Optional[List[Alarm]]
        page_info: Optional[PageInfo]


