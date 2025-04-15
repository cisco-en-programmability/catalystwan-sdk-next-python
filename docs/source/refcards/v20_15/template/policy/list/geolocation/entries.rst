========================================
template.policy.list.geolocation.entries
========================================


Operation: GET /dataservice/template/policy/list/geolocation/entries
--------------------------------------------------------------------


Get list of countries and continents for geo location

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
        client.template.policy.list.geolocation.entries.get()


