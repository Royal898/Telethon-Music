import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "16341342"))
    API_HASH = os.environ.get("API_HASH", "8d569ba1bdff190ed468f33d84fcb942")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6136292821:AAFxXZGYYrdK-gqxy_q6wanZlNsvAr-Ck_w")
    STRING_SESSION = os.environ.get("STRING_SESSION", "AQARyoWIKFhWEuwLWKhm5YOWqvRdItZSGVAQ5HQlLrVSuYDiRcye1thbJHxK9VtzRAMdmvU3KiTg6TrJjrMM0r2mMhis1Kc7jZjZG87X7j82yey6AxneX1_vavsNh6uyZvVWVsWeWQzMvjpEcG56XLcSdUX2p8gLoq0QoiDzx7DmgCVVGvRxpr8Vv8B0xMjzXB7_gN6P8VxM4nuzetB6LWgL5uiU1g0kRGjQIT-3QemmLcTabbLln9oezMsYBvsjSMCSN3BC-ct9z6iT-gHtbLzxda8QKIyzU8GwcnRQsrVqWwIy54GKbBuxLiYw9w1aZjPtb0UrTS8N55-sb8ENI65uAAAAATXMBPQA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "Blackdevil898") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "ModsTechz") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
