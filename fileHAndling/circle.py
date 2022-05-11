from math import pi
def main():
    file=open("Radius.txt")
    radiusData=file.readlines()
    header=['Radius','Diameter','Circumference','Area']
    file.close()
    result=[]
    for radius in radiusData:
        radius=float(radius)
        diameter=format(2*radius,'.5f')
        circumference=format(2*pi*radius,'.5f')
        area=format(2*pi*(radius**2),'.5f')
        radius=format(radius,'.5f')
        result.append([radius,diameter,circumference,area])
    format_row = "{:>15}" * (len(header) + 1)
    print(format_row.format("", *header))
    for team, row in zip(header, result):
        print(format_row.format("", *row))
main()
