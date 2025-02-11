===========
url.monitor
===========


Operation: GET /dataservice/url/monitor
---------------------------------------


List url's with monitoring configuration and details about the current state of alarm.

.. code:: python

    def get_url_monitor() -> List[UrlMonitoringInfoInner]: ...


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
        client.url.monitor.get_url_monitor()


Operation: PUT /dataservice/url/monitor
---------------------------------------


Update monitor configuration related to the url

.. code:: python

    def update_url_monitor(payload: Optional[Any] = None) -> None: ...


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
        client.url.monitor.update_url_monitor()


Operation: POST /dataservice/url/monitor
----------------------------------------


Monitor the url with specified configuration.

.. code:: python

    def create_url_monitor(payload: Optional[Any] = None) -> None: ...


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
        client.url.monitor.create_url_monitor()


Operation: DELETE /dataservice/url/monitor
------------------------------------------


Delete an url which is already being monitored.

.. code:: python

    def delete_url_monitor(url: str) -> None: ...


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
        client.url.monitor.delete_url_monitor()


.. toctree::
    :maxdepth: 1

    models

