# ===========
# mymodule.py
# ===========

from urllib.request import urlopen
import json

def get_weather(city):
    print ("Hello to GitHub")

def postal_lookup(postal_code):
    sock = urlopen("http://api.postcodes.io/postcodes/" + postal_code)
    result = sock.read()                            
    sock.close()                                        
    details = json.loads(result)
    return (details["result"]["latitude"], details["result"]["longitude"])

if __name__ == "__main__":
    degrees = get_weather("SINGAPORE")
    print("Weather in SINGAPORE is %.2f degrees Celsius" % degrees)

    location = postal_lookup("B323PP")
    print(location)
