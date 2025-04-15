====================
wani.recommendations
====================


Operation: GET /dataservice/wani/recommendations
------------------------------------------------


API to get the recommendations obtained from WANI for a given tenant. This returns only valid recommendations based on expiry. It filters out recommendations that are inactive.

.. code:: python

    def get(site_id: Optional[str] = None) -> RecommendationsResponse: ...


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
        client.wani.recommendations.get()


.. toctree::
    :maxdepth: 1

    applied/index
    models

