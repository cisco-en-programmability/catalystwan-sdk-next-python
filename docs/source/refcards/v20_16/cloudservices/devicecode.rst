========================
cloudservices.devicecode
========================


Operation: POST /dataservice/cloudservices/devicecode
-----------------------------------------------------


Get Azure device code

.. code:: python

    def get_device_code() -> Any: ...


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
        client.cloudservices.devicecode.get_device_code()


