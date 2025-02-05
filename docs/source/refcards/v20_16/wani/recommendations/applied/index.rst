============================
wani.recommendations.applied
============================


Operation: GET /dataservice/wani/recommendations/applied
--------------------------------------------------------


Per tenant api to check which Wani recommendations have been applied for a given tenant

.. code:: python

    def get_applied_wani_recommendations() -> (
        List[AppliedRecommendationsResEntry]
    ): ...


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
        client.wani.recommendations.applied.get_applied_wani_recommendations()


.. toctree::
    :maxdepth: 1

    models

