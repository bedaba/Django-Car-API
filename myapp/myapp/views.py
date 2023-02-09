from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.views.decorators.csrf import csrf_exempt

import json

from myapp.models import Car

def index(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')

def get_car(request, car_name):
    if request.method == 'GET':
        try:
            car = Car.objects.get(name=car_name)
            response = json.dumps([{ 'Car': car.name, 'Top Speed': car.top_speed}])
        except:
            response = json.dumps([{ 'Error': 'No car with that name'}])
    return HttpResponse(response, content_type='text/json')

@csrf_exempt
def add_car(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        car_name = payload['car_name']
        top_speed = payload['top_speed']
        car = Car(name=car_name, top_speed=top_speed)
        try:
            car.save()
            response = json.dumps([{ 'Success': 'Car added successfully!'}])
        except:
            response = json.dumps([{ 'Error': 'Car could not be added!'}])
    return HttpResponse(response, content_type='text/json')


import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def update_car(request, car_name):
    if request.method == 'PUT':
        try:
            car = Car.objects.get(name=car_name)
        except Car.DoesNotExist:
            response = json.dumps([{'Error': 'Car not found!'}])
            return HttpResponse(response, content_type='text/json', status=404)

        payload = json.loads(request.body)
        car_name = payload.get('car_name', car.name)
        top_speed = payload.get('top_speed', car.top_speed)

        try:
            car.name = car_name
            car.top_speed = top_speed
            car.save()
            response = json.dumps([{'Success': 'Car updated successfully!'}])
        except Exception as e:
            logger.error('Error updating car: {}'.format(e))
            response = json.dumps([{'Error': 'Car could not be updated!'}])

    return HttpResponse(response, content_type='text/json')

@csrf_exempt
def get_all_cars(request):
    if request.method == 'GET':
        cars = Car.objects.all()
        car_list = []
        for car in cars:
            car_dict = {'Car': car.name, 'Top Speed': car.top_speed}
            car_list.append(car_dict)
        response = json.dumps(car_list)
    return HttpResponse(response, content_type='text/json')

@csrf_exempt
def delete_car(request, car_name):
    response = json.dumps([{ 'Error': 'Invalid request method!'}])
    if request.method == 'DELETE':
        try:
            car = Car.objects.get(name=car_name)
            car.delete()
            response = json.dumps([{ 'Success': 'Car deleted successfully!'}])
        except:
            response = json.dumps([{ 'Error': 'Car could not be deleted!'}])
    return HttpResponse(response, content_type='text/json')