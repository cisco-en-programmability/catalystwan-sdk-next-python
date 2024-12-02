===================
multicloud.swimages
===================


Operation: GET /dataservice/multicloud/swimages
-----------------------------------------------


Get software image list

.. code:: python

    def get_supported_software_image_list(
        cloud_type: CloudTypeParam,
        account_id: Optional[str] = None,
        cloud_region: Optional[str] = None,
    ) -> List[SwImagesResponse]: ...


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
        client.multicloud.swimages.get_supported_software_image_list()


.. toctree::
    :maxdepth: 1

    models

