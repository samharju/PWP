from rest_framework.serializers import ModelSerializer


class MasonItemSerializer(ModelSerializer):

    def create_controls(self, instance, request):
        raise NotImplementedError("Override create_controls")  # pragma: no cover

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['@controls'] = self.create_controls(instance, self.context['request'])
        return data
