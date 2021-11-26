import phonenumbers
from phonenumbers import carrier,geocoder,timezone

mobileNo=phonenumbers.parse("+91 99990 55525")                        #write phone number
print(timezone.time_zones_for_number(mobileNo))
print(carrier.name_for_number(mobileNo,"en"))
print(geocoder.description_for_number(mobileNo,"en"))
print("Valid Mobile Number:",phonenumbers.is_valid_number(mobileNo))
print("Checking_possibility of Number:",phonenumbers.is_possible_number(mobileNo))
