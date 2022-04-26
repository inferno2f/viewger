import logging

logging.basicConfig(
    level=logging.INFO, filename='git_client.log', format='%(asctime)s - %(levelname)s - %(message)s - %(name)s'
)

logger = logging.getLogger(__name__)
