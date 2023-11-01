from django.shortcuts import render,HttpResponse
from panel.models import Bank 
# Create your views here.
def index(request):
    return render(request,'index.html')

# Function to create data in Database
def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        contact = request.POST.get('contact')
        account_no = request.POST.get('account_no')
        balance = request.POST.get('balance')
        account_type = request.POST.get('account_type')
        obj = Bank(name=name,email=email,password=password,contact=contact,account_no=account_no,balance=balance,account_type=account_type)
        obj.save()
        print("The Data has been Successfully Saved in the Database")
    return render(request,'create.html')

# Function to show all the data from Database
def show(request):
    user = Bank.objects.all()
    return render(request,'show.html',{'user':user})

# Function to search data from Database
def search(request): 
    user = None
    if request.method == "POST":
        name = request.POST.get('name')
        account_no = request.POST.get('account_no')
        if(name and account_no):
            user = Bank.objects.filter(name=name,account_no=account_no)
    return render(request,'search.html',{'user':user})


# Function to transfer money from one account to another
def transfer(request):
    if request.method == "POST":
        name = request.POST.get('name')
        sender_account = request.POST.get('sender_account')
        receiver_account = request.POST.get('receiver_account')
        amount = request.POST.get('amount')
        
        # Fetching the data of sender and receiver from Database
        sender = Bank.objects.get(name=name,account_no=sender_account)
        receiver = Bank.objects.get(account_no=receiver_account)
        
        # Checking if the sender has enough balance to transfer
        if(sender.balance < int(amount)):
            print("Insufficient Balance")
        else:
            sender.balance = sender.balance - int(amount)
            receiver.balance = receiver.balance + int(amount)
            sender.save()
            receiver.save()
            print("Amount has been successfully transferred")
        
    return render(request,'transfer.html')