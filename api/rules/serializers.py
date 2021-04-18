from rest_framework.reverse import reverse

from core.serializers import MasonItemSerializer
from core.models import Rule


class RuleDetailSerializer(MasonItemSerializer):

    def create_controls(self, instance, request):
        href_self = reverse(
            'rules:rule-detail', request=request, args=(instance.name,)
        )
        data = {
            'self': {
                'href': href_self
            },
            'collection': {
                'href': reverse('rules:rule-list', request=request)
            },
            'author': {
                'href': reverse('users:user-detail', request=request,
                                args=(instance.author.username,))
            }
        }
        if instance.author == request.user:
            data.update(
                delete={
                    'href': href_self,
                    'method': 'DELETE'
                }
            )
        return data

    class Meta:
        model = Rule
        fields = ('name', 'rows', 'columns', 'winning_tick_count', 'author')
        read_only_fields = ('author', )


class RuleListSerializer(MasonItemSerializer):

    def create_controls(self, instance, request):
        return {
            'self': {
                'href': reverse(
                    'rules:rule-detail', request=request, args=(instance.name,)
                )
            }
        }

    class Meta:
        model = Rule
        fields = ('name', 'rows', 'columns', 'winning_tick_count', 'author')
        read_only_fields = ('author', )
