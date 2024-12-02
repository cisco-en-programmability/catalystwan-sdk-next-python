======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class EventStatsDataResponsePayloadDataEventStatsObjectEventStatsList:
        event_counter: Optional[int]
        event_failed_to_trace_counter: Optional[int]
        event_name: Optional[str]
        event_to_trace_counter: Optional[int]


    class EventStatsDataResponsePayloadDataEventStatsObject:
        event_stats_list: Optional[
            List[
                EventStatsDataResponsePayloadDataEventStatsObjectEventStatsList
            ]
        ]
        total_event_counter: Optional[int]


    class EventStatsDataResponsePayloadData:
        device_site_id: Optional[str]
        event_stats_object: Optional[
            EventStatsDataResponsePayloadDataEventStatsObject
        ]


    class EventStatsDataResponsePayloadData1:
        auto_on_task_id: Optional[int]
        data: Optional[EventStatsDataResponsePayloadData]
        tenant: Optional[str]
        type_: Optional[str]


    class EventStatsDataResponsePayload:
        """
        Event Stats Data schema for GET response
        """

        data: Optional[List[EventStatsDataResponsePayloadData1]]


