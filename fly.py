import InsectClass as i

mosquito = i.Insect(4,8)
housefly = i.Insect(2,4)

mosquito.flight_length()
housefly.flight_length()

print("The moquito can fly up to", mosquito.get_miles(), "miles")
print("The housefly can fly up to", housefly.get_miles(), "miles")
