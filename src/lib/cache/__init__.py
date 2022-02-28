from lib.loggers import Logger

logger = Logger()


class Cache(dict):
    DEBUG = False

    def __str__(self):
        representation = (
            "{ " + ", ".join([f"'{key}': ..." for key in self.keys()]) + "}"
        )

        return representation

    def delete(self, key: str) -> None:
        if self.DEBUG:
            logger.info(f"Deleting key '{key}' from cache.")

        del self[key]
