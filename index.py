from appliances import (
  Dishwasher,
  Washer,
  Dryer,
  Refrigerator,
  CoffeeMaker,
  CanOpener,
  Stove
)

whirlpool_dishwasher = Dishwasher("black")
print(whirlpool_dishwasher)
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red", "electric")
samsung_washer.wash_clothes("super_scrub")

samsung_dryer = Dryer("red", "gas")
samsung_dryer.dry_clothes()

lg_fridge = Refrigerator("stainless")
lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white")
mr_coffee.make_coffee()

kitchen_aid_can_opener = CanOpener("red")
kitchen_aid_can_opener.open_can()

whirlpool_stove = Stove("black")
whirlpool_stove.make_coffee()
