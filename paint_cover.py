try
    coats = int(input("How many coats? "))
    height = int(input("Enter height of room: "))
    width = int(input("Enter width of room: "))
    length = int(input("Enter the length of room: "))
    unpaintable = int(input("How much is unpaintable? "))
    paintcover = int(input("How much wall does a litre of paint cover? "))
        
    walls_width = height * width * 2
    walls_length = height * length * 2
    walls_gross_total = walls_width + walls_length
    walls_net_total = walls_gross_total - unpaintable
    paint_needed = walls_net_total / paintcover
    paint_needed_coats = paint_needed * coats

    print("The paint required is", paint_needed_coats, "litres")

except
    print("Try again.")
