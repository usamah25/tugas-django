from django.shortcuts import render
from subcribe_app.models import Customer
from subcribe_app.forms import NewSubscriber

# Create your views here.
def index(request):
    return render(request, 'subcribe_app/index.html')

def customers(request):
    customers_list = Customer.objects.order_by('first_name')
    customer_dict = {'customers': customers_list}
    return render(request, 'subcribe_app/customers.html', context=customer_dict)

def subscribe(request):
    form = NewSubscriber()

    if request.method == 'POST':
        form = NewSubscriber(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return customers(request)
    else:
        print("Error: form invalid" )

    return render(request, 'subcribe_app/subscribe.html', {'form' :form})