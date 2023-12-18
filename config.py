import os
import telebot
from telebot import types
import emoji
from flask import Flask, Blueprint, make_response, request, render_template
from flask_restful import Api, Resource
# from pymongo import MongoClient
import random
import requests
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

# Configuration variable
TOKEN = os.getenv("TOKEN")

WEBHOOK_MODE = os.getenv("WEBHOOK_MODE")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# DATABASE_URL = os.getenv("DATABASE_URL")
# DATABASE_NAME = os.getenv("DATABASE_NAME")

bot = telebot.TeleBot(TOKEN, threaded=True)

# Initialize application
app = Flask(__name__)

# client = MongoClient(DATABASE_URL)
# db = client[DATABASE_NAME]

# Logging Setup
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
)