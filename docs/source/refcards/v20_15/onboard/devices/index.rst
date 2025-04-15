===============
onboard.devices
===============


Operation: GET /dataservice/onboard/devices
-------------------------------------------


GET Manual Onboard Device details

.. code:: python

    def get(status: str) -> List[DeviceDetailsData]: ...


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
        client.onboard.devices.get()


Operation: POST /dataservice/onboard/devices
--------------------------------------------


Manual Onboard added Device details

.. code:: python

    def post(payload: DeviceDetailsData) -> Any: ...


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
        client.onboard.devices.post()


.. toctree::
    :maxdepth: 1

    models

