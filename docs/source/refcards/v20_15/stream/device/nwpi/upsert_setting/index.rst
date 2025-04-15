=================================
stream.device.nwpi.upsert_setting
=================================


Operation: POST /dataservice/stream/device/nwpi/upsertSetting
-------------------------------------------------------------


Deprecated!!!

insert or update setting

.. code:: python

    def post(payload: NwpiSettingDataPayload) -> None: ...


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
        client.stream.device.nwpi.upsert_setting.post()


.. toctree::
    :maxdepth: 1

    models

