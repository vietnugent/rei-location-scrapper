import requests
from bs4 import BeautifulSoup
import re
import json

latlng_regex = re.compile('([-+]?([1-8]?\d(\.\d+)?|90(\.0+)?)),(\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?))')


def fetch_html():
    result = requests.get("https://www.rei.com/map/store#letter-link-directory")
    if result.status_code != 200:
        return None

    soup = BeautifulSoup(result.content, 'html.parser')
    stores = soup.find_all(attrs={'data-ui':'reiStore'})

    geojson_features = []

    for store in stores:
        name = store.find(attrs={'data-ui':'storeName'}).contents[0]
        gmap_url = store.find(attrs={'data-ui':'link-store-map'}).attrs['href']
        latlng = re.search(latlng_regex, gmap_url)
        if latlng is not None:
            geojson_features.append(_make_geojson_feature(
                latlng=[float(latlng.group(5)), float(latlng.group(1))],
                properties={"name": name}))

    fc = _make_geojson_featurecollection(geojson_features)
    print(json.dumps(fc))


def _make_geojson_feature(**kwargs):
    return {
        "goemetry": {
            "type": "POINT",
            "coordinates": kwargs['latlng']
        },
        "properties": kwargs['properties']
    }

def _make_geojson_featurecollection(features_array):
    return {
        "type": "FEATURECOLLECTION",
        "features": features_array
    }


if __name__ == '__main__':
    html = fetch_html()
    #print(html)