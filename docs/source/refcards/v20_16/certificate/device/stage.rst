========================
certificate.device.stage
========================


Operation: POST /dataservice/certificate/device/stage
-----------------------------------------------------


Stop data traffic to device

.. code:: python

    def post(payload: Any) -> str: ...


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
        client.certificate.device.stage.post()


