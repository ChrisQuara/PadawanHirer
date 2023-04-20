class Question:
    category = None
    weight = 0
    responses = None

    def __init__(self, category, weight, responses):
        self.category = category
        self.weight = weight
        if not isinstance(weight, int): raise RuntimeError('weight must be integer')
        self.responses = responses

    def getScore(self):
        # Da editare
        return self.weight

    def toString(self):
        return "<Category:" + str(self.category) + ", Weight:" + str(self.weight) + ", Responses:" + str(
            self.responses) + ">"
