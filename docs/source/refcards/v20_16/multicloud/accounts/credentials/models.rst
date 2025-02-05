======
Models
======


.. code:: python

    from typing import Optional, List, Dict, Union, Any, Literal


    class PostAccountsResponse:
        account_id: Optional[str]
        account_name: Optional[str]
        cloud_type: Optional[str]
        region_list: Optional[str]


    class AwsIamCredentials:
        external_id: str
        role_arn: str


    class AwsKeyCredentials:
        api_key: str
        secret_key: str


    class AzureCredentials:
        client_id: str
        cloud_tenant_id: str
        secret_key: str
        subscription_id: str


    class GcpCredentials:
        auth_provider_x509_cert_url: str
        auth_uri: str
        client_email: str
        client_id: str
        client_x509_cert_url: str
        private_key: str
        private_key_id: str
        project_id: str
        token_uri: str
        type_: str


    class PostAccounts:
        account_name: str
        azure_credentials: AzureCredentials
        cloud_type: str
        gcp_credentials: GcpCredentials
        account_id: Optional[str]
        aws_iam_credentials: Optional[AwsIamCredentials]
        aws_key_credentials: Optional[AwsKeyCredentials]
        cloud_gateway_enabled: Optional[str]
        description: Optional[str]
        gcp_billing_id: Optional[str]
        kubernetes_discovery_enabled: Optional[str]
        service_discovery_enabled: Optional[str]


