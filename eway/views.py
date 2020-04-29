from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.
def home(request):
	customers = Customer.objects.all()
	orders = Order.objects.all()
	
	total_customer = customers.count()
	total_order = orders.count()
	total_delivered = orders.filter(status = 'Delivered').count()
	total_pending = orders.filter(status = 'Pending').count()


	return render(request,'eway/dashboard.html',{'customers':customers,'orders':orders,'total_order':total_order,'total_delivered':total_delivered,'total_pending':total_pending})

def product(request):
	products = Product.objects.all()

	return render(request,'eway/product.html',{'products':products})

def customer(request,pk_test):
	customer = Customer.objects.get(id=pk_test)

	orders = customer.order_set.all()# Relationship Used
	order_count = orders.count()

	context = {'customer':customer, 'orders':orders, 'order_count':order_count}
	
	return render(request,'eway/customer.html',context)

def createOrder(request):
	form = OrderForm()
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	return render(request,'eway/order_form.html',{'form':form})


def updateOrder(request,pk):
	order = Order.objects.get(id = pk)
	form = OrderForm(instance = order)
	if request.method == 'POST':
		form = OrderForm(request.POST, instance = order)
		if form.is_valid():
			form.save()
			return redirect('/')

	return render(request,'eway/order_form.html',{'form':form})


def deleteOrder(request,pk):
	order = Order.objects.get(id = pk)
	if request.method == 'POST':
		order.delete()
		return redirect('/')

	return render(request,'eway/delete_order.html',{'item':order})