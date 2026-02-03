F3 = ["f3", "renault megane", 218, (198, 270), 8400, 5.9, 1995, 4]
F2 = ["f2", "vw off-road-bug", 185, (104, 142), 6000, 9, 1880, 4]
G3 = ["G3", "mitsubishi pajero", 285, (153, 208), 7000, 9.6, 3497, 6]
A4 = ["A4", "suzuki ignis", 180, (153, 206), 7250, 8, 1597, 4]
G1 = ["G1", "citroen visa 4x4", 190, (74, 100), 7680, 9, 1566, 4]
C3 = ["C3", "VW-polo GTI", 185, (96, 103), 7600, 8, 1600, 4]
E2 = ["E2", "ford escort WRC", 220, (220, 299), 6250, 5.6, 1993, 4]
B3 = ["B3", "toyota corolla WRC", 210, (220, 299), 5700, 5.4, 1927, 4]
B1 = ["B1", "Seat Cordoba WRC", 230, (221, 300), 6000, 5, 1998, 4]
C2 = ["C2", "Opel Astra GSi", 235, (235, 320), 6200, 5.6, 3962, 6]
cars = [F3, F2, G3, A4, G1, C3, E2, B3, B1, C2]

def display(car):
    print(" -----------------------------------")
    print(f"|    {car[0]}     {car[1]}        |")
    print(f"|                                 |")
    print(f"|        -------------------      |")
    print(f"|        |                  |     |")
    print(f"|        |                  |     |")
    print(f"|        |                  |     |")
    print(f"|        |                  |     |")
    print(f"|        --------------------     |")
    print(f"|       max speed    0-60         |")
    print(f"|       {car[2]}              {car[5]}      |")
    print(f"|                                 |")
    print(f"|       HP           CC           |")
    print(f"|       {car[3]}      {car[6]}      |")
    print(f"|                                 |")
    print(f"|       RPM          cylinders    |")
    print(f"|       {car[4]}               {car[7]}      |")
    print(f"|                                 |")
    print(" -----------------------------------")


while True:
    i = 1
    for c in cars:
        print(i, c[1])
        i +=1
    car_num = int(input("Select a car by number: "))
    display(cars[car_num - 1])
