from urllib.request import urlopen

import telepot
import telepot.aio
# from telegram.ext import CommandHandler, MessageHandler, Filters
from skybeard.beards import BeardAsyncChatHandlerMixin, Filters, regex_predicate, command_predicate
from . import gym

class Gym(telepot.aio.helper.ChatHandler, BeardAsyncChatHandlerMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_command(command_predicate("newgym"), self.add_gym)
        self.register_command(regex_predicate(".*gainz.*"), self.gainz_pics)
        self.register_command(Filters.location, self.gym_visit)

    async def gainz_pics(self, msg):
        gainz = gym.pics(msg)
        await self.sender.sendPhoto(("gainz.png", urlopen(gainz["photourl"])))
        if gainz["text"]:
            await self.sender.sendMessage(gainz["text"])

    async def gym_visit(self, msg):
        pass

    async def add_gym(msg):
        pass
