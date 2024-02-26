
import requests
import json
import random

def fun1(hashMap,_files=None,_data=None):
    
    j = { "customcards":         {
            "options":{
              "search_enabled":True,
              "save_position":True
            },
            "layout": {
            "type": "LinearLayout",
            "orientation": "vertical",
            "height": "match_parent",
            "width": "match_parent",
            "weight": "0",
            "Elements": [
            {
                "type": "LinearLayout",
                "orientation": "horizontal",
                "height": "wrap_content",
                "width": "match_parent",
                "weight": "0",
                "Elements": [
                {
                "type": "CheckBox",
                "Value": "@cb1",
                "NoRefresh": False,
                "document_type": "",
                "mask": "",
                "Variable": "cb1",
                "BackgroundColor": "#DB7093",
                "width": "match_parent",
                "height": "wrap_content",
                "weight": 2
                },
                {
                "type": "LinearLayout",
                "orientation": "vertical",
                "height": "wrap_content",
                "width": "match_parent",
                "weight": "1",
                "Elements": [
                {
                    "type": "TextView",
                    "show_by_condition": "",
                    "Value": "@string1",
                    "NoRefresh": False,
                    "document_type": "",
                    "mask": "",
                    "Variable": ""
                },
                {
                    "type": "TextView",
                    "show_by_condition": "",
                    "Value": "@string2",
                    "NoRefresh": False,
                    "document_type": "",
                    "mask": "",
                    "Variable": ""
                },
                {
                    "type": "TextView",
                    "show_by_condition": "",
                    "Value": "@string3",
                    "NoRefresh": False,
                    "document_type": "",
                    "mask": "",
                    "Variable": ""
                },
                {
                    "type": "Button",
                    "show_by_condition": "",
                    "Value": "#f290",
                    "TextColor": "#DB7093",
                    "Variable": "btn_tst1",
                    "NoRefresh": False,
                    "document_type": "",
                    "mask": ""
                    
                },
                {
                    "type": "Button",
                    "show_by_condition": "",
                    "Value": "#f469",
                    "TextColor": "#DB7093",
                    "Variable": "btn_tst2",
                    "NoRefresh": False,
                    "document_type": "",
                    "mask": ""
                    
                }
                ]
                },
                {
                "type": "TextView",
                "show_by_condition": "",
                "Value": "@val",
                "NoRefresh": False,
                "document_type": "",
                "mask": "",
                "Variable": "",
                "TextSize": "10",
                "TextColor": "#DB7093",
                "TextBold": True,
                "TextItalic": False,
                "BackgroundColor": "",
                "width": "match_parent",
                "height": "wrap_content",
                "weight": 2
                },
               {
                "type": "PopupMenuButton",
                "show_by_condition": "",
                "Value": "Удалить;Проверить",
                "NoRefresh": False,
                "document_type": "",
                "mask": "",
                "Variable": "menu_delete"
                
                }
                ]
            },
            {
                "type": "TextView",
                "show_by_condition": "",
                "Value": "@descr",
                "NoRefresh": False,
                "document_type": "",
                "mask": "",
                "Variable": "",
                "TextSize": "-1",
                "TextColor": "#6F9393",
                "TextBold": False,
                "TextItalic": True,
                "BackgroundColor": "",
                "width": "wrap_content",
                "height": "wrap_content",
                "weight": 0
            }
            ]
        }

    }
    }
   
    j["customcards"]["cardsdata"]=[]
    for i in range(0,5):
      c =  {
        "key": str(i),       
        "descr": "Pos. "+str(i),
        "val": str(random.randint(10, 10000))+" руб.",
        "string1": "Материнская плата ASUS ROG MAXIMUS Z690 APEX",
        "string2": "Гнездо процессора LGA 1700",
        "string3": "Частотная спецификация памяти 4800 МГц"
      }
      
      j["customcards"]["cardsdata"].append(c)

    #if not hashMap.containsKey("cards"):
    
    hashMap.put("cards",json.dumps(j,ensure_ascii=False).encode('utf8').decode())
    
    return hashMap

def fun11(hashMap,_files=None,_data=None):

  hashMap.put("toast","Создали чек ККМ")

  return hashMap

def fun_cards(hashMap,_files=None,_data=None):

  j = { "customcards":         {
          "options":{
            "search_enabled":True,
            "save_position":True
          },

          "layout": {
          "type": "LinearLayout",
          "orientation": "vertical",
          "height": "match_parent",
          "width": "match_parent",
          "weight": "0",
          "Elements": [
          {
              "type": "LinearLayout",
              "orientation": "horizontal",
              "height": "wrap_content",
              "width": "match_parent",
              "weight": "0",
              "Elements": [
              {
              "type": "Picture",
              "show_by_condition": "",
              "Value": "@pic1",
              "NoRefresh": False,
              "document_type": "",
              "mask": "",
              "Variable": "",
              "TextSize": "16",
              "TextColor": "#DB7093",
              "TextBold": True,
              "TextItalic": False,
              "BackgroundColor": "",
              "width": "match_parent",
              "height": "wrap_content",
              "weight": 2
              },
              {
              "type": "LinearLayout",
              "orientation": "vertical",
              "height": "wrap_content",
              "width": "match_parent",
              "weight": "1",
              "Elements": [
              {
                  "type": "TextView",
                  "show_by_condition": "",
                  "Value": "@string1",
                  "NoRefresh": False,
                  "document_type": "",
                  "mask": "",
                  "Variable": ""
              },
              {
                  "type": "TextView",
                  "show_by_condition": "",
                  "Value": "@string2",
                  "NoRefresh": False,
                  "document_type": "",
                  "mask": "",
                  "Variable": ""
              },
              {
                  "type": "TextView",
                  "show_by_condition": "",
                  "Value": "@string3",
                  "NoRefresh": False,
                  "document_type": "",
                  "mask": "",
                  "Variable": ""
              }
              ]
              },
              {
              "type": "TextView",
              "show_by_condition": "",
              "Value": "@val",
              "NoRefresh": False,
              "document_type": "",
              "mask": "",
              "Variable": "",
              "TextSize": "16",
              "TextColor": "#DB7093",
              "TextBold": True,
              "TextItalic": False,
              "BackgroundColor": "",
              "width": "match_parent",
              "height": "wrap_content",
              "weight": 2
              }
              ]
          },
          {
              "type": "TextView",
              "show_by_condition": "",
              "Value": "@descr",
              "NoRefresh": False,
              "document_type": "",
              "mask": "",
              "Variable": "",
              "TextSize": "-1",
              "TextColor": "#6F9393",
              "TextBold": False,
              "TextItalic": True,
              "BackgroundColor": "",
              "width": "wrap_content",
              "height": "wrap_content",
              "weight": 0
          }
          ]
      }

  }
  }
  #  "val": str(random.randint(10, 10000))+" руб.",

  j["customcards"]["cardsdata"]=[]
  for i in range(0,2):
    c =  {
    "key": str(i),
    "descr": "Pos. "+str(i),
    "val": "1 234 руб.",
    "string1": "Материнская плата ASUS ROG MAXIMUS Z690 APEX",
    "string2": "Гнездо процессора LGA 1700",
    "string3": "Частотная спецификация памяти 4800 МГц"
    }
    j["customcards"]["cardsdata"].append(c)

  hashMap.put("cards",json.dumps(j,ensure_ascii=False).encode('utf8').decode())

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

def choice_user(hashMap,_files=None,_data=None):

  hashMap.put("ShowScreen","Чек ККМ")

  return hashMap
