class Player:
    VERSION = "NO FOLDS LOL"

    def betRequest(self, game_state):
        player_index = game_state['in_action']
        hole_cards = game_state['players'][player_index]['hole_cards']
        ranks = [c['rank'] for c in hole_cards]

        if includes_high_symbol(ranks) or is_pair(hole_cards):
            print '##### hole hand A'
            return 1000
        return 100

    def showdown(self, game_state):
        pass

def is_pair(hole_cards):
    return hole_cards[0]["rank"] == hole_cards[1]["rank"]


def includes_symbol(ranks):
    symbols = ['A', 'K', 'Q', 'J']
    return any(r in symbols for r in ranks)


def includes_high_symbol(ranks):
    symbols = ['A', 'K']
    return any(r in symbols for r in ranks)


def get_call_value(game_state):
    player_index = game_state['in_action']
    return game_state['current_buy_in'] - game_state['players'][player_index]['bet']


def get_minimum_raise_value(game_state):
    player_index = game_state['in_action']
    return game_state['current_buy_in'] - game_state['players'][player_index]['bet'] + game_state['minimum_raise']

