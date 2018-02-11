# Description
Get all REI locations (latitude, longitude) by parsing rei.com

Geojson data files:
- Human-readable [rei_formatted.geojson](rei_formmatted.geojson)
- Raw[rei.geojson](rei.geojson)

# How to run (python3 required)

```
git clone https://github.com/vietnugent/rei-location-scrapper.git
cd rei-location-scrapper
virtualenv venv
source ./venv/bin/activate
pip3 install -r requirements.txt
python3 rei.py
```

# License
Apache 2
