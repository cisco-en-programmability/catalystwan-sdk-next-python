==============================
certificate.controller.bulkcsr
==============================


Operation: POST /dataservice/certificate/controller/bulkcsr
-----------------------------------------------------------


Generate CSR for all controller

.. code:: python

    def generate_cs_rfor_all_controller() -> str: ...


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
        client.certificate.controller.bulkcsr.generate_cs_rfor_all_controller()


