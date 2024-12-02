==========================
device.action.status.clear
==========================


Operation: DELETE /dataservice/device/action/status/clear
---------------------------------------------------------


Delete status of action

.. code:: python

    def delete_status(process_id: Optional[str] = None) -> None: ...


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
        client.device.action.status.clear.delete_status()


