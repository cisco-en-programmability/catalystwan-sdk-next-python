===========================================
v1.feature_profile.nfvirtual.system.logging
===========================================


Operation: POST /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/logging
-----------------------------------------------------------------------------------


Create Logging Profile Parcel for System feature profile

.. code:: python

    def post(
        system_id: str, payload: CreateNfvirtualLoggingParcelPostRequest
    ) -> CreateNfvirtualLoggingParcelPostResponse: ...


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
        client.v1.feature_profile.nfvirtual.system.logging.post()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/logging/{loggingId}
----------------------------------------------------------------------------------------------


Get Logging Profile Parcels for System feature profile

.. code:: python

    def get(
        system_id: str, logging_id: str
    ) -> GetSingleNfvirtualSystemLoggingPayload: ...


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
        client.v1.feature_profile.nfvirtual.system.logging.get()


Operation: PUT /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/logging/{loggingId}
----------------------------------------------------------------------------------------------


Edit a  Logging Profile Parcel for System feature profile

.. code:: python

    def put(
        system_id: str,
        logging_id: str,
        payload: EditNfvirtualLoggingParcelPutRequest,
    ) -> EditNfvirtualLoggingParcelPutResponse: ...


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
        client.v1.feature_profile.nfvirtual.system.logging.put()


Operation: DELETE /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/logging/{loggingId}
-------------------------------------------------------------------------------------------------


Delete a Logging Profile Parcel for System feature profile

.. code:: python

    def delete(system_id: str, logging_id: str) -> None: ...


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
        client.v1.feature_profile.nfvirtual.system.logging.delete()


.. toctree::
    :maxdepth: 1

    models

