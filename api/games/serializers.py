from rest_framework.reverse import reverse
from rest_framework.serializers import Field

from core.models import Game
from core.serializers import MasonItemSerializer
from games.tictactoe import str_to_arrays


class GameCreateSerializer(MasonItemSerializer):

    def create_controls(self, instance, request):
        return {
            'self': {
                'href': reverse(
                    'games:game-detail', request=request, args=(instance.id,)
                )
            }
        }

    class Meta:
        model = Game
        fields = ('rule',)


class GameListSerializer(MasonItemSerializer):

    def create_controls(self, instance, request):
        return {
            'self': {
                'href': reverse(
                    'games:game-detail', request=request, args=(instance.id,)
                )
            }
        }

    class Meta:
        model = Game
        fields = ('player1', 'rule')


class BoardSerializer(Field):
    """Serialize string board to a list of lists, because clients would do it
    anyway. Ease the pain.
    """

    def to_internal_value(self, data):
        """This is a read-only serializer."""
        pass

    def get_attribute(self, instance):
        """Override parent method to have access to multiple parent instance fields
        instead of instance.board.
        """
        return instance

    def to_representation(self, instance):
        return str_to_arrays(instance.rule, instance.board)


class GameDetailSerializer(MasonItemSerializer):

    board = BoardSerializer(read_only=True)

    def create_controls(self, instance, request):
        self_href = reverse('games:game-detail', request=request, args=(instance.id,))
        controls = {
            'self': {
                'href': self_href
            }
        }
        if request.user != instance.player1 and not instance.player2:
            controls.update(
                **{
                    'join': {
                        'href': reverse(
                            'games:game-join', request=request,
                            args=(instance.id,)
                        ),
                        'method': 'PUT'
                    }
                }
            )
        if instance.player2:
            player_num = [instance.player1, instance.player2].index(request.user) + 1
            if instance.turn == player_num:
                controls.update(
                    **{
                        'add-move': {
                            'href': reverse('games:game-add-move', args=(instance.id,)),
                            'method': 'PUT',
                            'schema': {
                                'type': 'object',
                                'properties': {
                                    'row': 'number',
                                    'column': 'number'
                                }
                            }
                        }
                    }
                )
        return controls

    class Meta:
        model = Game
        fields = ('board', 'turn', 'winner', 'player1', 'player2', 'rule')
