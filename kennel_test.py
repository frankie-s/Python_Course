from mammals import Cat, Dog, Kennel
 
#d1 = Dog('Spot','mutt',2)
#d2 = Dog('Fred','Leonberger',4)
#d3 = Dog('Rebel','Pomerian', 3)
k1 = Kennel("Chris' Kennel", 'Mercedes')
k1._dogs.append(Dog('Spot','mutt',2))
k1._dogs.append(Dog('Fred','Leonberger',4))
k1._dogs.append(Dog('Rebel','Pomerian', 3))
for dog in k1._dogs:
    print(dog)
print("Now let's get rid of Dog 2")
del(k1._dogs[1])
for dog in k1._dogs:
    print(dog)
