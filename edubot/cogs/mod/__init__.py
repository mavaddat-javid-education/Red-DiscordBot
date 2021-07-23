from edubot.core.bot import Edu
from .mod import Mod


async def setup(bot: Edu):
    cog = Mod(bot)
    bot.add_cog(cog)
    await cog.initialize()
