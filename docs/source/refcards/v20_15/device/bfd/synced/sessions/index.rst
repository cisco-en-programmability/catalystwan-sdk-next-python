==========================
device.bfd.synced.sessions
==========================


Operation: GET /dataservice/device/bfd/synced/sessions
------------------------------------------------------


Get list of BFD sessions from vManage synchronously

.. code:: python

    def get(
        device_id: str,
        system_ip: Optional[str] = None,
        color: Optional[ColorParam] = None,
        local_color: Optional[LocalColorParam] = None,
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
        client.device.bfd.synced.sessions.get()


.. toctree::
    :maxdepth: 1

    models

