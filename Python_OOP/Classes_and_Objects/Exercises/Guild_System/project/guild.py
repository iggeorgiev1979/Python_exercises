# from Classes_and_Objects.Exercises.Guild_System.project.player import Player
from project.player import Player

class Guild:
    def __init__(self, name: str, ):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == "Unaffiliated":
            player.guild = self.name
            self.players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str):
        for pl in self.players:
            if pl.name == player_name:
                pl.guild = "Unaffiliated"
                self.players.remove(pl)
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        tmp_list = [f"Guild: {self.name}"]
        for el in self.players:
            tmp_list.append(el.player_info())
        return "\n".join(tmp_list)


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())

