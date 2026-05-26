"""gRPC channel credentials for the Gibson SDK.

Reads GIBSON_ENDPOINT and GIBSON_TOKEN from the environment.
Optionally supports mTLS via GIBSON_CLIENT_CERT / GIBSON_CLIENT_KEY.
"""

from __future__ import annotations

import os

import grpc


def credentials_from_env() -> tuple[str, grpc.ChannelCredentials]:
    """Read GIBSON_ENDPOINT and GIBSON_TOKEN from the environment.

    Returns:
        (endpoint, credentials) tuple ready for grpc.secure_channel().

    Raises:
        ValueError: if a required environment variable is missing.
    """
    endpoint = os.environ.get("GIBSON_ENDPOINT")
    if not endpoint:
        raise ValueError("GIBSON_ENDPOINT environment variable is required")

    token = os.environ.get("GIBSON_TOKEN")
    if not token:
        raise ValueError("GIBSON_TOKEN environment variable is required")

    return endpoint, channel_credentials(token)


def channel_credentials(token: str) -> grpc.ChannelCredentials:
    """Create gRPC channel credentials with bearer-token auth.

    Attaches the token as ``Authorization: bearer <token>`` on every RPC.
    If GIBSON_CLIENT_CERT and GIBSON_CLIENT_KEY are set, adds mTLS.
    """
    call_creds = grpc.metadata_call_credentials(
        _BearerTokenPlugin(token), name="bearer-token"
    )

    client_cert_path = os.environ.get("GIBSON_CLIENT_CERT")
    client_key_path = os.environ.get("GIBSON_CLIENT_KEY")

    if client_cert_path and client_key_path:
        with open(client_cert_path, "rb") as f:
            cert = f.read()
        with open(client_key_path, "rb") as f:
            key = f.read()
        ssl_creds = grpc.ssl_channel_credentials(certificate_chain=cert, private_key=key)
    else:
        ssl_creds = grpc.ssl_channel_credentials()

    return grpc.composite_channel_credentials(ssl_creds, call_creds)


class _BearerTokenPlugin(grpc.AuthMetadataPlugin):
    """Attaches ``Authorization: bearer <token>`` to every outbound RPC."""

    def __init__(self, token: str) -> None:
        self._token = token

    def __call__(
        self,
        context: grpc.AuthMetadataContext,
        callback: grpc.AuthMetadataPluginCallback,
    ) -> None:
        callback((("authorization", f"bearer {self._token}"),), None)
