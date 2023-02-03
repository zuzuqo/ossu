from urllib import request, parse, error
import json
import ssl

api_key = False
# api_key = 'AIzaSy_IDByT70'

if api_key is False:
    api_key = 42
    service_url = 'http://py4e-data.dr-chuck.net/json?'
else:
    service_url = 'http://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = service_url + parse.urlencode(parms)

    print('Retrieving', url)
    uh = request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    # print(json.dumps(js, indent=4))

    area_type = js['results'][0]['address_components'][0]['types'][0]
    try:
        if len(js['results'][0]['address_components']) > 1:
            country_code = js['results'][0]['address_components'][-1]['short_name']
        else:
            country_code = None
    except:
        country_code = None

    if country_code != None or area_type == 'establishment':
        lat = js['results'][0]['geometry']['location']['lat']
        lng = js['results'][0]['geometry']['location']['lng']
        if country_code != None:
            print(f"lat: {lat}, lng: {lng}, country code: {country_code}")
        else:
            print(f"lat: {lat}, lng: {lng}")


    # lat = js['results'][0]['geometry']['location']['lat']
    # lng = js['results'][0]['geometry']['location']['lng']
    # print(f"lat: {lat}, lng: {lng}")
    # location = js['results'][0]['formatted_address']
    # print(location)
