===========================
umbrella.getkeys.management
===========================


Operation: GET /dataservice/umbrella/getkeys/management
-------------------------------------------------------


Get management keys from Umbrella

.. code:: python

    def get() -> None: ...


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
        client.umbrella.getkeys.management.get()


