======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class EventStats:
        discarded_events: Optional[int]
        processed_events: Optional[int]
        total: Optional[int]


    class AlarmStatsResponseCorrelationEngine:
        added_events: Optional[int]


    class AlarmStatsResponse:
        correlation_db_manipulator: Optional[Dict[str, EventStats]]
        correlation_engine: Optional[AlarmStatsResponseCorrelationEngine]
        link_update_correlator: Optional[Dict[str, str]]


