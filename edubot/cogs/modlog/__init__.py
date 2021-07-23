from edubot.core.bot import Edu
from .modlog import ModLog


def setup(bot: Edu):
    bot.add_cog(ModLog(bot))
