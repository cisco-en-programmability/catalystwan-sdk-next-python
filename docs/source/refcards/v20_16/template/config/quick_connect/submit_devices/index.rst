============================================
template.config.quick_connect.submit_devices
============================================


Operation: POST /dataservice/template/config/quickConnect/submitDevices
-----------------------------------------------------------------------


Creates and pushes bootstrap configurations onto day0 devices.

.. code:: python

    def submit_day0_config(
        payload: Optional[SubmitDay0ConfigPostRequest] = None,
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
        client.template.config.quick_connect.submit_devices.submit_day0_config()


.. toctree::
    :maxdepth: 1

    models

