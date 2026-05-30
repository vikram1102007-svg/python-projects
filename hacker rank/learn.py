import csv
with open("sample.txt","w",newline="")as f:
    writer=csv.writer(f)
    writer.writerow(["name","age","city"])
    writer.writerow(["Alice",30,"New York"])
    writer.writerow(["Bob",25,"Los Angeles"])
    
    with open("sample.txt","r")as f:
        reader=csv.reader(f)
        for row in reader:
            print(row)