GUD = GLOBAL_USERS_DICTIONARY = {}
import os
import logging
import random
IMPORTED = {}
import requests
import requests
from loguru import logger
from telegram.ext import CallbackContext
from telegram import ChatAction, Update
import requests
import importlib
from bs4 import BeautifulSoup
INPUT_PHONE_NUMBER, INPUT_TG_CODE = range(2)
GLOBAL_USERS_DICTIONARY = {}
from telegram import ParseMode
from telegram.ext import CommandHandler,MessageHandler,Filters,ConversationHandler
from base64 import b64decode
from FONK import *
from telegram.ext import Updater
updater = Updater(TG_BOT_TOKEN)
hypeVoid = updater.dispatcher
class InterceptHandler(logging.Handler):
    LEVELS_MAP = {
        logging.CRITICAL: "CRITICAL",
        logging.ERROR: "ERROR",
        logging.WARNING: "WARNING",
        logging.INFO: "INFO",
        logging.DEBUG: "DEBUG"}
    def _get_level(self, record):
        return self.LEVELS_MAP.get(record.levelno, record.levelno)
    def emit(self, record):
        logger_opt = logger.opt(depth=6, exception=record.exc_info, ansi=True, lazy=True)
        logger_opt.log(self._get_level(record), record.getMessage())
logging.basicConfig(handlers=[InterceptHandler()], level=logging.INFO)
HYPEEED = logging.getLogger(__name__)