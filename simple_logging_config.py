import logging
import logging.config

logging.config.fileConfig('logging.conf')
logging.basicConfig(filename = 'speedlog.log', level = logging.debug)

# create logger
logger = logging.getLogger('root')

# 'application' code
logging.debug('debug message')
logging.info('info message')
logging.warn('warn message')
logging.error('error message')
logging.critical('critical message')