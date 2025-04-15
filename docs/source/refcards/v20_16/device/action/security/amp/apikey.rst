=================================
device.action.security.amp.apikey
=================================


Operation: DELETE /dataservice/device/action/security/amp/apikey/{uuid}
-----------------------------------------------------------------------


Process amp api key deletion operation

.. code:: python

    def delete(uuid: str) -> Any: ...


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
        client.device.action.security.amp.apikey.delete()


