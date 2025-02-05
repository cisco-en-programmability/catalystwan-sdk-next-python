=================================
certificate.controller.certstatus
=================================


Operation: GET /dataservice/certificate/controller/certstatus
-------------------------------------------------------------


invalidate the device

.. code:: python

    def get_controller_cert_status() -> str: ...


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
        client.certificate.controller.certstatus.get_controller_cert_status()


