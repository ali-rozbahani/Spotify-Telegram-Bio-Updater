CLIENT_ID = "f145532eca7343bc9e6a8fb064dff850"
CLIENT_SECRET = "fc8fb2d3f045437c9e6d12abf7b8c879"
API_ID = 13717481
API_HASH = "b7fcf88e3a231f780173b603130ce8e1"
INITIAL_TOKEN = "AQBqMJ0ePjr2i_9ROK1v9ML9bEctOq2-XksToJmdnmgTVerlJFoWBotknl0N3-yU4CAInb6tkmfiGZNL4cK7bqh2yWedvSKQtYa-xLUzgexU5NMx4zsZNPWcu8X7I6ef91U0eAyD4xuDSJULgW312ZqKkiS1tW5Ezb-RQlqqj9NrU27p_KtAz_QmneosxL-6Y_6FQFAzmm06B0iXlgDSYhs7y5qmRujF9H8_sMX9"
INITIAL_BIO = "shokr..."
LOG = "me"
# the escaping is necessary since we are testing against a regex pattern with it.
SHUTDOWN_COMMAND = "\/\/stop"
# The key which is used to determine if the current bio was generated from the bot ot from the user. This means:
# NEVER use whatever you put here in your original bio. NEVER. Don't do it!
KEY = "🎶"
# The bios MUST include the key. The bot will go though those and check if they are beneath telegrams character limit.
BIOS = [
    KEY + " Now Playing: {interpret} - {title} {progress}/{duration}",
    KEY + " Now Playing: {interpret} - {title}",
    KEY + " : {interpret} - {title}",
    KEY + " Now Playing: {title}",
    KEY + " : {title}",
]
# Mind that some characters (e.g. emojis) count more in telegram more characters then in python. If you receive an
# AboutTooLongError and get redirected here, you need to increase the offset. Check the special characters you either
# have put in the KEY or in one of the BIOS with an official Telegram App and see how many characters they actually
# count, then change the OFFSET below accordingly. Since the standard KEY is one emoji and I don't have more emojis
# anywhere, it is set to one (One emoji counts as two characters, so I reduce 1 from the character limit).
OFFSET = 1
# reduce the OFFSET from our actual 70 character limit
LIMIT = 70 - OFFSET
