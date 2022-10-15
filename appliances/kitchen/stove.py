from appliances.appliance import Appliance
class Stove(Appliance):

    def __init__(self, color, heat_method="electric"):
        super().__init__(color, heat_method)

    def make_coffee(self):
        print("gurgle, gurgle. Ding. Your drug of choice is piping hot and ready!")
