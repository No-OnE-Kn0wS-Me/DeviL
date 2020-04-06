from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 861055237  # my telegram ID
    OWNER_USERNAME = "tHe_GaMeR_B0Y"  # my telegram username
    API_KEY = "1164745168:AAGaZZLbrseEJmtOy8ow_o7XLNksUkQWKHQ"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/database'  # sample db credentials
    MESSAGE_DUMP = '--1001490304893' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [861055237, 1008681754]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
