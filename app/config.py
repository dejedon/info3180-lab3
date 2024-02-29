import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    """Base Config Object"""
    DEBUG = True
    SECRET_KEY = "Som3$ec5etK*y"
    MAIL_SERVER = "sandbox.smtp.mailtrap.io"   
    MAIL_PORT = 465     
    MAIL_USERNAME = "a3c13cfda3dd08"  
    MAIL_PASSWORD = "ddfad67786a98b"