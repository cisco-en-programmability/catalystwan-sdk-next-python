==============================
featurecertificate.certificate
==============================


Operation: GET /dataservice/featurecertificate/certificate
----------------------------------------------------------


Get feature cert from cEdge device<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

.. code:: python

    def get_device_certificate(device_id: str) -> Any: ...


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
        client.featurecertificate.certificate.get_device_certificate()


Operation: PUT /dataservice/featurecertificate/certificate
----------------------------------------------------------


Upload feature cert for cEdge device<br><br><br>Note: In a multitenant vManage system, this API is only available in the Provider and Provider-As-Tenant view.

.. code:: python

    def install_feature_certificate(
        payload: Optional[Any] = None,
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
        client.featurecertificate.certificate.install_feature_certificate()


