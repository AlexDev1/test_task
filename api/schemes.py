from drf_yasg.generators import OpenAPISchemaGenerator

from settings.settings import DEBUG


class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        if DEBUG:
            schema.schemes = ['http']
        else:
            schema.schemes = ['https']
        return schema
