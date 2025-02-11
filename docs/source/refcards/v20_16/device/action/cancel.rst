====================
device.action.cancel
====================


Operation: POST /dataservice/device/action/cancel
-------------------------------------------------


Cancel tasks

.. code:: python

    def process_cancel_task(payload: Optional[Any] = None) -> None: ...


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
        client.device.action.cancel.process_cancel_task()


