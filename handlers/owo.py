import asyncio
import random
from handlers.message_handler import HandlerModule, MessageHandler

class Module(HandlerModule):
    def __init__(self):
        super().__init__("test")


    def init_handlers(self):

        self.handlers.append( owoHandler() )


class TestHandler(MessageHandler):
    def __init__(self):
        self.signal = "!OWO"

        # params to dispay in help meesages
        self.params = ""

        # displayed when !help is called
        self.short_description = " What's this?"

        # displatyed when !help test is called
        self.long_description = " No really, what is this?"




    async def handle_message(self, client, message, state):

        if message.content.startswith(self.signal):

            await client.edit_message(message.channel, "What's this?")
