import logging

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.plugins import PluginImplementations

from interfaces import IExternalIDProvider

log = logging.getLogger(__name__)
external_id_name = 'relation'
id_providers = PluginImplementations(IExternalIDProvider)

class External_IdPlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IDatasetForm)
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    def process_external_id(self, value, context):
        for provider in id_providers:
            if provider.name == value:
                log.info("Call %s external ID provider" % value)
                return provider.get_external_id(context)
        log.info("External ID manually entered, set to %s" % value)
        return value

    def get_id_providers(self):
        # Used to populate the select list
        options = [{'value': provider.name, 'text': provider.get_pretty_name()}
                   for provider in id_providers]
        options.append({'value': 'manual', 'text': 'Manual entry'})
        return options

    def get_helpers(self):
        '''Register the get_id_providers() function above as a template
        helper function.

        '''
        # Template helper function names should begin with the name of the
        # extension they belong to, to avoid clashing with functions from
        # other extensions.
        return {'external_id_plugin_get_id_providers': self.get_id_providers}

    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('fanstatic', 'external_id')

    def _modify_package_schema(self, schema):
        schema.update({
            external_id_name: [toolkit.get_validator('ignore_missing'),
                               self.process_external_id,
                               toolkit.get_converter('convert_to_extras')]
        })
        log.info("Active id providers %s " % list(id_providers))
        return schema

    def create_package_schema(self):
        # let's grab the default schema in our plugin
        schema = super(External_IdPlugin, self).create_package_schema()
        # our custom field
        schema = self._modify_package_schema(schema)
        log.info('Create schema')
        return schema

    def update_package_schema(self):
        schema = super(External_IdPlugin, self).update_package_schema()
        # our custom field
        schema = self._modify_package_schema(schema)
        log.info('Update schema')
        return schema

    def show_package_schema(self):
        schema = super(External_IdPlugin, self).show_package_schema()
        schema.update({
            external_id_name: [
                toolkit.get_converter('convert_from_extras'),
                toolkit.get_validator('ignore_missing') ]
        })

        log.info("Show schema")
        return schema

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []
