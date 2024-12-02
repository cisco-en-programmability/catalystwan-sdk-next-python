===========================
device.security.information
===========================


Operation: GET /dataservice/device/security/information
-------------------------------------------------------


Get security information from devices

.. code:: python

    def create_session_list(device_id: str) -> List[Any]: ...


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
        client.device.security.information.create_session_list()


