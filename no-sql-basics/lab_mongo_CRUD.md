# Insert Documents

db.languages.insert({"name":"java","type":"object oriented"})
db.languages.insert({"name":"python","type":"general purpose"})
db.languages.insert({"name":"scala","type":"functional"})
db.languages.insert({"name":"c","type":"procedural"})
db.languages.insert({"name":"c++","type":"object oriented"})

# Read Documents

Find the count of documents.

1
2
db.languages.count()
Copied!
List the first document in the collection.

1
db.languages.findOne()
Copied!
List all documents in the collection.

1
db.languages.find()
Copied!
List first 3 documents in the collection.

1
db.languages.find().limit(3)
Copied!
Query for “python” language.

1
db.languages.find({"name":"python"})
Copied!
Query for “object oriented” languages.

1
db.languages.find({"type":"object oriented"})
Copied!
List only specific fields.

Using a projection document you can specify what fields we wish to see or skip in the output.

This command lists all the documents with only name field in the output.

1
db.languages.find({},{"name":1})
Copied!
This command lists all the documents without the name field in the output.

1
db.languages.find({},{"name":0})
Copied!
This command lists all the “object oriented” languages with only “name” field in the output.

1
db.languages.find({"type":"object oriented"},{"name":1})


# Update documents

Update documents based on a criteria.

Add a field to all the documents.

The ‘updateMany’ command is used to update documents in a mongodb collection, and it has the following generic syntax.

1
db.collection.updateMany({what documents to find},{$set:{what fields to set}})
Copied!
Here we are adding a field description with value programming language to all the documents.

1
db.languages.updateMany({},{$set:{"description":"programming language"}})
Copied!
Set the creater for python language.

1
db.languages.updateMany({"name":"python"},{$set:{"creator":"Guido van Rossum"}})
Copied!
Set a field named compiled with a value true for all the object oriented languages.

1
db.languages.updateMany({"type":"object oriented"},{$set:{"compiled":true}})

# Delete Document

Delete documents based on a criteria.

Delete the scala language document.

1
db.languages.remove({"name":"scala"})
Copied!
Delete the object oriented languages.

1
db.languages.remove({"type":"object oriented"})
Copied!
Delete all the documents in a collection.

1
db.languages.remove({})


