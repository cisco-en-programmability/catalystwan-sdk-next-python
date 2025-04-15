=================================
util.logfile.appserver.lastnlines
=================================


Operation: GET /dataservice/util/logfile/appserver/lastnlines
-------------------------------------------------------------


List last N lines of log file. This API accepts content type as text/plain. It is mandatory to provide response content type. Any other content type would result in empty response.

.. code:: python

    def get(lines: Optional[int] = 100) -> Any: ...


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
        client.util.logfile.appserver.lastnlines.get()


