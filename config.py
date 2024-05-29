import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6916875347:AAEVxR4cO_sIBB6V57ANA92pHKxzw9G3yX0") # Make a bot from https://t.me/BotFather and enter the token here
    #If deploying on vps edit the above value as example := TG_BOT_TOKEN = "Your-bot-token-inside-inverted-commas."
    
    APP_ID = int(os.environ.get("APP_ID", 10471716)) # Get this value from https://my.telegram.org/apps
    #If deploying on vps edit the above value as example := APP_ID = Your-APP_ID-without-inverted-commas
    
    API_HASH = os.environ.get("API_HASH", "f8a1b21a13af154596e2ff5bed164860") # Get this value from https://my.telegram.org/apps
    #If deploying on vps edit the above value as example := API_HASH = "Your-API_HASH-inside-inverted-commas."
    
    Mega_email = os.environ.get("Mega_email", "") # This is not necessary! Enter your mega email only if you have a mega.nz account with pro/business features.
    #If deploying on vps edit the above value as example := Mega_email = "Your-Mega_email-inside-inverted-commas."
    
    Mega_password = os.environ.get("Mega_password", "") # This is not necessary! Enter your mega password only if you have a mega.nz account with pro/business features.
    #If deploying on vps edit the above value as example := Mega_password = "Your-Mega_password-inside-inverted-commas."
    
    Bot_username = os.environ.get("Bot_username", "@Io_TesterBot") # Your bot's telegram username (must enter with '@' in the front of the username)
    #If deploying on vps edit the above value as example := Bot_username = "Your-Bot_username-inside-inverted-commas."
    
    OWNER_ID = os.environ.get("OWNER_ID", 6883997969) # Your(owner's) telegram id
    #If deploying on vps edit the above value as example := OWNER_ID = Your-telegram id-without-inverted-commas
    
    REDIS_URI = os.environ.get("REDIS_URI", "redis-18689.c85.us-east-1-2.ec2.redns.redis-cloud.com:18689") # Get This Value from https://app.redislabs.com/#/login
    #If deploying on vps edit the above value as example := REDIS_URI = "Your-Redis-Endpoint-inside-inverted-commas."
    
    REDIS_PASS = os.environ.get("REDIS_PASS", "5bQedh5WnTg24cMblDGeRjylvQxT1cBx") # Get This Value from https://app.redislabs.com/#/login
    #If deploying on vps edit the above value as example := REDIS_PASS = "Your-Redis-Password-inside-inverted-commas."

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "6883997969").split()) # Id's of the telegram users, who you want to allow for multitasking - downloading multiple links at once!
    
    #If deploying on heroku separate the ids by space. (don't put commas. Only separate each of the id's with space)
    
    #If deploying on vps edit the above value as example := 
    #AUTH_USERS = set(int(x) for x in (id1, id2)) 👈 Type exactly as that and replace id1 and id2 with the id's of the telegram users, who you want to allow for multitasking. You cand add many users like that!
    DOWNLOAD_LOCATION = "./DOWNLOADS" # The download location for users. (Don't change anything in this field!)
    ADMIN_LOCATION = "./ADOWNLOADS" # The download location for auth users. (Don't change anything in this field!)
