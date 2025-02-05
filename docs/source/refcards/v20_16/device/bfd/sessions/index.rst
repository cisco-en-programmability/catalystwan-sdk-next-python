===================
device.bfd.sessions
===================


Operation: GET /dataservice/device/bfd/sessions
-----------------------------------------------


Get list of BFD sessions from vManage (Real Time)

.. code:: python

    def create_bfd_sessions(
        device_id: str,
        system_ip: Optional[str] = None,
        color: Optional[ColorParam] = None,
        local_color: Optional[ColorParam] = None,
        region_type: Optional[RegionTypeParam] = None,
    ) -> List[Any]: ...


Example:
^^^^^^^^


.. code:: python

    from catalyswan.core import create_client

    url = "example.com"
    username = "admin"
    password = "password123"

    with create_client(
        url=url, username=username, password=password
    ) as client:
        client.device.bfd.sessions.create_bfd_sessions()


.. toctree::
    :maxdepth: 1

    models

