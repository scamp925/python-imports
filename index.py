# from appliances.kitchen.utility.dishwasher import Dishwasher
# from appliances.laundry.dryer import Dryer
# from appliances.laundry.washer import Washer
# from appliances.kitchen.utility.refrigerator import Refrigerator
# from appliances.kitchen.coffeemaker import CoffeeMaker
# from appliances.kitchen.can_opener import CanOpener
from appliances import (
  Dishwasher,
  Washer,
  Dryer,
  Refrigerator,
  CoffeeMaker,
  CanOpener,
)

whirlpool_dishwasher = Dishwasher("black")
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red", "electric")
samsung_dryer = Dryer("red", "gas")

lg_fridge = Refrigerator("stainless")
lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white")
mr_coffee.make_coffee()

kitchen_aid_can_opener = CanOpener("red")
kitchen_aid_can_opener.open_can()
