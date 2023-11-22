import ckan.plugins as p
from flask import Blueprint


def odata(uri):
    data_dict = {'uri': uri}
    action = p.toolkit.get_action('ckanext-odata_odata')
    result = action({}, data_dict)
    return result


datastore_odata = Blueprint('datastore_odata', __name__)

datastore_odata.add_url_rule('/datastore/odata3.0/<path:uri>', view_func=odata)
