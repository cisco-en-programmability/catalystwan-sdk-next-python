=========================
app_registry.applications
=========================


Operation: GET /dataservice/app-registry/applications
-----------------------------------------------------


Get All the App for the given conditions

.. code:: python

    def get(
        traffic_class: Optional[str] = None,
        business_relevance: Optional[str] = None,
    ) -> List[Any]: ...


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
        client.app_registry.applications.get()


Operation: PUT /dataservice/app-registry/applications
-----------------------------------------------------


.. code:: python

    @overload
    def put(payload: List[EditAppDetailsPutRequest]) -> List[Any]: ...


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
        client.app_registry.applications.put()


Operation: PUT /dataservice/app-registry/applications/{appId}
-------------------------------------------------------------


.. code:: python

    @overload
    def put(payload: Any, app_id: str) -> PayloadItems: ...


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
        client.app_registry.applications.put()


.. toctree::
    :maxdepth: 1

    models

