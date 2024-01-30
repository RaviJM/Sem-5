from bs4 import BeautifulSoup
import requests
import csv


def f(a,b):
    file = "D:\\News\\op.csv"

    with open(file, 'a', newline='') as fp:
        csvW = csv.writer(fp)
        csvW.writerow([a, b])
    fp.close()

def callme():
    file = "D:\\News\\op.csv"

    with open(file, 'w', newline='') as fp:
        pass
    fp.close()

callme()
f("andu, makwana", "acha, boht")
f("gondu, sharma", "gandu, boht")

