============
msla.devices
============


Operation: GET /dataservice/msla/devices
----------------------------------------


Retrieve list of devices and their subscription information

.. code:: python

    def get_msla_devices_1(
        site_id: Optional[str] = None,
    ) -> GetMslaDevicesPayload: ...


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
        client.msla.devices.get_msla_devices_1()


Operation: PUT /dataservice/msla/devices
----------------------------------------


Release licenses assigned to the devices

.. code:: python

    def release_licenses_1(
        payload: Optional[ReleaseLicensesRequest] = None,
    ) -> None: ...


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
        client.msla.devices.release_licenses_1()


Operation: GET /dataservice/msla/devices/{uuid}
-----------------------------------------------


Get licenses associated to device

.. code:: python

    def get_license_by_uuid_1(
        uuid: str,
    ) -> List[GetDeviceLicensesInner]: ...


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
        client.msla.devices.get_license_by_uuid_1()


.. toctree::
    :maxdepth: 1

    models

