import pytest

from edubot.cogs.permissions import Permissionsedubot
from edubot.core import Config


@pytest.fixture()
def permissions(config, monkeypatch, red):
    with monkeypatch.context() as m:
        m.setattr(Config, "get_conf", lambda *args, **kwargs: config)
        return Permissions(red)
