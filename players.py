import pandas as pd


class PlayerList:

    def __init__(self, player_file):
        self.players = []

        player_df = pd.read_csv(player_file)

        for index, row in player_df.iterrows():
            new_player = f'{row.First}%20{row.Last}'
            self.players.append(new_player)
