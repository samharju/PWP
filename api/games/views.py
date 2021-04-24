from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.viewsets import ModelViewSet

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


class GameViewSet(ModelViewSet):

    queryset = Game.objects.all()

    def get_queryset(self):
        if self.action == 'list':
            return Game.objects.filter(player2=None)
        return self.queryset

    @action(detail=True, methods=['put'], url_name='join')
    def join(self, request, pk=None):
        game = self.get_object()
        if request.user in [game.player1, game.player2]:
            return Response(
                {'detail': 'You are already in this game'},
                status=status.HTTP_400_BAD_REQUEST
            )
        if game.player2:
            return Response(
                {'detail': 'Can\'t join full game'},
                status=status.HTTP_400_BAD_REQUEST
            )
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

    @action(detail=True, methods=['put'], url_name='add-move', url_path='add-move')
    def add_move(self, request, pk=None):
        game = self.get_object()
        board = str_to_arrays(game.rule, game.board)
        players = [game.player1, game.player2]
        marker = 'XO'[players.index(request.user)]
        row = request.data.get('row')
        col = request.data.get('column')

        error_msg = {
            '@controls': {
                'up': {
                    'description': "Main menu",
                    'href': reverse(
                        'games:game-detail', request=request, args=(pk,)
                    )
                }
            }
        }
        if not all([row, col]):
            error_msg['detail'] = 'Row and column are required values'
            return Response(error_msg, status=status.HTTP_400_BAD_REQUEST)

        move = Move(int(row), int(col), marker)
        ok, error = add_move_if_ok(board, move)
        if not ok:
            error_msg['detail'] = error
            return Response(error_msg, status=status.HTTP_400_BAD_REQUEST)

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
