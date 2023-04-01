from models.turn import Turn
from models.game import Game
from models.player import Player

import uuid
from datetime import datetime
import random

class Tournament:
    def __init__(
            self,
            name: str,
            place: str,
            startDate: datetime.date,
            endDate: datetime.date,
            all_turns: list[Turn],
            registeredPlayers: list[Player],
            description: str,
            number_of_turns=4,
            actual_turn=1
    ):
        self.ID = uuid.uuid1()
        self.name = name
        self.place = place
        self.startDate = startDate.today()
        self.endDate = endDate
        self.actualTurn = actual_turn
        self.all_turns = all_turns
        self.registeredPlayers = registeredPlayers
        self.description = description
        self.number_of_turns = number_of_turns
        self.actual_turn = actual_turn

    def register_new_player(self, player: Player):
        for registeredPlayer in self.registeredPlayers:
            if player.national_chess_ID == registeredPlayer.national_chess_ID:
                print("This player has been already registered")
                return
        self.registeredPlayers.append(player)

    def blend_players_first_turn(self):
        blended_players = self.registeredPlayers
        random.shuffle(blended_players)
        return blended_players

    def sort_players_by_score(self):
        sorted_players = self.registeredPlayers
        sorted_players.sort(key=Player.display_score, reverse=False)
        return sorted_players

    def update_players_by_game(self, game: Game):
        self.update_player_score_by_id(game.playerOneInfo.national_chess_ID, game.playerOneInfo.score)
        self.update_player_has_played(game.playerTwoInfo.national_chess_ID, game.playerOneInfo)
        self.update_player_score_by_id(game.playerTwoInfo.national_chess_ID, game.playerTwoInfo.score)
        self.update_player_has_played(game.playerOneInfo.national_chess_ID, game.playerTwoInfo)

    def update_player_score_by_id(self, nationalChessID: str, new_score: int):
        player = self.find_player(nationalChessID)
        player.score = new_score
        print("we didn't find a player with this national chess ID in this tournaments")
        return

    def update_player_has_played(self, nationalChessID: str, player: Player):
        opponent = self.find_player(nationalChessID)
        player.has_played_with.append(opponent.national_chess_ID)

    def find_player(self, nationalChessID: str):
        for player in self.registeredPlayers:
            if player.national_chess_ID == nationalChessID:
                return player
        print("we didn't find a player with this national chess ID in this tournaments")
        return

    def create_games(self, players: list[Player]):
        all_games = list[Game]
        for i in range(0, len(players), 2):
            game = players[i:i+2]
            all_games.append(game)
        return all_games

    def create_turn(self):
        players = list[Player]
        if self.actualTurn == 1:
            players = self.blend_players_first_turn()
        else:
            players = self.sort_players_by_score()
        turn_name = "round " + str(self.actualTurn)
        start_date = datetime.today()
        start_hour = datetime.time().strftime("%H:%M:%S")
        self.check_players_opponents(players)
        all_games = self.create_games(players)
        turn = Turn(turn_name, players, len(all_games), all_games, start_date, start_hour)
        self.all_turns.append(turn)
        return turn

    def check_players_opponents(self, players: list[Player]):
        if self.actualTurn == 1:
            print("it's the first turn, we don't need to check who played against who")
            return
        for i in range(0, len(players), 2):
            if i == (len(players)-2):
                break
            if self.find_player_opponent(players[i], players[i+1].national_chess_ID):
                players[i+1], players[i+2] = players[i+2], players[i+1]
        return players

    def find_player_opponent(self, player: Player, national_chess_id: str):
        print("player {} nationalchess {}".format(player.national_chess_ID, player.has_played_with))
        for opponent_chess_id in player.has_played_with:
            if opponent_chess_id == national_chess_id:
                return True
        return False

    def update_actual_turn(self):
        if self.actualTurn == self.number_of_turns:
            print("it was the last turn of the tournaments")
            return
        self.actualTurn += 1

    def end_turn(self, turn: Turn):
        turn.end_turn()
        for game in turn.all_games:
            self.update_players_by_game(game)
        self.update_actual_turn()

    def post(self):
        pass

    def get(self, tournamentID):
        pass

    def put(self, tournamentID):
        pass
