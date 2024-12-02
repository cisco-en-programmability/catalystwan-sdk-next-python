=================
hsec.testbed_mode
=================


Operation: GET /dataservice/hsec/testbedMode
--------------------------------------------


Return testbed mode information staging or production

.. code:: python

    def testbed_mode() -> TestbedMode: ...


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
        client.hsec.testbed_mode.testbed_mode()


.. toctree::
    :maxdepth: 1

    models

