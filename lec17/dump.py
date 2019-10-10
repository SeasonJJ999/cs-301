import csv,sys

# copied from https://automatetheboringstuff.com/chapter14/
def process_csv(filename):
    exampleFile = open(filename, encoding="utf-8")
    exampleReader = csv.reader(exampleFile)
    exampleData = list(exampleReader)
    return exampleData


rows = process_csv(sys.argv[1])
header = rows[0]
print(header)

print("We are searching for '", sys.argv[2],"'.")
col = header.index(sys.argv[2])
print("That column is at index", col,".")

year_count = [0]*2100

for row in rows[1:]:
    print(row[0],row[col])
    year = int(row[col])
    year_count[year] += 1

for year in range(len(year_count)):
    count = year_counts[year]
    if count > 0:
        print(year, count)


print("There were", year)
