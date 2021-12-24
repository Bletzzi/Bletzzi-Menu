# Main File
# Copyright Bletzzi


# imports:
from colorama import Fore, init, Back
from time import sleep
import os
import requests
import random
import json

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def cpf_generator():
    print("CPF Generated: " + random.choice("1234567890") + random.choice("1234567890") + random.choice("1234567890") + random.choice("1234567890") + random.choice("1234567890") + random.choice("1234567890") + random.choice("1234567890") + random.choice("1234567890") + random.choice("1234567890") + "-" + random.choice("1234567890") + random.choice("1234567890"))

cpf_generator()

def menu():
    clear()
    print(Fore.LIGHTGREEN_EX + "==================")
    print(Fore.LIGHTGREEN_EX + "   Bletzzi Menu")
    print(Fore.LIGHTGREEN_EX + "==================")
    print(Fore.LIGHTGREEN_EX + "Version: 1.0")
    print(Fore.LIGHTGREEN_EX + "Author: Bletzzi")
    print(Fore.LIGHTGREEN_EX + "==================")
    print(Fore.LIGHTRED_EX + "I am not responsible for your actions\n")
    print(Fore.LIGHTCYAN_EX + "[1] Track IP Adress")
    print(Fore.LIGHTCYAN_EX + "[2] Track Postal Code")
    print(Fore.LIGHTCYAN_EX + "[3] Generate CPF\n")
    print(Fore.LIGHTCYAN_EX + "[99] Exit\n")

    option = input(Fore.LIGHTGREEN_EX + "Choose a option:\n")
    if option == "1":
        clear()
        ip = input("Enter the ip to be consulted:\n")
        ip_data = requests.get("http://ipwhois.app/json/" + ip)
        ip_data = ip_data.json()
        ip_data_type = ip_data['type']
        ip_data_continent = ip_data['continent']
        ip_data_continent_code = ip_data['continent_code']
        ip_data_country = ip_data['country']
        ip_data_country_code = ip_data['country_code']
        ip_data_country_capital = ip_data['country_capital']
        ip_data_country_phone = ip_data['country_phone']
        ip_data_country_neighbours = ip_data['country_neighbours']
        ip_data_region = ip_data['region']
        ip_data_city = ip_data['city']
        ip_data_latitude = ip_data['latitude']
        ip_data_longitude = ip_data['longitude']
        ip_data_asn = ip_data['asn']
        ip_data_org = ip_data['org']
        ip_data_isp = ip_data['isp']
        ip_data_timezone = ip_data['timezone']
        ip_data_timezone_name = ip_data['timezone_name']
        ip_data_timezone_dstOffset = ip_data['timezone_dstOffset']
        ip_data_timezone_gmtOffset = ip_data['timezone_gmtOffset']
        ip_data_timezone_gmt = ip_data['timezone_gmt']
        ip_data_currency = ip_data['currency']
        ip_data_currency_code = ip_data['currency_code']
        ip_data_currency_symbol = ip_data['currency_symbol']
        ip_data_currency_rates = ip_data['currency_rates']
        ip_data_currency_plural = ip_data['currency_plural']
        print("Type: " + ip_data_type)
        print("Continent: " + ip_data_continent)
        print("Continent Code: " + ip_data_continent_code)
        print("Country: " + ip_data_country)
        print("Country Code: " + ip_data_country_code)
        print("Country Capital: " + ip_data_country_capital)
        print("Country Phone: " + ip_data_country_phone)
        print("Country Neighbours: " + ip_data_country_neighbours)
        print("Region: " + ip_data_region)
        print("City: " + ip_data_city)
        print(ip_data_latitude)
        print(ip_data_longitude)
        print("ASN: " + ip_data_asn)
        print("ORG: " + ip_data_org)
        print("ISP: " + ip_data_isp)
        print("Timezone: " + ip_data_timezone)
        print("Timezone Name: " + ip_data_timezone_name)
        print("Timezone GMT: " + ip_data_timezone_gmt)
        print("Currency: " + ip_data_currency)
        print("Currency Code: " + ip_data_currency_code)
        print("Currency Symbol: " + ip_data_currency_symbol)
        print("Currency Plural: " + ip_data_currency_plural)
        input("\nPress any key to continue")

    elif option == "2":
        clear()
        postal_code = input("Enter the Postal Code to be consulted:\n")
        postal_code_data = requests.get("https://viacep.com.br/ws/{}/json/".format(postal_code))
        postal_code_data = postal_code_data.json()
        postal_code_data_public_place = postal_code_data['logradouro']
        postal_code_data_complement = postal_code_data["complemento"]
        postal_code_data_district = postal_code_data["bairro"]
        postal_code_data_locality = postal_code_data["localidade"]
        postal_code_data_uf = postal_code_data["uf"]
        postal_code_data_ibge = postal_code_data["ibge"]
        postal_code_data_gia = postal_code_data["gia"]
        postal_code_data_ddd = postal_code_data["ddd"]
        postal_code_data_siafi = postal_code_data["siafi"]
        print("Postal Code: " + postal_code)
        print("Public Place: " + postal_code_data_public_place)
        print("Complement: " + postal_code_data_complement)
        print("district: " + postal_code_data_district)
        print("locality: " + postal_code_data_locality)
        print("UF: " + postal_code_data_uf)
        print("IBGE: " + postal_code_data_ibge)
        print("GIA: " + postal_code_data_gia)
        print("DDD: " + postal_code_data_ddd)
        print("Siafi: " + postal_code_data_siafi)
        input("\nPress any key to continue")
    elif option == "3":
        clear()
        cpf_generator()
        input("\nPress any key to continue")
while True:
    menu()