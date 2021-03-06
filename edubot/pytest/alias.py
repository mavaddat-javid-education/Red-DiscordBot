import pytest

from edubot.cogs.alias import Aliasedubot
from edubot.core import Config

__all__ = ["alias"]


@pytest.fixture()
def alias(config, monkeypatch):
    with monkeypatch.context() as m:
        m.setattr(Config, "get_conf", lambda *args, **kwargs: config)
        return Alias(None)
