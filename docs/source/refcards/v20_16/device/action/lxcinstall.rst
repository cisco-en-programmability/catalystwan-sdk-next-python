========================
device.action.lxcinstall
========================


Operation: POST /dataservice/device/action/lxcinstall
-----------------------------------------------------


Process an installation operation

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
        client.device.action.lxcinstall.post()


