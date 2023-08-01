class MoneyMachine:

    CURRENCY = "R$"

    COIN_VALUES = {
        "moedas de 0,25": 0.25,
        "moedas de 0,10": 0.10,
        "moedas de 0,05": 0.05,
        "moedas de 0,01": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Dinheiro: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Insira suas moedas.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"Quantidade de {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Seu troco é de {self.CURRENCY}{change}.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Desculpe, não há dinheiro suficiente, dinheiro devolvido.")
            self.money_received = 0
            return False

