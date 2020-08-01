from rest_framework import serializers 
from django_rest_api.models import Country, State, City, Person
 
 
class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id',
                  'name',
                  'description',
                  'population',
                  'gdp')

class StateSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = State
        fields = ('id',
                  'name',
                  'description',
                  'population',
                  'gdp',
                  'country')
    def to_representation(self, instance):
        self.fields['country'] =  CountrySerializer(read_only=True)
        return super(StateSerializer, self).to_representation(instance)

class CitySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = City
        fields = ('id',
                  'name',
                  'description',
                  'population',
                  'gdp',
                  'state')
    def to_representation(self, instance):
        self.fields['state'] =  StateSerializer(read_only=True)
        return super(CitySerializer, self).to_representation(instance)

class PersonSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Person
        fields = ('id',
                  'fname',
                  'mname',
                  'lname',
                  'city')
    def to_representation(self, instance):
        self.fields['city'] =  CitySerializer(read_only=True)
        return super(PersonSerializer, self).to_representation(instance)