from ckan.plugins.interfaces import Interface

class IExternalIDProvider(Interface):
    '''
    External ID Provider
    '''

    def get_external_id(self, pkg):
        '''
        External ID Providers must implement this method, which will
        return an external ID for this resource

        :param pkg: The package being referenced
        :return: A string
        '''

    def get_pretty_name(self):
        '''
        External ID Providers must implement this method, which will
        return a human readable name for this resource

        :return: A string
        '''