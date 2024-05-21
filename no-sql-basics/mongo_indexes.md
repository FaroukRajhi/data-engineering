Indexes help quickly locate data without looking for it everywhere.
Without indexes you will need to look through all of data.
To find information quickly
Indexes should be created for the most frequent queries.

db.courseEnrollment.find({"courseID": 1547})
db.courseEnrollment.createIndex({"courseID": 1})

Instead of scanning the whole collection, we create an index on the field 'courseID' in the course in the courseEnrollment collection.

{"courseID": 1}: means store the index in ascending order

# Use index to sort

Indexes can help with sorting
db.courseEnrollment.find({"courseID": 1547}.sort({"studentId": 1}))
db.courseEnrollment.createIndex({"courseID": 1, "studentId": 1})

# Indexes in MongoDB

MongoDB indexes are special data structures
They store the fields you are indexing and the location of the document
MongoDB stores indexes in a tree form: a balanced tree

![image](./mongo_index.png)


