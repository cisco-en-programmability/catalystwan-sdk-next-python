===================================
v1.cloudonramp.saas.webexsyncstatus
===================================


Operation: GET /dataservice/v1/cloudonramp/saas/webexsyncstatus
---------------------------------------------------------------


Get Webex's sync Status for devices with COR Saas enabled via config group or device template

.. code:: python

    def get() -> None: ...


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
        client.v1.cloudonramp.saas.webexsyncstatus.get()


