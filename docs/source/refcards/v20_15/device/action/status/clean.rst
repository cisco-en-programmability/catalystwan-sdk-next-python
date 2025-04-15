==========================
device.action.status.clean
==========================


Operation: GET /dataservice/device/action/status/clean
------------------------------------------------------


Deprecated!!!

Delete task and status vertex

.. code:: python

    def get(clean_status: Optional[bool] = None) -> None: ...


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
        client.device.action.status.clean.get()


