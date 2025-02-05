===================
sdavc.cloud_sourced
===================


Operation: GET /dataservice/sdavc/cloud-sourced
-----------------------------------------------


returns all cloud sourced application

.. code:: python

    def get_extended_applications(
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_by: Optional[str] = None,
        order_by: Optional[str] = None,
        application_family: Optional[str] = None,
        application_group: Optional[str] = None,
        traffic_class: Optional[str] = None,
        business_relevance: Optional[str] = None,
        status: Optional[str] = None,
        app_name: Optional[str] = None,
        source: Optional[str] = None,
        search_keyword: Optional[str] = None,
    ) -> GetExtendedApplicationResponse: ...


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
        client.sdavc.cloud_sourced.get_extended_applications()


Operation: POST /dataservice/sdavc/cloud-sourced
------------------------------------------------


.. code:: python

    def save_extended_applications(
        payload: Optional[SaveExtendedApplicationRequest] = None,
    ) -> DefaultSuccessResponse: ...


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
        client.sdavc.cloud_sourced.save_extended_applications()


.. toctree::
    :maxdepth: 1

    approve/index
    compliance/index
    models

