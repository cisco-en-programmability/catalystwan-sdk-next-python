===========================
util.logging.configurations
===========================


Operation: GET /dataservice/util/logging/configurations
-------------------------------------------------------


List logger configuration

.. code:: python

    def get() -> Configurations: ...


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
        client.util.logging.configurations.get()


.. toctree::
    :maxdepth: 1

    models

