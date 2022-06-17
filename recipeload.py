import typesense

client = typesense.Client({
    'nodes': [{
      'host': 'localhost', # For Typesense Cloud use xxx.a1.typesense.net
      'port': '8108',      # For Typesense Cloud use 443
      'protocol': 'http'   # For Typesense Cloud use https
    }],
    'api_key': 'Hu52dwsas2AdxdE',
    'connection_timeout_seconds': 2
  })



# recipe_schema = {
# 'name': 'recipe1',
# 'fields': [
#   {'name': 'nickname', 'type': 'string' },
#   {'name': 'info', 'type': 'string' },
#   {'name': 'type', 'type': 'string', 'facet': True },
# ]
# }

# client.collections.create(recipe_schema)
# client.collections['recipe1'].delete()
# client.collections.create({
# 'name': 'recipe1',
# 'fields': [
#   {'name': 'name', 'type': 'string', "locale":"zh" },
#   {'name': 'nickname', 'type': 'string', "locale":"zh" },
#   {'name': 'info', 'type': 'auto' , "locale":"zh"},
#   {'name': 'type', 'type': 'string', 'facet': True },
# ]
# })
with open('data/food-table.json',encoding='utf-8') as jsonl_file:
  for i,j in enumerate(jsonl_file):

    print(i,j)
    try:
      client.collections['recipe1'].documents.import_(j.encode("utf-8"))
    except:
      print("error",i,j)


# document = {"_id":{"$oid":"5f9ebd1f13908471f1bc1961"},"name":"香雪酒","url":"http://www.foodwake.com/food/872","info":"能量","nickname":"无","type":"酒类","update_time":1604314204579,"imgUrl":"https://image.shutterstock.com/image-photo/incense-stick-smoke-natural-wood-260nw-1641807787.jpg"}

# build()
res = client.collections['recipe1'].documents.search({
  'q'         : '酒',
  'query_by'  : 'name',
})
hit = res["hits"]
print(hit)




# res = client.collections['recipe'].documents.search(search_parameters)
# hit = res["hits"]
# print(hit)
# client.collections['companies'].documents.search(search_parameters)