==========================
sig.sig_global_credentials
==========================


Operation: GET /dataservice/sig/sigGlobalCredentials/{featureTemplateType}
--------------------------------------------------------------------------


Get sig global credentials

.. code:: python

    def get(feature_template_type: str) -> FeatureTemplateType: ...


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
        client.sig.sig_global_credentials.get()


.. toctree::
    :maxdepth: 1

    models

