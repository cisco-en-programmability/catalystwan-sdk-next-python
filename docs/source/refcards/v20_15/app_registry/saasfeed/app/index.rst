=========================
app_registry.saasfeed.app
=========================


Operation: GET /dataservice/app-registry/saasfeed/app/{feedId}
--------------------------------------------------------------


Get All Saas feed details of a particular application

.. code:: python

    def get_all_saas_feed_for_selected_app(feed_id: str) -> List[Any]: ...


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
        client.app_registry.saasfeed.app.get_all_saas_feed_for_selected_app()


.. toctree::
    :maxdepth: 1

    configure

