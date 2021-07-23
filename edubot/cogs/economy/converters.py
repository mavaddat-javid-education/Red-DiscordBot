from typing import NewType, TYPE_CHECKING

from edubot.core.commands import BadArgument
from edubot.core.i18n import Translator
from edubot.core.utils.chat_formatting import inline

_ = Translator("Economy", __file__)

# Duplicate of edubot.cogs.cleanup.converters.PositiveInt
PositiveInt = NewType("PositiveInt", int)
if TYPE_CHECKING:
    positive_int = PositiveInt
else:

    def positive_int(arg: str) -> int:
        try:
            ret = int(arg)
        except ValueError:
            raise BadArgument(_("{arg} is not an integer.").format(arg=inline(arg)))
        if ret <= 0:
            raise BadArgument(_("{arg} is not a positive integer.").format(arg=inline(arg)))
        return ret
