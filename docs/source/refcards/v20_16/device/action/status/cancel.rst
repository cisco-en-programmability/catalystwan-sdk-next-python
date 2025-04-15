===========================
device.action.status.cancel
===========================


Operation: POST /dataservice/device/action/status/cancel/{processId}
--------------------------------------------------------------------


Bulk cancel task status

.. code:: python

    def post(process_id: str) -> None: ...


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
        client.device.action.status.cancel.post()


