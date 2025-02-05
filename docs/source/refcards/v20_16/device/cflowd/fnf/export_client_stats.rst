=====================================
device.cflowd.fnf.export_client_stats
=====================================


Operation: GET /dataservice/device/cflowd/fnf/export-client-stats
-----------------------------------------------------------------


Get FnF export client stats from device

.. code:: python

    def get_fn_f_export_client_stats(device_id: str) -> Any: ...


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
        client.device.cflowd.fnf.export_client_stats.get_fn_f_export_client_stats()


