# Insert Documents

Let us insert a lot of documents into the newly created collection.
This should take around 3 minutes, so please be patient.
The code given below will insert 200000 documents into the ‘bigdata’ collection.
Each document would have a field named account_no which is a simple auto increment number.
And a field named balance which is a randomly generated number, to simulate the bank balance for the account.
Copy the below code and paste it on the mongo client.

1
2
use training
for (i=1;i<=200000;i++){print(i);db.bigdata.insert({"account_no":i,"balance":Math.round(Math.random()*1000000)})}
Copied!
Verify that 200000 documents got inserted by running the below command.

1
db.bigdata.count()

# Measure the time taken by a query

et us run a query and find out how much time it takes to complete.

Let us query for the details of account number 58982.

We will make use of the explain function to find the time taken to run the query in milliseconds.

Run the below command.

1
db.bigdata.find({"account_no":58982}).explain("executionStats").executionStats.executionTimeMillis
Copied!
Make a note of the milliseconds it took to run the query. We will need this at a later stage.


# Working with indexes 

Before you create an index, choose the field you wish to create an index on. It is usually the field that you query most.

Run the below command to create an index on the field account_no.

1
2
    
db.bigdata.createIndex({"account_no":1})
Copied!
Run the below command to get a list of indexes on the ‘bigdata’ collection.

1
db.bigdata.getIndexes()
Copied!
You should see an index named account_no_1

# Delete an Index

db.bigdata.dropIndex({"account_no":1})

