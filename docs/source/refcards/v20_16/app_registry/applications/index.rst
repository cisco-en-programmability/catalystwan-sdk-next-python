=========================
app_registry.applications
=========================


Operation: GET /dataservice/app-registry/applications
-----------------------------------------------------


Get All the App for the given conditions

.. code:: python

    def get_app_list(
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
        client.app_registry.applications.get_app_list()


Operation: PUT /dataservice/app-registry/applications
-----------------------------------------------------


Edit App Details

.. code:: python

    def edit_app_details(
        payload: Optional[List[EditAppDetailsPutRequest]] = None,
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
        client.app_registry.applications.edit_app_details()


Operation: PUT /dataservice/app-registry/applications/{appId}
-------------------------------------------------------------


Edit App Details

.. code:: python

    def edit_app_details_with_uuid(
        app_id: str, payload: Optional[Any] = None
    ) -> PayloadItems: ...


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
        client.app_registry.applications.edit_app_details_with_uuid()


.. toctree::
    :maxdepth: 1

    models

