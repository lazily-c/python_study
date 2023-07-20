dict2 = {"current": 1,
         "limit": 20,
         "count": 449685,
         "list": [
             {"id": 1423085, "prodName": "大白菜", "prodCatid": 1181, "prodCat": "蔬菜"},
             {"id": 1423084, "prodName": "娃娃菜", "prodCatid": 1182, "prodCat": "蔬菜"},
             {"id": 1423083, "prodName": "小白菜", "prodCatid": 1183, "prodCat": "蔬菜"},
             {"id": 1423082, "prodName": "圆白菜", "prodCatid": 1184, "prodCat": "水果"},
             {"id": 1423081, "prodName": "圆白菜", "prodCatid": 1185, "prodCat": "蔬菜"},
             {"id": 1423080, "prodName": "紫甘蓝", "prodCatid": 1186, "prodCat": "谷物"},
             {"id": 1423079, "prodName": "芹菜", "prodCatid": 1187, "prodCat": "水果"},
             {"id": 1423078, "prodName": "西芹", "prodCatid": 1188, "prodCat": "蔬菜"},
             {"id": 1423077, "prodName": "菠菜", "prodCatid": 1189, "prodCat": "谷物"},
         ]
        }

# 提取出id，prodName，prodCatid，prodCat的值
value = dict2["list"]
for i in value:
    print(i['id'], end=" ")
    print(i['prodName'], end=" ")
    print(i['prodCatid'], end=" ")
    print(i['prodCat'])
