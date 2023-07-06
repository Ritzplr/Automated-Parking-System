from sqlite3 import IntegrityError
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from parking_app.models import Parking
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from imaplib import _Authenticator
from django.contrib.auth.models import User
#for demo
from collections import defaultdict
from .models import ParkingSpace, Distance, ParkingSlot
from .utils import calculate_shortest_distance



# Create your views here.

def home(request):
    return render(request,'home.html')

def index(request):
    # return HttpResponse('this is home page')
    if (request.method == "POST"):
        state = request.POST.get('state')
        vehicle_no = request.POST.get('vehicle_no')
        vehicle_type = request.POST.get('vehicle_type')

        parking = Parking(state=state, vehicle_no=vehicle_no,
                          vehicle_type=vehicle_type, park_time=datetime.now().time(), park_date=datetime.today())

        try:
            parking.save()
            messages.success(request, ' Your slot has been booked...')
        except IntegrityError as e:
            messages.error(' Invalid Entry...')
        


    # all_vehicle = Parking.objects.all().count()
    two_wheel = Parking.objects.filter(vehicle_type="2 Wheeler").count()
    four_wheel = Parking.objects.filter(vehicle_type="4 Wheeler").count()

    context = {'total': (two_wheel+four_wheel), 'remain': (100-(two_wheel+four_wheel)),
               'two_wheel': 50-two_wheel, 'four_wheel': 50-four_wheel, 'booked_two': two_wheel, 'booked_four': four_wheel}
    return render(request, 'index.html', context)



def parking(request):
    all_vehicle = Parking.objects.all()
    exit_time = datetime.now().time()
    exit_date = datetime.today()
    context = {'vehicles': all_vehicle,
               'exit_time': exit_time, 'exit_date': exit_date}
    return render(request, 'parking.html', context)


#for demo
def calculate_shortest_distance_view(request):
    parking_spaces = ParkingSpace.objects.all()

    if not parking_spaces:
        # Handle the case when no parking spaces exist
        return HttpResponse("No parking spaces found.")

    graph = defaultdict(dict)

    for space in parking_spaces:
        for distance in space.distances_to.all():
            graph[space.number][distance.destination.number] = distance.distance

    root_parking_space = parking_spaces.first()
    distances = calculate_shortest_distance(graph, root_parking_space.number)

    # Get the parking slots for the targeted parking space
    targeted_parking_space = ParkingSpace.objects.get(number=10) #define I/O func later
    parking_slots = ParkingSlot.objects.filter(space=targeted_parking_space)

    return render(request, 'shortest_distance.html', {'distances': distances, 'root_parking_space': root_parking_space, 'parking_slots': parking_slots})

#for Signin and signup
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)

        if user is not None:
           login(request, user)
           messages.success(request,"login Successfully.")
           return render(request,"home.html", )
           

        else:
            messages.error(request,"Wrong Credentials!!")
            return redirect('signin.html')

    return render(request, 'signin.html')

def signup(request):

    if request.method=="POST":
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        confirmpassword= request.POST['confirmpassword']

        railwayuser = User.objects.create_user(username,email,password)
        railwayuser.save()

        messages.success(request,"Your Account has been Successfully Created.")

        return redirect('signin.html')


    return render(request, 'signup.html')