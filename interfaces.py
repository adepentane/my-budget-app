class InsurancePolicy:
    def __init__(self, price_of_item):
        self.price_of_insured_item = price_of_item


class VehicleInsurance(InsurancePolicy):
    def __init__(self, price_of_item):
        super().__init__(price_of_item)
        self.price_of_insured_items = None

    def get_rate(self):
        return self.price_of_insured_items * .001


class HomeInsurance(InsurancePolicy):
    def get_rate(self):
        return self.price_of_insured_item * .00005
