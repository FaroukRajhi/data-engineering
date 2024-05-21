# Load sample data into the training database.

use training
db.marks.insert({"name":"Ramesh","subject":"maths","marks":87})
db.marks.insert({"name":"Ramesh","subject":"english","marks":59})
db.marks.insert({"name":"Ramesh","subject":"science","marks":77})
db.marks.insert({"name":"Rav","subject":"maths","marks":62})
db.marks.insert({"name":"Rav","subject":"english","marks":83})
db.marks.insert({"name":"Rav","subject":"science","marks":71})
db.marks.insert({"name":"Alison","subject":"maths","marks":84})
db.marks.insert({"name":"Alison","subject":"english","marks":82})
db.marks.insert({"name":"Alison","subject":"science","marks":86})
db.marks.insert({"name":"Steve","subject":"maths","marks":81})
db.marks.insert({"name":"Steve","subject":"english","marks":89})
db.marks.insert({"name":"Steve","subject":"science","marks":77})
db.marks.insert({"name":"Jan","subject":"english","marks":0,"reason":"absent"})


# Limiting the rows in the output

Using the $limit operator we can limit the number of documents printed in the output.
This command will print only 2 documents from the marks collection.

1
2
use training
db.marks.aggregate([{"$limit":2}])

# Sorting based on column

We can use the $sort operator to sort the output.

This command sorts the documents based on field marks in ascending order.

1
2
db.marks.aggregate([{"$sort":{"marks":1}}])
Copied!
This command sort the documents based on field marks in descending order.

1
2
db.marks.aggregate([{"$sort":{"marks":-1}}])

# Sorting and limiting

Aggregation usually involves using more than one operator.
A pipeline consists of one or more operators declared inside an array.
The operators are comma separated.
Mongodb executes the first operator in the pipeline and sends its output to the next operator.

Let us create a two stage pipeline that answers the question “What are the top 2 marks?”.
db.marks.aggregate([
{"$sort":{"marks":-1}},
{"$limit":2}
])
```	
# Exercise 5 - Group by
The operator $group by, along with operators like $sum, $avg, $min, $max, allows us to perform grouping operations.
This aggregation pipeline prints the average marks across all subjects.
```	
db.marks.aggregate([
{
    "$group":{
        "_id":"$subject",
        "average":{"$avg":"$marks"}
        }
}
])
Copied!
The above query is equivalent to the below sql query.

SELECT subject, average(marks)
FROM marks
GROUP BY subject

# Putting all together

db.marks.aggregate([
{
    "$group":{
        "_id":"$name",
        "average":{"$avg":"$marks"}
        }
},
{
    "$sort":{"average":-1}
},
{
    "$limit":2
}
])

