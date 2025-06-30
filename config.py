import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7559908542:AAG1eBoWpspEzCiBfxTNEzaWcT4N3TGBr1g")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "20560221"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "37d35e3ead5d84adc8c4ea5032922f8d")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "5913223291"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://yexecax883:p0VAv5zsG1G9qPZm@cluster0.xu2k9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "yexecax883")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
