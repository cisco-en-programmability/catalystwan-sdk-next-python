===========
url.monitor
===========


Operation: GET /dataservice/url/monitor
---------------------------------------


List url's with monitoring configuration and details about the current state of alarm.

.. code:: python

    def get() -> List[UrlMonitoringInfoInner]: ...


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
        client.url.monitor.get()


Operation: PUT /dataservice/url/monitor
---------------------------------------


Update monitor configuration related to the url

.. code:: python

    def put(payload: Any) -> None: ...


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
        client.url.monitor.put()


Operation: POST /dataservice/url/monitor
----------------------------------------


Monitor the url with specified configuration.

.. code:: python

    def post(payload: Any) -> None: ...


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
        client.url.monitor.post()


Operation: DELETE /dataservice/url/monitor
------------------------------------------


Delete an url which is already being monitored.

.. code:: python

    def delete(url: str) -> None: ...


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
        client.url.monitor.delete()


.. toctree::
    :maxdepth: 1

    models

