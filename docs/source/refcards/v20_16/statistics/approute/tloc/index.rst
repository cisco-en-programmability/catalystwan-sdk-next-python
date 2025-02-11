========================
statistics.approute.tloc
========================


Operation: POST /dataservice/statistics/approute/tloc
-----------------------------------------------------


Get tloc

.. code:: python

    def get_approute_tloc(
        payload: Optional[Any] = None,
    ) -> List[AppRouteTlocRespInner]: ...


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
        client.statistics.approute.tloc.get_approute_tloc()


.. toctree::
    :maxdepth: 1

    models

