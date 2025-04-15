========================
statistics.sdra.sessions
========================


Operation: GET /dataservice/statistics/sdra/sessions
----------------------------------------------------


Get SD-WAN Remote Access session summary

.. code:: python

    def get(site: Optional[int] = None) -> SdraSessionSummary: ...


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
        client.statistics.sdra.sessions.get()


.. toctree::
    :maxdepth: 1

    models

