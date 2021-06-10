from geojson import Point, Feature, FeatureCollection, dump

'''
@function: export the gps location [lat, lng, alt] as a geojson file
@param: ps - a list of np.array([lat, lng, alt])
        count - the counter name
@return: 
'''
def export_geojson(ps):

    features = []
    for p in ps:
        point = Point(p[:-1])
        features.append(Feature(geometry=point))

    # add more features...
    # features.append(...)

    feature_collection = FeatureCollection(features)

    with open('data/gps/{}.geojson'.format(int(time.time())), 'w') as f:
        dump(feature_collection, f)