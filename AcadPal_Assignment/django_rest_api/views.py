from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from django_rest_api.models import *
from django_rest_api.serializer import *
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
import django_filters

@api_view(['GET', 'POST', 'DELETE'])
def country_list(request):
    # GET list of Countries, POST a new Country, DELETE all Countries
    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 5
        countries = Country.objects.all()
        result_page = paginator.paginate_queryset(countries, request)
        serializer = CountrySerializer(result_page, many=True)
        return JsonResponse(serializer.data, safe = False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        country_data = JSONParser().parse(request)
        country_serializer = CountrySerializer(data=country_data)
        if country_serializer.is_valid():
            country_serializer.save()
            return JsonResponse(country_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(country_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        	count = Country.objects.all().delete()
        	return JsonResponse({'message': '{} Countries were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    else:
    	return JsonResponse({'message': 'The Country does not exist'}, status=status.HTTP_404_NOT_FOUND) 

 
@api_view(['GET', 'PUT', 'DELETE'])
def country_detail(request, pk):
    # find Country by pk (id)
    try: 
        country = Country.objects.get(pk=pk) 
        if request.method == 'GET': 
	        country_serializer = CountrySerializer(country) 
	        return JsonResponse(country_serializer.data) 
        elif request.method == 'PUT': 
	        country_data = JSONParser().parse(request) 
	        country_serializer = CountrySerializer(country, data=country_data) 
	        if country_serializer.is_valid(): 
	            country_serializer.save() 
	            return JsonResponse(country_serializer.data) 
        	return JsonResponse(country_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        elif request.method == 'DELETE': 
	        country.delete() 
	        return JsonResponse({'message': 'Country was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except Country.DoesNotExist: 
        return JsonResponse({'message': 'The Country does not exist'}, status=status.HTTP_404_NOT_FOUND) 

@api_view(['GET', 'POST', 'DELETE'])
def state_list(request):
    # GET list of States, POST a new State, DELETE all States
    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 5
        states = State.objects.all()
        result_page = paginator.paginate_queryset(states, request)
        serializer = StateSerializer(result_page, many=True)
        return JsonResponse(serializer.data, safe = False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        state_data = JSONParser().parse(request)
        state_serializer = StateSerializer(data=state_data)
        if state_serializer.is_valid():
            state_serializer.save()
            return JsonResponse(state_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(state_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
            count = State.objects.all().delete()
            return JsonResponse({'message': '{} States were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    else:
        return JsonResponse({'message': 'The States does not exist'}, status=status.HTTP_404_NOT_FOUND) 

 
@api_view(['GET', 'PUT', 'DELETE'])
def state_detail(request, pk):
    # find State by pk (id)
    try: 
        state = State.objects.get(pk=pk) 
        if request.method == 'GET': 
            state_serializer = StateSerializer(state) 
            return JsonResponse(state_serializer.data) 
        elif request.method == 'PUT': 
            state_data = JSONParser().parse(request) 
            state_serializer = StateSerializer(state, data=state_data) 
            if state_serializer.is_valid(): 
                state_serializer.save() 
                return JsonResponse(state_serializer.data) 
            return JsonResponse(state_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        elif request.method == 'DELETE': 
            state.delete() 
            return JsonResponse({'message': 'State was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except State.DoesNotExist: 
        return JsonResponse({'message': 'The State does not exist'}, status=status.HTTP_404_NOT_FOUND) 

@api_view(['GET', 'POST', 'DELETE'])
def city_list(request):
    # GET list of Cities, POST a new City, DELETE all Cities
    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 5
        cities = City.objects.all()
        result_page = paginator.paginate_queryset(cities, request)
        serializer = CitySerializer(result_page, many=True)
        return JsonResponse(serializer.data, safe = False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        city_data = JSONParser().parse(request)
        city_serializer = CitySerializer(data=city_data)
        if city_serializer.is_valid():
            city_serializer.save()
            return JsonResponse(city_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(city_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
            count = City.objects.all().delete()
            return JsonResponse({'message': '{} Cities were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    else:
        return JsonResponse({'message': 'The City does not exist'}, status=status.HTTP_404_NOT_FOUND) 

 
@api_view(['GET', 'PUT', 'DELETE'])
def city_detail(request, pk):
    # find City by pk (id)
    try: 
        city = City.objects.get(pk=pk) 
        if request.method == 'GET': 
            city_serializer = CitySerializer(city) 
            return JsonResponse(city_serializer.data) 
        elif request.method == 'PUT': 
            city_data = JSONParser().parse(request) 
            city_serializer = CitySerializer(city, data=city_data) 
            if city_serializer.is_valid(): 
                city_serializer.save() 
                return JsonResponse(city_serializer.data) 
            return JsonResponse(city_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        elif request.method == 'DELETE': 
            city.delete() 
            return JsonResponse({'message': 'City was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except City.DoesNotExist: 
        return JsonResponse({'message': 'The City does not exist'}, status=status.HTTP_404_NOT_FOUND) 

@api_view(['GET', 'POST', 'DELETE'])
def person_list(request):
    # GET list of Person, POST a new Person, DELETE all Persons
    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 5
        persons = Person.objects.all()
        result_page = paginator.paginate_queryset(persons, request)
        serializer = PersonSerializer(result_page, many=True)
        return JsonResponse(serializer.data, safe = False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        person_data = JSONParser().parse(request)
        person_serializer = PersonSerializer(data=person_data)
        if person_serializer.is_valid():
            person_serializer.save()
            return JsonResponse(person_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(person_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
            count = Person.objects.all().delete()
            return JsonResponse({'message': '{} Persons were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
    else:
        return JsonResponse({'message': 'The Person does not exist'}, status=status.HTTP_404_NOT_FOUND) 


@api_view(['GET', 'PUT', 'DELETE'])
def person_detail(request, pk):
    # find Person by pk (id)
    try: 
        person = Person.objects.get(pk=pk) 
        if request.method == 'GET': 
            person_serializer = PersonSerializer(person) 
            return JsonResponse(person_serializer.data) 
        elif request.method == 'PUT': 
            person_data = JSONParser().parse(request) 
            person_serializer = PersonSerializer(person, data=person_data) 
            if person_serializer.is_valid(): 
                person_serializer.save() 
                return JsonResponse(person_serializer.data) 
            return JsonResponse(person_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        elif request.method == 'DELETE': 
            person.delete() 
            return JsonResponse({'message': 'Person was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except Person.DoesNotExist: 
        return JsonResponse({'message': 'The Person does not exist'}, status=status.HTTP_404_NOT_FOUND) 

def search_view(request, country_name):
    persons = Person.objects.all()
    if persons is not None:
        persons = persons.filter(city__state__country__name__contains = country_name)
    serializer = PersonSerializer(persons, many =True)
    return JsonResponse(serializer.data, safe = False)