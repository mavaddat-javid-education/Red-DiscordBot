from edubot.core.bot import Edu
from .mutes import Mutes


def setup(bot: Edu):
    cog = Mutes(bot)
    bot.add_cog(cog)
