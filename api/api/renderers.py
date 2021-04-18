from rest_framework.renderers import JSONRenderer


class MasonRenderer(JSONRenderer):

    media_type = 'application/vnd.mason+json'
