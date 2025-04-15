=====================
util.logging.debuglog
=====================


Operation: POST /dataservice/util/logging/debuglog
--------------------------------------------------


Deprecated!!!

Test whether logging works

.. code:: python

    def post(payload: DebugLogPostRequest) -> None: ...


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
        client.util.logging.debuglog.post()


.. toctree::
    :maxdepth: 1

    models

