from edubot.core.bot import Edu
from .reports import Reports


def setup(bot: Edu):
    bot.add_cog(Reports(bot))
