"""Tests for gibson.auth — channel credentials from environment variables."""

from __future__ import annotations

import grpc
import pytest

from gibson.auth import channel_credentials, credentials_from_env
from gibson.auth._credentials import _BearerTokenPlugin


def test_credentials_from_env_missing_endpoint(monkeypatch):
    monkeypatch.delenv("GIBSON_ENDPOINT", raising=False)
    monkeypatch.delenv("GIBSON_TOKEN", raising=False)
    with pytest.raises(ValueError, match="GIBSON_ENDPOINT"):
        credentials_from_env()


def test_credentials_from_env_missing_token(monkeypatch):
    monkeypatch.setenv("GIBSON_ENDPOINT", "localhost:50051")
    monkeypatch.delenv("GIBSON_TOKEN", raising=False)
    with pytest.raises(ValueError, match="GIBSON_TOKEN"):
        credentials_from_env()


def test_credentials_from_env_returns_tuple(monkeypatch):
    monkeypatch.setenv("GIBSON_ENDPOINT", "daemon.example.com:443")
    monkeypatch.setenv("GIBSON_TOKEN", "tok-test-1234")
    endpoint, creds = credentials_from_env()
    assert endpoint == "daemon.example.com:443"
    assert isinstance(creds, grpc.ChannelCredentials)


def test_channel_credentials_returns_composite(monkeypatch):
    monkeypatch.delenv("GIBSON_CLIENT_CERT", raising=False)
    monkeypatch.delenv("GIBSON_CLIENT_KEY", raising=False)
    creds = channel_credentials("tok-abc")
    assert isinstance(creds, grpc.ChannelCredentials)


def test_bearer_token_plugin_attaches_header():
    plugin = _BearerTokenPlugin("my-secret-token")
    received: list = []

    def callback(metadata, error):
        received.extend(metadata)

    plugin(None, callback)  # type: ignore[arg-type]
    assert ("authorization", "bearer my-secret-token") in received


def test_bearer_token_plugin_uses_lowercase_bearer():
    plugin = _BearerTokenPlugin("t")
    received: list = []
    plugin(None, lambda m, e: received.extend(m))  # type: ignore[arg-type]
    key, value = received[0]
    assert value.startswith("bearer ")
