distance_mi = 5
is_raining = False
has_bike = False
has_car = True
has_ride_share_app = True

if not distance_mi:
    print(False)

elif distance_mi <= 1 and not is_raining:
        print(True)

elif distance_mi >1 and  distance_mi <= 6 and has_bike == True and not is_raining:
    print(True)

elif distance_mi > 6 and (has_car == True or has_ride_share_app == True):
    print(True)
else:
    print(False)