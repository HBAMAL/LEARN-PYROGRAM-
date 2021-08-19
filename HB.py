import os

HB = Client(
	"SAMPLE_BOT"
	bot_token = os.environ["BOT_TOKEN"],
	api_id = int(os.environ["API_ID"]),
	api_hash = os.environ["API_HASH"]
	)

START_MSG = """
HI I AM A TEST BOT MADE BY HB
"""
HELP_MSG = """ 
NO ONE GONE HELP U"""
