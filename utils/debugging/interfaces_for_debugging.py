from src.content import EpicGamesGiveaways


class EpicGamesGiveawaysForDebugging(EpicGamesGiveaways):
    # providing interface to encapsulated attributes
    @property
    def server_response(self):
        return self.response
