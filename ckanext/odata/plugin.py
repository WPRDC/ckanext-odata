import ckan.plugins as p

import ckanext.odata.actions as action

from ckanext.odata.blueprints import datastore_odata


def link(resource_id):
    return '%s%s' % (action.base_url(), resource_id)


class ODataPlugin(p.SingletonPlugin):
    p.implements(p.IConfigurer)
    p.implements(p.IBlueprint)
    p.implements(p.IActions)
    p.implements(p.ITemplateHelpers, inherit=True)

    # IConfigurer
    def update_config(self, config):
        p.toolkit.add_template_directory(config, 'templates')
        p.toolkit.add_resource('resources', 'odata')

    # IBlueprint
    def get_blueprint(self):
        return [datastore_odata]

    # IActions
    def get_actions(self):
        actions = {
            'ckanext-odata_odata': action.odata,
        }
        return actions

    # ITemplateHelpers
    def get_helpers(self):
        return {
            'ckanext_odata_link': link,
        }
