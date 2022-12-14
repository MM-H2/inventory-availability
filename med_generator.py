# med_generator 
# ID QUANTITY TRANSACTION_TYPE TRANSACTION_DATE
import random
import datetime

COUNT_OF_TRANSACTIONS = 1000000
END_DATETIME = datetime.datetime.now()
START_DATETIME = END_DATETIME - datetime.timedelta(days=30)
COUNT_OF_MEDS = 10000

# generate medcine IDs
medicine_id_list = []
for i in range(COUNT_OF_MEDS):
    medicine_id_list.append(i)

print("medicine_id_list generated")

# select IDs for transactions
IDs = []
for i in range(COUNT_OF_TRANSACTIONS):
    IDs.append(random.choice(medicine_id_list))

print("IDs selected")

# generate random QUANTITYs for transactions
QUANTITY = []
for i in range(COUNT_OF_TRANSACTIONS):
    QUANTITY.append(round(random.uniform(1,100),2))

print("QUANTITYs generated")

# generate random TRANSACTION_TYPE for transactions
TRANSACTION_TYPE = []
for i in range(COUNT_OF_TRANSACTIONS):
    TRANSACTION_TYPE.append(random.choice(["BUY", "SELL"]))

print("TRANSACTION_TYPEs generated")

# generate random TRANSACTION_DATE for transactions
TRANSACTION_DATE = []
for i in range(COUNT_OF_TRANSACTIONS):
    TRANSACTION_DATE.append((START_DATETIME + (END_DATETIME - START_DATETIME) * random.random()).replace(microsecond=0))

print("TRANSACTION_DATEs generated")

with open("med_transactions.csv", "w") as f:
    # f.write("ID,QUANTITY,TRANSACTION_TYPE,TRANSACTION_DATETIME\n")
    for i in range(COUNT_OF_TRANSACTIONS):
        f.write(f"{IDs[i]}, {QUANTITY[i]}, {TRANSACTION_TYPE[i]}, {TRANSACTION_DATE[i]}\n")
