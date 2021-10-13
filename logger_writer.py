import logging
import sys


class LoggerWriter:
    def __init__(self, logger, level):
        self.logger = logger
        self.level = level

    def write(self, message):
        if message != '\n':
            self.logger.log(self.level, message)

    def flush(self):
        pass


log = logging.getLogger('STDOUT')
sys.stdout = LoggerWriter(log, logging.INFO)
log.info('Test to standard out')
