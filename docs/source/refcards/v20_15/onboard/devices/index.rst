===============
onboard.devices
===============


Operation: GET /dataservice/onboard/devices
-------------------------------------------


GET Manual Onboard Device details

.. code:: python

    def get_devices(status: str) -> List[DeviceDetailsData]: ...


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
        client.onboard.devices.get_devices()


Operation: POST /dataservice/onboard/devices
--------------------------------------------


Manual Onboard added Device details

.. code:: python

    def manual_onboard_devices(
        payload: Optional[DeviceDetailsData] = None,
    ) -> Any: ...


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
        client.onboard.devices.manual_onboard_devices()


.. toctree::
    :maxdepth: 1

    models

