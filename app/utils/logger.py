import logging
from pathlib import Path

Path("logs").mkdir(exist_ok=True)

LOG_FILE = "logs/trading_bot.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)