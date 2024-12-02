=====================
onboard.supportedlist
=====================


Operation: POST /dataservice/onboard/supportedlist
--------------------------------------------------


Manual Onboard Supported Device features

.. code:: python

    def get_supported_features(
        payload: Optional[List[str]] = None,
    ) -> SupportedResponse: ...


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
        client.onboard.supportedlist.get_supported_features()


.. toctree::
    :maxdepth: 1

    models

