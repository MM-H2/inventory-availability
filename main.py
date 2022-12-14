# main file with the main function

if __name__ == "__main__":
    from datetime import datetime
    import csv
    import random
    import inventory
    strating_stock = 0

    # read data from csv file
    data = csv.reader(open('med_transactions.csv','r'))

    # cut the header
    data = [i for i in data][1:]

    # sort data by date
    data = sorted(data, key = lambda row: datetime.strptime(row[3].strip(), "%Y-%m-%d %H:%M:%S"))


    def init_dict_of_medcinies() -> dict[str:inventory.Medicine]:
        # create a dictionary of medicines objects with random starting stock
        dict_of_medicines = {}
        for i in data:
            dict_of_medicines[i[0]] = inventory.Medicine(id=i[0], quantity=round(random.uniform(0, 100),2)) 
        return dict_of_medicines

    def output_day_inventory(dict_of_medicines:dict[str:inventory.Medicine], date:datetime.date) -> None:
        # output the inventory for each day
        for i in dict_of_medicines:
            with open("output.csv", "a") as f:
                f.write(f"{i},{dict_of_medicines[i].quantity},{date}\n")

    def process_transaction(dict_of_medicines:dict[str:inventory.Medicine], data:list[list[str]]) -> None:

        # write the header to the output file
        with open("output.csv", "a") as f:
            f.write("ID,QUANTITY,DATE\n")
        
        # set the current date to the first date in the data
        current_date = datetime.strptime(data[0][3].strip(), "%Y-%m-%d %H:%M:%S").date()


        for row in data:
            # check if the date has changed and output the inventory for the previous day
            if datetime.strptime(row[3].strip(), "%Y-%m-%d %H:%M:%S").date() != current_date:
                output_day_inventory(dict_of_medicines, current_date)
                current_date = datetime.strptime(row[3].strip(), "%Y-%m-%d %H:%M:%S").date()
                print(f"Day {current_date} processed")
            
            # add or remove the quantity from the medicine object
            if row[2] == "BUY":
                dict_of_medicines[row[0]].add(quantity=row[1])
            elif row[2] == "SELL":
                dict_of_medicines[row[0]].remove(quantity=row[1])

    process_transaction(init_dict_of_medcinies(), data)
    
