========================
statistics.approute.tloc
========================


Operation: POST /dataservice/statistics/approute/tloc
-----------------------------------------------------


Get tloc

.. code:: python

    def post(payload: Any) -> List[List[AppRouteTlocRespInner]]: ...


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
        client.statistics.approute.tloc.post()


.. toctree::
    :maxdepth: 1

    models

