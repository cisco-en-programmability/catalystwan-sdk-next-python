===============================
umbrella.getkeys.networkdevices
===============================


Operation: GET /dataservice/umbrella/getkeys/networkdevices
-----------------------------------------------------------


Get network devices keys from Umbrella

.. code:: python

    def get_network_keys_from_umbrella() -> None: ...


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
        client.umbrella.getkeys.networkdevices.get_network_keys_from_umbrella()


