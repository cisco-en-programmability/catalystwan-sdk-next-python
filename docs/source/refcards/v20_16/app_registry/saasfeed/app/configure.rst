===================================
app_registry.saasfeed.app.configure
===================================


Operation: PUT /dataservice/app-registry/saasfeed/app/configure
---------------------------------------------------------------


Get All the App for the given conditions

.. code:: python

    def disableor_enable_saas_feed_for_selected_app(
        payload: Optional[Any] = None,
    ) -> Any: ...


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
        client.app_registry.saasfeed.app.configure.disableor_enable_saas_feed_for_selected_app()


