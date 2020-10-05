import random
import statistics

class NoZeroRoulette():
    def __init__(self):
        self.pockets = list(i for i in range(1,37))
        self.ball = None
        self.odds = len(self.pockets) - 1

    def spin(self):
        self.ball = random.choice(self.pockets)

    def place_bet(self, pocket, amount):
        if pocket == self.ball:
            return self.odds * amount
        else: return -amount

    def __str__(self):
        return f"Non Zero Roulette"
    
class EuropeanRoulette(NoZeroRoulette):
    def __init__(self):
        NoZeroRoulette.__init__(self)
        self.pockets.append(0)
         
    def __str__(self):
        return "European Roulette"
    

class AmericanRoulette(EuropeanRoulette):
    def __init__(self):
        EuropeanRoulette.__init__(self)
        self.pockets.append(0)
    def __str__(self):
        return "American Roulette"


def get_pocket_returns(game, num_spins, pocket, bet_amount):
    bankroll = 0
    for i in range(num_spins):
        game.spin()
        bankroll += game.place_bet(pocket, bet_amount)
    return bankroll/num_spins

def calc_mean_and_std(X):
    return sum(X)/float(len(X)), statistics.stdev(X)

def empirical_rule():
    results = {}
    num_trials = 20
    games = (NoZeroRoulette, EuropeanRoulette, AmericanRoulette)

    for spins in (100, 100000, 1000000):
        print(f"Simulating betting a pocket or 20 trials of {spins} spins each")
        for game in games:

            if game().__str__() not in results:
                results[game().__str__()] = []

            pocket_returns = [get_pocket_returns(game(), spins, 2, 1) for t in range(num_trials)]
            mean, std = calc_mean_and_std(pocket_returns)
            results[game().__str__()].append((spins, 100*mean, 100*std))

            print(f"Exp. return for {game()} = {str(round(100*mean, 3))}%, +/- {str(round(100*1.96*std,3))}% with 95% confidence")
        print("-"*50)
empirical_rule()



