======================
util.logfile.appserver
======================


Operation: GET /dataservice/util/logfile/appserver
--------------------------------------------------


Lists content of log file. This API accepts content type as text/plain. It is mandatory to provide response content type. Any other content type would result in empty response.

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
        client.util.logfile.appserver.get()


.. toctree::
    :maxdepth: 1

    lastnlines

