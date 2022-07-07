class Bill:
    """
    Object that contains data about the bill like
    the total amount and the period of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Object that contains the details of the flatmate like
    his/her name, the days he/she stayed in the house and
    generate the shared amount he/she has to pay
    """

    def __init__(self, name, daysStayed):
        self.name = name
        self.daysStayed = daysStayed

    def pays(self, bill, flatmate2):
        return bill.amount * (self.daysStayed / (self.daysStayed + flatmate2.daysStayed))
