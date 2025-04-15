========================
statistics.sdra.headends
========================


Operation: GET /dataservice/statistics/sdra/headends
----------------------------------------------------


Get SD-WAN Remote Access Head-end summary

.. code:: python

    def get(site: Optional[int] = None) -> SdraHeadendSummary: ...


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
        client.statistics.sdra.headends.get()


.. toctree::
    :maxdepth: 1

    models

