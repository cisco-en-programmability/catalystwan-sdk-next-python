======================================
system.device.selfsignedcert.iscreated
======================================


Operation: GET /dataservice/system/device/selfsignedcert/iscreated
------------------------------------------------------------------


Whether self signed certificate created

.. code:: python

    def get() -> Any: ...


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
        client.system.device.selfsignedcert.iscreated.get()


