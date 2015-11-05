__author__ = 'Roy'
import requests
import codecs
import xmltodict


gekozenstation= ""

auth_details = ('username', 'password')

def schrijf_xml(bestandsnaam, response):
    bestand = codecs.open(bestandsnaam, "w", "utf-8")
    bestand.write(str(response.text))
    bestand.close()


def create_stationlist():
    bestand = open('stationslijst.xml', 'r')
    xml_string = bestand.read()
    return xmltodict.parse(xml_string)

def create_vertreklist():
    bestand = open('vertrektijden.xml', 'r')
    xml_string = bestand.read()
    return xmltodict.parse(xml_string)

def input_station():
        global gekozenstation
        station = input('Voer een station in:\n')
        if station in lijst_stations:
            gekozenstation  = station
            return vertrektijden_lijst(station)
        else:
            print ('Station bestaat niet\n')
            input_station()

def is_geldig_station(station):
    if station in lijst_stations:
        return True
    return False


def vertrektijden_lijst(station):
    url = 'http://webservices.ns.nl/ns-api-avt?station=' + station
    response = requests.get(url, auth = auth_details)
    schrijf_xml('vertrektijden.xml',response)
    return xmltodict.parse(response.text)



station_url = 'http://webservices.ns.nl/ns-api-stations-v2'
response = requests.get(station_url, auth = auth_details)
schrijf_xml('stationslijst.xml',response)
stations_dict = create_stationlist()

lijst_stations = []
for station_naam in stations_dict['Stations']['Station']:
    lijst_stations.append(station_naam['Namen']['Lang'])



lijst_vertrek = []
