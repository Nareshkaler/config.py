import os
import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()
# Get this value from my.telegram.org/apps
API_ID = int(getenv("27823471"))
API_HASH = getenv("3fdcfcdfad951b85b81477a1329d39d4")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7146398220:AAEJjDAYm0jDczg4WKFiD_ew7wLIIsy0r98")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://noobxcoder:nareshKaler@cluster0.7rgzxwq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 16000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("7422283124"))
LOG_GROUP_ID = int(getenv(" -1002158640298", "-1001443337704"))

# Get this value from  on Telegram by /id
OWNER_ID = int(getenv("7422283124"))

# Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv(" choudharyxmusic")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HRKU-7fc12e59-0b80-4283-a1fa-e541e51caa43")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/THE-VIP-BOY-OP/VIP-MUSIC",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/MYz_MOD")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/LosTxCHATTING")

# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "100"))

RADIO_URL = getenv("RADIO_URL", "http://peridot.streamguys.com:7150/Mirchi")

# Don't fill here any YouTube link fill here any direct acessable audio link

# MaximuM limit for fetching playlist's track from youtube, spotify, apple
# links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "100"))
# Set this to True if you want the assistant to automatically leave chats
# after an interval
AUTO_LEAVING_ASSISTANT = False

# Auto Gcast/Broadcast Handler, Write:- [On / Off] During Hosting, Dont Do
# anything here.)
AUTO_GCAST = os.getenv("AUTO_GCAST")

# Auto Broadcast Message That You Want Use In Auto Broadcast In All Groups.
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv(
    "SPOTIFY_CLIENT_SECRET", "409e31d3ddd64af08cfcc3b0f064fcbe"
)


# Maximum limit for fetching playlist's track from youtube, spotify, apple
# links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 2500))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes

# Time after which bot will suggest random chats about bot commands.
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "3")
)  # Remember to give value in Seconds

# Set it True if you want to bot to suggest about bot commands to random
# chats of your bots.
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "True")
# Cleanmode time after which bot will delete its old messages from chats
CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5")
)  # Remember to give value in Seconds

# Get your pyrogram v2 session from @VIP_STRING_ROBOT on Telegram
STRING1 = getenv("BQGojW8AAr_CZLJETjfACUzLy9wSeYBVDVOXfVBDv3xNNp6tmgtG0dqJJJwKUMFlNRxrk5cz8XOf2MTXwmrtTKmEBctPLlw-HXlZaSR7W5e5GP2Xag4Nes9IZvbBnLc8Y1_VIm9D4ijkOD-FOpuIkoix6yeTGNZoGkBKEbhXMOWwzDt_hF5ciLhZB0qJFIa7xkRRcNFFUufkVLNnXdEDG1eB1fBk0U6fTOJ9yArOIaoJgYb8yeOZrTaLl_82B8WXanKuuWPqIQVILfdFXIPv9NEp7YZPSTA-fQdD6GcVt6-2wjp1gHsdxFmRjupj3G1LFdzp56iLTq7ovH20D7VrGjiiDdbReAAAAAG6Zw10AA", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


╱╱▏┈┈╱╱╱╱▏╱╱▏
▇╱▏┈┈▇▇▇╱▏▇╱▏
▇╱▏▁┈▇╱▇╱▏▇╱▏▁
▇╱╱╱▏▇╱▇╱▏▇╱╱╱
▇▇▇╱┈▇▇▇╱┈▇▇▇╱ 


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/ecdeac045f4045c198bd6.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/ecdeac045f4045c198bd6.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/ecdeac045f4045c198bd6.jpg"
STATS_IMG_URL = "https://graph.org/file/079686b17ed424ab8edca.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/ecdeac045f4045c198bd6.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/ecdeac045f4045c198bd6.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/ecdeac045f4045c198bd6.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/ecdeac045f4045c198bd6.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/ecdeac045f4045c198bd6.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/ecdeac045f4045c198bd6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/ecdeac045f4045c198bd6.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/ecdeac045f4045c198bd6.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
