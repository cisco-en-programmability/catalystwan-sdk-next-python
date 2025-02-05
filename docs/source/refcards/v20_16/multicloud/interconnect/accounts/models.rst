======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class InterconnectAccountAttCredentials:
        """
        AT&T Credential information.
        """

        # Client id of the AT&T Account.
        client_id: str
        # Client secret of the AT&T Account.
        client_secret: str


    class InterconnectAccountEquinixCredentials:
        """
        Equinix Credential information.
        """

        # Client id of the Equinix Account.
        client_id: str
        # Client secret of the Equinix Account.
        client_secret: str


    class InterconnectAccountMegaportCredentials:
        """
        Megaport Credential Information
        """

        # Password of the Megaport Account.
        password: str
        # Username of the Megaport Account.
        username: str


    class InterconnectAccount:
        # AT&T Credential information.
        att_credentials: InterconnectAccountAttCredentials
        edge_account_id: str
        edge_account_name: str
        edge_type: str
        # Equinix Credential information.
        equinix_credentials: InterconnectAccountEquinixCredentials
        # Megaport Credential Information
        megaport_credentials: InterconnectAccountMegaportCredentials
        billing_provider_type: Optional[str]
        cred_type: Optional[str]
        description: Optional[str]
        # List of regions
        region_list: Optional[List[str]]


