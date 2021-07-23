from .cleanup import Cleanup
from edubot.core.bot import Edu


def setup(bot: Edu):
    bot.add_cog(Cleanup(bot))
