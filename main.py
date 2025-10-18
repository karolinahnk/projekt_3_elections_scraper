"""
main.py: třetí projekt do Engeto Online Python Akademie
author: Karolína Hynková
email: karolinahynkova97@seznam.cz
"""
import code
import sys
import requests
from bs4 import BeautifulSoup
import csv

def get_villages_data(url):
    #downloads and returns data from villages
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    #the name of the village which can be found in the tag h3
    name = soup.find("h3").text.strip()
    #table with numbers of voters and votes
    voters = soup.find("td", headers="sa2").text.strip()
    envelopes = soup.find("td", headers="sa3").text.strip()
    valid = soup.find("td", headers="sa6").text.strip()

    #table with party results
    parties = soup.find_all("td", headers="t1sa1 t1sb2")
    votes = soup.find_all("td", headers="t1sa2 t1sb3")

    results = {}
    for party, number in zip(parties, votes):
        results[party.text.strip()] = number.text.strip()

    return {
        "code_village": code,
        "name_village": name,
        "voters": voters,
        "envelopes": envelopes,
        "valid": valid,
        **results
    }

def save_to_csv(data_list, output_file):
    #saves a list of data to csv and ending election
    if not data_list:
        print("No data to save!")
        return

    headers = data_list[0].keys()
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for data in data_list:
            writer.writerow(data)

    print(f"The data was saved to: {output_file}")
    print(f"Ending the election-scraper.")

def main():
    #default values
    default_url = "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101"
    default_output = "vysledky_benesov.csv"

    #checking if all values are entered correctly
    if len(sys.argv) == 3:
        url = sys.argv[1]
        output_file = sys.argv[2]
    elif len(sys.argv) == 1:
        url = default_url
        output_file = default_output
    else:
        print("You have to input 2 arguments.")
        sys.exit(1)


    print(f"Downloading data from: {url}")
    response = requests.get(url)

    if response.status_code != 200:
        print("Request failed with status code.")
        sys.exit(1)

    #loading HTML
    soup = BeautifulSoup(response.text, "html.parser")

    #find all links in the table
    villages = []
    base_url = "https://www.volby.cz/pls/ps2017nss/"
    for link in soup.find_all("a"):
        href = link.get("href")
        text = link.text.strip()
        #we are looking for links with the villages code
        if href and text.isdigit():
            full_link = base_url + href
            villages.append((text, full_link))

    #downloading data all villages
    all_villages = []
    for code, link in villages:
        data = get_villages_data(link)
        data["code_village"] = code
        all_villages.append(data)


    save_to_csv(all_villages, output_file)

if __name__ == "__main__":
    main()
