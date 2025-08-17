from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from web3 import Web3

def dashboard(request):
    # w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
    # print("Connected:", w3.is_connected())
    # print("Latest block:", w3.eth.block_number)
    return render(request,'dashboard.html')

