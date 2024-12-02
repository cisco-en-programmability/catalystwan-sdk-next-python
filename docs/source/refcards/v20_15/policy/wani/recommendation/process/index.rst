==================================
policy.wani.recommendation.process
==================================


Operation: POST /dataservice/policy/wani/recommendation/process
---------------------------------------------------------------


Applies recommendations to a centralized policy

.. code:: python

    def apply_wani_recommendation(key: str) -> ApplyRecommendationRes: ...


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
        client.policy.wani.recommendation.process.apply_wani_recommendation()


.. toctree::
    :maxdepth: 1

    models

