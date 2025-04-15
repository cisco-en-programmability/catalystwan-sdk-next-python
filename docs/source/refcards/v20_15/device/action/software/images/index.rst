=============================
device.action.software.images
=============================


Operation: GET /dataservice/device/action/software/images
---------------------------------------------------------


Get software images

.. code:: python

    def get(
        image_type: List[Image], vnf_type: Optional[str] = None
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
        client.device.action.software.images.get()


.. toctree::
    :maxdepth: 1

    models

