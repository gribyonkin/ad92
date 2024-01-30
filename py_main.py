import json

def fun1(hashMap,_files=None,_data=None):

  hashMap.put("toast","Создали чек ККМ")

  return hashMap

def get_prices(hashMap,_files=None,_data=None):

  hashMap.put("toast","Мой первый коммит!!! ad92")

  return hashMap

def after_scan(hashMap,_files=None,_data=None):

  hashMap.put("article","oc90")
  hashMap.put("brand","Mahle")
  hashMap.put("warname", hashMap.get("barcode"))
  hashMap.put("ShowScreen","Найден товар")

  return hashMap
