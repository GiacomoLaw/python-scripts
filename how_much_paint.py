try:
    coats = int(input("How many coats? "))
    height = int(input("Enter height of room: "))
    width = int(input("Enter width of room: "))
    unpaintable = int(input("How much is unpaintable? "))
    paintcover = int(input("How much wall does a litre of paint cover? "))
    
    room = height * width
    realroom = room - unpaintable
    mainsize = realroom * coats

    answer = mainsize/paintcover
    print("The paint required is", answer, "litres")
    
except:
    print("Try again")
