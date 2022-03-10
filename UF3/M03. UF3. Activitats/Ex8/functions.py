import csv
def get_info():
    line_count = 0
    total_price = 0
    with open('projects_board.csv') as csvfile:
        readCSV = csv.DictReader(csvfile)
        for row in readCSV:
            total_price += int(row['preu'])
            line_count += 1
    print(f"El document conté {line_count} projectes i l'empresa facturara un total de {total_price} €")