from .alias import Alias
from edubot.core.bot import Edu


async def setup(bot: Edu):
    cog = Alias(bot)
    bot.add_cog(cog)
    cog.sync_init()
