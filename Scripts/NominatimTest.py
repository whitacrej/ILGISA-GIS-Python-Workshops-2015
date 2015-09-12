# Script to test that Nominatim was installed correctly

# This script should be run using a 32 bit IDE


from nominatim import Nominatim, NominatimReverse

nom = Nominatim()

print nom.query('Urbana, IL')


# You should get an output that looks like below, only longer. Only the first record is shown below

# {u'display_name': u'Urbana, Champaign County, Illinois, United States of America', u'importance': 0.72235913166643, u'place_id': u'151154892', u'lon': u'-88.207301', u'lat': u'40.1117174', u'osm_type': u'relation', u'licence': u'Data \xa9 OpenStreetMap contributors, ODbL 1.0. http://www.openstreetmap.org/copyright', u'osm_id': u'126133', u'boundingbox': [u'40.0728246', u'40.157395', u'-88.2330399', u'-88.1530562'], u'type': u'city', u'class': u'place', u'icon': u'http://64.12.173.17:8000/nominatim/v1/images/mapicons/poi_place_city.p.20.png'},...