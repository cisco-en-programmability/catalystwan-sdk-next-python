======================
network.issues.summary
======================


Operation: GET /dataservice/network/issues/summary
--------------------------------------------------


Retrieve network issues summary

.. code:: python

    def get_network_issues_summary() -> Any: ...


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
        client.network.issues.summary.get_network_issues_summary()


