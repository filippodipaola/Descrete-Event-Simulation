# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 16:16:13 2016

@author: VMdev
"""

from django.db import models


class Street(models.Model):
    street_name = models.CharField(default='Street 1 w/ 30 house etc', max_length=300)
    #This is a cheats way of getting the houses that are in the street.
    house_list = models.CharField(max_length=1000)

class House(models.Model):
    house_type = models.CharField(default='Terraced, Semi, etc',max_length = 200)
    number_of_occupants = models.IntegerField(default=1)
    house_name = models.CharField(max_length=300)
    def __str__(self):
        return "Name: %s, Type: %s, No of occupants: %s" %(self.house_name, self.house_type, self.number_of_occupants)
    
class Simulation(models.Model):
    house_id = models.ForeignKey(House, blank=True, null=True)
    html = models.CharField(max_length=99999)
    total_consumption = models.IntegerField(default=1)
    def __str__(self):
      return "ID: %s house: %s, total_consumption %s" %(self.id, self.house_id, self.total_consumption)
class OperationTimes(models.Model):
    on_time = models.TimeField()
    off_time = models.TimeField()
    hours = models.IntegerField(default=0)
    minutes = models.IntegerField(default=0)
    def __str__(self):
      return str(self.on_time)[:-3]
    #def start_time(self):
    #  print on_time
    #  return '10.00'

class Appliance(models.Model):
    name_text = models.CharField(max_length=300)
    watts = models.IntegerField(default=0)
    default_time = models.ForeignKey(OperationTimes, blank=True, null=True)
    def __str__(self):
        return "Name: %s, Watts: %s" %(self.name_text, self.watts)
    

class Table_Link(models.Model):
  house_id = models.ForeignKey(House, blank=True, null=True)
  appliance_id = models.ForeignKey(Appliance, blank=True, null=True)
  operation_id = models.ForeignKey(OperationTimes, blank=True, null=True)
  street_id = models.ForeignKey(Street, blank=True, null=True)
  
  def __str__(self):
    return "House ID: %s, Appliance ID: %s, Operation ID: %s" %(self.house_id, self.appliance_id, self.operation_id)