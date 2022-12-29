# Import phonenumbers module
import phonenumbers
from phonenumbers import timezone, geocoder, carrier

# Getting phone number as an user input
number = input("Enter the Phone Number with Country Code : ")

if len(number)>13:
    print("You have exceeded the no. of digits in phone number, Try Again!!")
    exit()

if len(number)<13:
    print("Your Phone Number is too short. Please Enter Phone Number with country code!!")
    exit()

else:
    try:
        # Parsing number string as phone_number
        phone_number = phonenumbers.parse(number)

        # Getting Time zone of the phone number
        time_zone = timezone.time_zones_for_number(phone_number)

        # Removing Unwanted Characters from time_zone list
        time_zone = str(time_zone)
        time_zone = time_zone.replace("('", "")
        time_zone = time_zone.replace("',)", "")
        

        # Getting region information
        region = geocoder.description_for_number(phone_number, 'en')

        # Getting carrier of a phone number
        phoneno_carrier = carrier.name_for_number(phone_number, 'en')

        #Printing Information
        print(phone_number)
        print("Timezone : ", time_zone)
        print("Region : ", region)
        print("SIM Provider : ", phoneno_carrier)

    except:
        print("This Phone Number May Not Exist or any other Problem Occured, Pease Try Again!!")
