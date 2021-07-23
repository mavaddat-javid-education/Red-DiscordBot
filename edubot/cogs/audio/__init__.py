from edubot.core.bot import Edu

from .core import Audio


def setup(bot: Edu):
    cog = Audio(bot)
    bot.add_cog(cog)
    cog.start_up_task()
