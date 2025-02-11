===========================
dca.device.crashlog.details
===========================


Operation: POST /dataservice/dca/device/crashlog/details
--------------------------------------------------------


Get crash log

.. code:: python

    def get_crash_logs(payload: Optional[Any] = None) -> Any: ...


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
        client.dca.device.crashlog.details.get_crash_logs()


