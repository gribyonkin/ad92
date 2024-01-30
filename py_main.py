
import requests
import json

def fun1(hashMap,_files=None,_data=None):

  hashMap.put("toast","Создали чек ККМ")

  return hashMap

def get_prices(hashMap,_files=None,_data=None):
    
  art = hashMap.get("article")
  brnd = hashMap.get("brand")

  param_tuples = [('key', 's6e1IlkWJJfzNu07e8fvuIBcAZmnJB5e'), ('article', art), ('brand', brnd)]
  response = requests.post('https://avtodrug92.freno.ru/ApiRequest/getOneOffer', data=param_tuples)

  json_data = response.text
  #.json()

  hashMap.put("res",json_data)
  #hashMap.put("toast","Проверяем цены!!!")

  return hashMap

def after_scan(hashMap,_files=None,_data=None):

  hashMap.put("article","oc90")
  hashMap.put("brand","Mahle")
  hashMap.put("warname", hashMap.get("barcode"))
  hashMap.put("ShowScreen","Найден товар")

  return hashMap
