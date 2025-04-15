=======================================
v1.feature_profile.nfvirtual.system.aaa
=======================================


Operation: POST /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/aaa
-------------------------------------------------------------------------------


Create AAA Profile Parcel for System feature profile

.. code:: python

    def post(
        system_id: str, payload: CreateNfvirtualAaaParcelPostRequest
    ) -> CreateNfvirtualAaaParcelPostResponse: ...


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
        client.v1.feature_profile.nfvirtual.system.aaa.post()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/aaa/{aaaId}
--------------------------------------------------------------------------------------


Get AAA Profile Parcels for System feature profile

.. code:: python

    def get(
        system_id: str, aaa_id: str
    ) -> GetSingleNfvirtualSystemAaaPayload: ...


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
        client.v1.feature_profile.nfvirtual.system.aaa.get()


Operation: PUT /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/aaa/{aaaId}
--------------------------------------------------------------------------------------


Edit a  AAA Profile Parcel for System feature profile

.. code:: python

    def put(
        system_id: str,
        aaa_id: str,
        payload: EditNfvirtualAaaParcelPutRequest,
    ) -> EditNfvirtualAaaParcelPutResponse: ...


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
        client.v1.feature_profile.nfvirtual.system.aaa.put()


Operation: DELETE /dataservice/v1/feature-profile/nfvirtual/system/{systemId}/aaa/{aaaId}
-----------------------------------------------------------------------------------------


Delete a AAA Profile Parcel for System feature profile

.. code:: python

    def delete(system_id: str, aaa_id: str) -> None: ...


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
        client.v1.feature_profile.nfvirtual.system.aaa.delete()


.. toctree::
    :maxdepth: 1

    models

