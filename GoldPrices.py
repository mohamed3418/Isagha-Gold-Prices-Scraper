from bs4 import BeautifulSoup
import requests
import csv

url ="https://market.isagha.com/prices"
GoldPrices = []
def main_code(url) :
    page=requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")
    golds = soup.find_all("div", {"class":"isagha-panel"})

    for i in golds:
        guage = i.find("span").text
        sell_price = i.find_all("div",{"class":"value"})[0].text.strip().split()[0]
        buy_price = i.find_all("div",{"class":"value"})[1].text.strip().split()[0]
        coin =  i.find_all("div",{"class":"value"})[0].text.strip().split()[-1]
        if not coin :
            i.find_all("div",{"class":"value"}).text.strip()
            continue
        price_change = i.find_all("div",{"class":"value"})[2].text.strip()
        price_change_stat = i.find_all("div",{"class":"state"})[2].text.strip()

        GoldPrices.append(
            {
                "العيار": guage,
                "سعر الشراء": buy_price,
                "سعر البيع":sell_price,
                "العملة":coin,
                "نسبة التغير": price_change,
                "حالة التغير": price_change_stat,
            }
        )

def printing_results():
    header = GoldPrices[0].keys()
    path = "Gold_Prices.csv"
    with open(path , "w" , encoding='utf-8', newline='') as file :
        writer = csv.DictWriter(file , header)
        writer.writeheader()
        writer.writerows(GoldPrices)
        print("file printed Succefully")

main_code(url)
printing_results()


