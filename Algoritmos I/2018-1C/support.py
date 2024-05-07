import random

def generate_map(heigth,widht):
    return [
            [
                max (0 ,
                    heigth * widht - random.randrange(
                        abs(heigth//2-h)*abs(widht//2-w),
                        2*(heigth + widht) + (abs(heigth//2-h)*abs(widht//2-w)*5)
                    )
                )for w in range(widht)
            ]
                for h in range(heigth)
    ]

def print_map(map_to_print):
    print("| "*len(map_to_print[0])+"|")
    print("|:--"*len(map_to_print[0])+"|")
    for row in map_to_print:
        for cell in row:
            print("|{0:03}".format(cell),end="")
        print("|")
