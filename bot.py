import logging

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

import pyrogram, os

if __name__ == "__main__":
    plugins = dict(root="plugins")
    app = pyrogram.Client(
        "bot",
        bot_token="6891228669:AAE3XDSkqgb4OGpcUUFCHvsFbI5iM-TrARA",
        api_id=23696595,
        api_hash="a5b4f74cd5b550622c4eee4fea7285b0",
        plugins=plugins,
    )
    app.run()
