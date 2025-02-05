======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class AuditLogEntry:
        auditdetails: List[str]
        entry_time: int
        logdeviceid: str
        logfeature: str
        logid: str
        logmessage: str
        logmodule: str
        loguser: str
        logusersrcip: str
        statcycletime: int
        tenant: str
        id: Optional[str]


    class ChartObject:
        series: Optional[List[str]]
        title: Optional[str]
        x_axis: Optional[List[str]]
        x_axis_label: Optional[str]
        y_axis: Optional[List[str]]
        y_axis_label: Optional[str]


    class AuditLogHeaderColumns:
        data_type: str
        property: str
        title: str
        display_format: Optional[str]
        hideable: Optional[bool]
        input_format: Optional[str]
        is_display: Optional[bool]
        min_width: Optional[int]
        width: Optional[int]


    class GetStatDataFields:
        data_type: Optional[str]
        property: Optional[str]


    class AuditLogHeaderViewKeys:
        preference_key: Optional[str]
        unique_key: Optional[List[str]]


    class AuditLogHeader:
        chart: Optional[ChartObject]
        columns: Optional[AuditLogHeaderColumns]
        fields: Optional[GetStatDataFields]
        generated_on: Optional[int]
        view_keys: Optional[AuditLogHeaderViewKeys]


    class GetAuditLogData:
        data: List[AuditLogEntry]
        header: AuditLogHeader


