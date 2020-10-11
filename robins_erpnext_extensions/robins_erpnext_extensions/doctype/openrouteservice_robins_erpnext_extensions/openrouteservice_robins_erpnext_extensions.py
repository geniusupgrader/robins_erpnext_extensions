# -*- coding: utf-8 -*-
# Copyright (c) 2020, Robin Rosenstock and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import enqueue
import openrouteservice as ors
import time


class OpenRouteService_robins_erpnext_extensions(Document):


	def validate(self):
		pass
		# frappe.msgprint("hallo")
		# self.duration_compute = "validate"


@frappe.whitelist()
def get_distance_and_duration(destination_address):

	doc = frappe.get_doc('OpenRouteService_robins_erpnext_extensions')
	client = ors.Client(key=doc.api_openrouteservice)
	home_address = doc.address_line1+", "+doc.pincode+" "+doc.city+", "+doc.country

	home_address_location = client.pelias_search(text=home_address)
	home_address_coordinates = home_address_location["features"][0]["geometry"]["coordinates"]

	destination_address_location = client.pelias_search(text=destination_address)
	destination_address_coordinates = destination_address_location["features"][0]["geometry"]["coordinates"]

	coordinates = [home_address_coordinates, destination_address_coordinates]

	route = client.directions(coordinates=coordinates, profile='driving-car', geometry_simplify=True, instructions=False, geometry=False)


	distance_and_duration = route.get("routes")[0].get("summary")
	distance = distance_and_duration["distance"]
	duration = distance_and_duration["duration"]
	
	distance = distance/1000
	duration = duration/60

	return distance, duration



@frappe.whitelist()
def update_all():
	enqueue(long_job, arg1="arg1", arg2="arg2")



@frappe.whitelist()
def long_job(arg1, arg2):

	frappe.publish_realtime('msgprint', 'Starting long job...')

	doc = frappe.get_doc('OpenRouteService_robins_erpnext_extensions')
	client = ors.Client(key=doc.api_openrouteservice)
	home_address = doc.address_line1+", "+doc.pincode+" "+doc.city+", "+doc.country

	home_address_location = client.pelias_search(text=home_address)
	home_address_coordinates = home_address_location["features"][0]["geometry"]["coordinates"]

	# get list of all adresses
	all_adresses = frappe.db.get_list("Address", fields=['name'], as_list=True)


	for i in all_adresses:
		# strip it from
		address_id = i[0]

		print(address_id)

		address_line1 = frappe.db.get_value("Address", address_id, "address_line1")
		pincode = frappe.db.get_value("Address", address_id, "pincode")
		city = frappe.db.get_value("Address", address_id, "city")
		country = frappe.db.get_value("Address", address_id, "country")

		destination_address = str(address_line1)+", "+str(pincode)+" "+str(city)

		print(destination_address)

		destination_address_location = client.pelias_search(text=destination_address)

		destination_address_coordinates = destination_address_location["features"][0]["geometry"]["coordinates"]

		print(destination_address_coordinates)

		coordinates = [home_address_coordinates, destination_address_coordinates]


		route = client.directions(coordinates=coordinates, profile='driving-car', geometry_simplify=True, instructions=False, geometry=False)

		distance_and_duration = route.get("routes")[0].get("summary")

		print(distance_and_duration)

		try:
			distance = distance_and_duration["distance"]
			distance = distance/1000
		except:
			distance = 0
		try:
			duration = distance_and_duration["duration"]
			duration = duration/60
		except:
			duration = 0

		frappe.db.set_value("Address", address_id, "distance", distance)
		frappe.db.set_value("Address", address_id, "duration_from_home_address_in_minutes", duration)

		time.sleep(1.6)



	frappe.publish_realtime('msgprint', 'Ending long job...')



	return distance, duration
