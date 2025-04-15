================================
device.action.security.amp.rekey
================================


Operation: POST /dataservice/device/action/security/amp/rekey
-------------------------------------------------------------


Process amp api re-key operation

.. code:: python

    def post(payload: Any) -> Any: ...


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
        client.device.action.security.amp.rekey.post()


