======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class SpeedTestResponse:
        """
        This is valid speedTestResponse
        """

        is_new_session: Optional[bool]
        is_owner: Optional[bool]
        renewal_time: Optional[int]
        session_id: Optional[str]
        start_time: Optional[int]
        type_: Optional[str]
        user_ip: Optional[str]
        uuid: Optional[str]


    class ServerList:
        server_name: Optional[str]
        server_ports: Optional[str]


    class SpeedTestSession:
        """
        This is valid SpeedTestSession
        """

        destination_color: Optional[str]
        destination_ip: Optional[str]
        device_uuid: Optional[str]
        port: Optional[str]
        server_list: Optional[List[ServerList]]
        source_color: Optional[str]
        source_interface: Optional[str]
        source_ip: Optional[str]


    class SpeedTestStatusResponse:
        """
        This is valid speedTestStatusResponse
        """

        status: Optional[str]


    class Uuid:
        """
        This is valid uuid
        """

        uuid: Optional[str]


    class SpeedTestResult:
        """
        This is valid SpeedTestResult
        """

        down_speed: Optional[int]
        error: Optional[str]
        location: Optional[str]
        server: Optional[str]
        status: Optional[str]
        up_speed: Optional[int]


    class SpeedTestData:
        """
        This is valid speedTestData
        """

        destination_circuit: Optional[str]
        destination_ip: Optional[str]
        destination_local_ip: Optional[str]
        device_uuid: Optional[str]
        down_bw: Optional[str]
        down_speed: Optional[int]
        entry_time: Optional[int]
        error: Optional[str]
        logid: Optional[int]
        port: Optional[str]
        session_id: Optional[str]
        source_circuit: Optional[str]
        source_ip: Optional[str]
        source_local_ip: Optional[str]
        status: Optional[str]
        tenant: Optional[str]
        up_bw: Optional[str]
        up_speed: Optional[int]


    class SpeedTestResultResponse:
        """
        This is valid speedTestResultResponse
        """

        # This is valid speedTestData
        data: Optional[SpeedTestData]


