import core.models


class IntegrationDBA:
    def __init__(self):
        pass

    @staticmethod
    def get_path(module=None, name=None):
        filters = {'status': True}

        if module:
            filters['module'] = module

        if name:
            filters['name'] = name

        path = core.models.IntegrationKeys.objects.filter(
            **filters
        ).values_list(
            'path', flat=True
        ).first()

        return path

    @staticmethod
    def get_token(module=None, name=None):
        filters = {'status': True}

        if module:
            filters['module'] = module

        if name:
            filters['name'] = name

        token = core.models.IntegrationKeys.objects.filter(
            **filters
        ).values_list(
            'token', flat=True
        ).first()

        return token

    @staticmethod
    def get_description(module=None, name=None):
        filters = {'status': True}

        if module:
            filters['module'] = module

        if name:
            filters['name'] = name

        description = list(core.models.IntegrationKeys.objects.filter(
            **filters
        ).values_list(
            'description', flat=True
        ))

        return description

