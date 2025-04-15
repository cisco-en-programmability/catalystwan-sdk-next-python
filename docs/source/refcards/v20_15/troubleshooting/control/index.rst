=======================
troubleshooting.control
=======================


Operation: GET /dataservice/troubleshooting/control/{uuid}
----------------------------------------------------------


Troubleshoot control connections

.. code:: python

    def get(uuid: str) -> GetControlConnections: ...


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
        client.troubleshooting.control.get()


.. toctree::
    :maxdepth: 1

    models

