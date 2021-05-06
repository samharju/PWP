from django.db import transaction
from django.db.models import Q
from rest_framework import status, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.viewsets import GenericViewSet

from api.error_handlers import mason_error
from core.models import Game
from games.serializers import (
    GameCreateSerializer, GameDetailSerializer,
    GameListSerializer,
)
from games.tictactoe import (
    Move, add_move_if_ok, arrays_to_str, is_winning_move,
    str_to_arrays,
)


def update_player_stats(winner, loser):
    winner.wins += 1
    loser.losses += 1
    for user in (winner, loser):
        user.win_percentage = user.wins / (user.wins + user.losses)
        user.save()


class GameViewSet(GenericViewSet,
                  mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  mixins.ListModelMixin):

    queryset = Game.objects.all()

    def get_queryset(self):
        if self.action == 'list':
            if user := self.request.query_params.get('history'):
                queryset = Game.objects.filter(
                    Q(player1=user) | Q(player2=user),
                    ~Q(winner=0)
                )
            else:
                queryset = Game.objects.filter(player2=None) | \
                       Game.objects.filter(
                           Q(winner=0),
                           Q(player1=self.request.user) | Q(player2=self.request.user)
                       )
            return queryset
        return self.queryset

    @action(detail=True, methods=['put'], url_name='join')
    def join(self, request, pk=None):
        game = self.get_object()
        if request.user in [game.player1, game.player2]:
            return mason_error('You are already in this game')
        if game.player2:
            return mason_error('Can\'t join full game')
        game.player2 = request.user
        game.turn = 1
        game.save()
        return Response(
            {
                'detail': 'Successfully joined game',
                '@controls': {
                    'self': {
                        'description': "Current game",
                        'href': reverse(
                            'games:game-detail', request=request, args=(pk,)
                        )
                    }
                }
            },
            status=status.HTTP_200_OK,
        )

    @transaction.atomic
    @action(detail=True, methods=['put'], url_name='add-move', url_path='add-move')
    def add_move(self, request, pk=None):
        game = self.get_object()
        board = str_to_arrays(game.rule, game.board)
        players = [game.player1, game.player2]
        marker = 'XO'[players.index(request.user)]
        row = request.data.get('row')
        col = request.data.get('column')

        if not all([row is not None, col is not None]):
            return mason_error('Row and column are required values')

        move = Move(int(row), int(col), marker)
        ok, error = add_move_if_ok(board, move)
        if not ok:
            return mason_error(error)

        if game.turn == 1:
            game.turn = 2
        elif game.turn == 2:
            game.turn = 1

        if is_winning_move(game.rule, board, move):
            winner = players.index(request.user)
            game.winner = winner + 1
            game.turn = 0
            update_player_stats(players.pop(winner), players.pop())

        game.board = arrays_to_str(board)
        game.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):
        if self.action == 'create':
            return GameCreateSerializer
        elif self.action == 'retrieve':
            return GameDetailSerializer
        return GameListSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = None
        return response

    def perform_create(self, serializer):
        rule = serializer.validated_data['rule']
        empty_board = " " * rule.rows * rule.columns
        serializer.save(player1=self.request.user, board=empty_board)

    def get_success_headers(self, data):
        return {'Location': data['@controls']['self']['href']}

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        response = {
            'items': serializer.data,
            '@controls': {
                'up': {
                    'description': "Main menu",
                    'href': reverse('entrypoint', request=request)
                },
                'create': {
                    'description': "Create game",
                    'href': reverse('games:game-list', request=request),
                    'method': 'POST',
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'rule': {
                                'type': 'string',
                                'description': 'name of rule to be used'
                            }
                        }
                    }
                }
            }
        }
        return Response(response)
