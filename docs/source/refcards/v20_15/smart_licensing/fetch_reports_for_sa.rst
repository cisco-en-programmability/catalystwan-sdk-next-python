====================================
smart_licensing.fetch_reports_for_sa
====================================


Operation: GET /dataservice/smartLicensing/fetchReportsForSa
------------------------------------------------------------


fetch reports offline for sle

.. code:: python

    def fetch_reports(
        sa_domain: str, sa_id: str, payload: Optional[Any] = None
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
        client.smart_licensing.fetch_reports_for_sa.fetch_reports()


