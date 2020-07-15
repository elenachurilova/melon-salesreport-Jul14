"""Generate sales report showing total melons each salesperson sold."""
import sys

path = sys.argv[1]

def print_sales_report(filename):
    """Generate dictionary and print sales report

    Take in txt file name as an argument
    """

    file = open(path)

    sales_data = {}

    for line in file:

        line = line.rstrip()
        sales = line.split("|")
        salesperson = sales[0]
        usd = float(sales[1])
        melons = int(sales[2])

        if salesperson in sales_data:

            sales_data[salesperson][0] += usd
            sales_data[salesperson][0] = round(sales_data[salesperson][0],2)
            sales_data[salesperson][1] += melons

        else:

            sales_data[salesperson] = [usd,melons]


    for key, value in sales_data.items():
        print(f"\n{key.upper()}")
        print(f"${value[0]}\n{value[1]} melons")
