import json
import numpy as np
import pandas as pd
import requests
import matplotlib.pyplot as plt
import datetime

#create API function
def get_json(api_url):
	response = requests.get(api_url)
	if response.status_code == 200:
		return json.loads(response.content.decode('utf-8'))
	else:
		return None
