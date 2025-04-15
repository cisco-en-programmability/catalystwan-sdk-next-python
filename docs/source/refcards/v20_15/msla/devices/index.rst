============
msla.devices
============


Operation: PUT /dataservice/msla/devices
----------------------------------------


Release licenses assigned to the devices

.. code:: python

    def put(payload: ReleaseLicensesRequest) -> None: ...


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
        client.msla.devices.put()


Operation: GET /dataservice/msla/devices
----------------------------------------


.. code:: python

    @overload
    def get(site_id: Optional[str] = None) -> GetMslaDevicesPayload: ...


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
        client.msla.devices.get()


Operation: GET /dataservice/msla/devices/{uuid}
-----------------------------------------------


.. code:: python

    @overload
    def get(uuid: str) -> List[GetDeviceLicensesInner]: ...


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
        client.msla.devices.get()


.. toctree::
    :maxdepth: 1

    models

