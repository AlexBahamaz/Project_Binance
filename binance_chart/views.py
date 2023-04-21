from django.shortcuts import render
import pandas as pd
import json
from binance.client import Client # pip install python-binance
# Create your views here.
client = Client()

def index(request):
    dataSet = pd.DataFrame(client.get_all_tickers())
    json_records = dataSet[:200].reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}
    return render(request, 'index.html', context)

def graph(request):
    return(request, 'graph.html')

