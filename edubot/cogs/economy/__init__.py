from edubot.core.bot import Edu
from .economy import Economy


def setup(bot: Edu):
    bot.add_cog(Economy(bot))
