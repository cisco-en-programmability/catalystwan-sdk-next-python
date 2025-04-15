======================
alarms.markallasviewed
======================


Operation: POST /dataservice/alarms/markallasviewed
---------------------------------------------------


Mark all alarms as acknowledged by the user

.. code:: python

    def post(payload: Any, type_: Optional[str] = None) -> Any: ...


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
        client.alarms.markallasviewed.post()


