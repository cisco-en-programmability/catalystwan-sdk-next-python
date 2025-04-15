============================================
template.config.quick_connect.submit_devices
============================================


Operation: POST /dataservice/template/config/quickConnect/submitDevices
-----------------------------------------------------------------------


Creates and pushes bootstrap configurations onto day0 devices.

.. code:: python

    def post(payload: SubmitDay0ConfigPostRequest) -> List[Any]: ...


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
        client.template.config.quick_connect.submit_devices.post()


.. toctree::
    :maxdepth: 1

    models

