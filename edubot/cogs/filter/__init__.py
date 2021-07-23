from .filter import Filter
from edubot.core.bot import Edu


async def setup(bot: Edu) -> None:
    cog = Filter(bot)
    await cog.initialize()
    bot.add_cog(cog)
