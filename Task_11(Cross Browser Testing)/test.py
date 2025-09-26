from selenium import webdriver
from selenium.webdriver.edge.service import Service

edge_driver_path = r"C:\Users\VIMAL RAJ\Downloads\edgedriver_win64\msedgedriver.exe"
service = Service(edge_driver_path)
driver = webdriver.Edge(service=service)
driver.get("https://www.google.com")

