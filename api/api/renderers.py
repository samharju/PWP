from rest_framework.renderers import JSONRenderer


class MasonRenderer(JSONRenderer):
    """Override JSONRenderer to set default mime to vnd.mason+json."""

    media_type = 'application/vnd.mason+json'
