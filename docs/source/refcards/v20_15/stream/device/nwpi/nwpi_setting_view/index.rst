====================================
stream.device.nwpi.nwpi_setting_view
====================================


Operation: GET /dataservice/stream/device/nwpi/nwpiSettingView
--------------------------------------------------------------


Deprecated!!!

get NWPI setting

.. code:: python

    def nwpi_setting_view(
        type_: Optional[str] = None,
    ) -> NwpiSettingDataPayload: ...


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
        client.stream.device.nwpi.nwpi_setting_view.nwpi_setting_view()


.. toctree::
    :maxdepth: 1

    models

