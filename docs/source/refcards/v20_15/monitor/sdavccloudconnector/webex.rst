=================================
monitor.sdavccloudconnector.webex
=================================


Operation: GET /dataservice/monitor/sdavccloudconnector/webex
-------------------------------------------------------------


Get SD AVC App Rules for Webex

.. code:: python

    def get_webex_app_data() -> Any: ...


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
        client.monitor.sdavccloudconnector.webex.get_webex_app_data()


