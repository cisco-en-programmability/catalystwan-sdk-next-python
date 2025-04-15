========================================================
v1.feature_profile.nfvirtual.networks.vnf_attributes.vnf
========================================================


Operation: POST /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/vnf-attributes/{vnfAttributesId}/vnf
--------------------------------------------------------------------------------------------------------------------


Create VNF Profile Parcel for Networks feature profile

.. code:: python

    def post(
        networks_id: str,
        vnf_attributes_id: str,
        payload: CreateNfvirtualVnfParcelPostRequest,
    ) -> CreateNfvirtualVnfParcelPostResponse: ...


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
        client.v1.feature_profile.nfvirtual.networks.vnf_attributes.vnf.post()


Operation: GET /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/vnf-attributes/{vnfAttributesId}/vnf/{vnfId}
---------------------------------------------------------------------------------------------------------------------------


Get VNF Profile Parcels for Networks feature profile

.. code:: python

    def get(
        networks_id: str, vnf_attributes_id: str, vnf_id: str
    ) -> GetSingleNfvirtualNetworksVnfAttributesVnfPayload: ...


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
        client.v1.feature_profile.nfvirtual.networks.vnf_attributes.vnf.get()


Operation: PUT /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/vnf-attributes/{vnfAttributesId}/vnf/{vnfId}
---------------------------------------------------------------------------------------------------------------------------


Edit a VNF Profile Parcel for networks feature profile

.. code:: python

    def put(
        networks_id: str,
        vnf_attributes_id: str,
        vnf_id: str,
        payload: EditNfvirtualVnfParcelPutRequest,
    ) -> EditNfvirtualVnfParcelPutResponse: ...


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
        client.v1.feature_profile.nfvirtual.networks.vnf_attributes.vnf.put()


Operation: DELETE /dataservice/v1/feature-profile/nfvirtual/networks/{networksId}/vnf-attributes/{vnfAttributesId}/vnf/{vnfId}
------------------------------------------------------------------------------------------------------------------------------


Delete a VNF Profile Parcel for Networks feature profile

.. code:: python

    def delete(
        networks_id: str, vnf_attributes_id: str, vnf_id: str
    ) -> None: ...


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
        client.v1.feature_profile.nfvirtual.networks.vnf_attributes.vnf.delete()


.. toctree::
    :maxdepth: 1

    models

