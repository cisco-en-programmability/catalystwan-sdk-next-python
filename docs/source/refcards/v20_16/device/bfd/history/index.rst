==================
device.bfd.history
==================


Operation: GET /dataservice/device/bfd/history
----------------------------------------------


Get BFD session history from device (Real Time)

.. code:: python

    def create_bfd_history_list(
        device_id: str,
        system_ip: Optional[str] = None,
        color: Optional[ColorParam] = None,
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
        client.device.bfd.history.create_bfd_history_list()


.. toctree::
    :maxdepth: 1

    models

