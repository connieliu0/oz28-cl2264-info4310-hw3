import csv
import json

def process_row(row):
    # name = row['name']
    # url = row['url']
    categories = []
    cats = json.loads(row['categories'])
    for c in cats:
        categories.append(c[0])
    # row['location'] = json.loads(row['location'])

    res = {
        'name': row['name'],
        'url': row['url'],
        'review_count': int(row['review_count']),
        'categories': categories,
        'rating': float(row['rating']),
        'location': json.loads(row['location']),
        'latitude': float(row['latitude']),
        'longitude': float(row['longitude']),
        'search_category': row['search category']
    }

    return res

data = []
with open('static/yelp_boston.csv','r') as f:
    reader = csv.DictReader(f)
    header = reader.fieldnames

    for row in reader:
        res = process_row(row)
        data.append(res)

print(len(data))
with open('static/yelp_boston.json','w') as f:
    s_data = json.dump(data, f)
