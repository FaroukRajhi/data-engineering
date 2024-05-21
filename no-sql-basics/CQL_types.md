Welcome to CQL Data Types. Let's talk about the Cassandra
Query Language (or CQL) accepted data types. After watching this video, you will be able to:
Describe the main data types in CQL Explain how to use these data types
when defining a Cassandra table, and understand the role of collection
data types and user-defined data types In the previous videos you have already
been introduced to the syntax for table creation in Cassandra.
Now let's focus a bit on the data types that you will work with when declaring
the Cassandra tables. Data types usually signify the type of variables, such as ‘int’,
‘char’, ‘float’, and others. In CQL there are many data types,
but they can be grouped into three main categories:
Built-in data types Collection data types
and User-Defined data types. The user can choose any of them
according to the requirements of the application and data model. Now let’s discuss each of them
in turn to understand what they mean. The built-in data types are basically
pre-defined in Cassandra. The user can refer the variables to any of them.
Besides regular data types like Ascii, Boolean, Decimal, Double, Float, Int, and Text – which
are fairly straightforward – there are some others that maybe require a bit of explanation.
Let's take the ‘Blob’ data type. Although Cassandra mainly stores text-based information,
there is also the possibility to store blobs, which stands for Binary Large Objects.
Blobs are typically used to store images, audio, or other multimedia objects. While
blobs represent a collection of binary data stored as a single entity, in Cassandra it is recommended
that their size does not exceed 1MB. Thus, you could store a small image or string using a blob.
The ‘Bigint’ data type can be used for a 64-bit signed long integer. This data
type stores a higher range of integers when compared to the ‘int’ data type.
The well-known ‘Varchar’ is also available in Cassandra as a data type.
It represents UTF8 encoded strings. Moving on to more complex data types,
Cassandra provides collection types as a way to group and store data together in a column.
For example, in a relational database, a
grouping such as a user's multiple email addresses is related with a many-to-one joined relationship
between a ‘users’ table and an ‘email’ table. Cassandra avoids joins between two tables by
storing the user's email addresses in a collection column in the ‘users’ table. Each collection
specifies the data type of the data held. A collection is appropriate if the data for
collection storage is limited. If the data has unbounded growth potential,
like messages sent or sensor events registered every second, do not use the collection data type.
Instead, use a table with a compound primary key where data is stored in the clustering columns.
Within the Collection data types category there are three data types:
Lists: This Cassandra data type represents a collection of one or more elements in a table.
List is used in cases where the order of the elements is to be maintained, and a value is to be
stored multiple times, such as entries in a log. Maps: This Cassandra data type represents
a collection of key-value pairs. Map is a data type that is used to store
a key-value pair of elements, such as entries in a journal entered using a date and then text.
and Sets: This Cassandra data type represents a collection of one or more sorted elements
in a table. Set is a data type that is used to store a group of elements. The elements of a set
will be returned in a sorted order. An example would be a list of email addresses.
Let's go back to the ‘users’ table. Let's add a new column to the table, called jobs, which
is basically just a list of jobs. We would like to store the jobs in the order of their occurrences.
Remember that the ‘users’ table is a static table with its primary key
consisting of the ‘userid’ column. In Cassandra we will store all the users’ jobs
in a single column, since we cannot perform joins. In this case we will use the ‘list’ type of the
collection data types because we want to preserve the order of the jobs. Another reason is that a
person can work at a specific company more than once, so uniqueness is not required.
We can add a job in the list: either at the beginning or end of the list
or in a specific position. The entries in the list can be repetitive, as they are not unique.
A select in cqlsh on our table shows that we currently have two jobs recorded for our user.
We can also remove an entry from the list. A select on our table now shows that we
only have one job listed for our user. Besides collection data types there are
other data types that allow for the storing of data together. We have seen that collection data
types can be used instead of a one-to-many join relationship. However, for one-to-one relations
we can use Cassandra User-Defined Types (or UDTs). UDTs can attach multiple data types to a single
column. Think of an address being a combination of an apartment number, building, street,
and so on. CQL enables the user to create their own data type. The fields used in a created UDT
can be any valid data type, including collections and other existing UDTs.
After creating a data type and fields in it, the user can alter, verify,
and even drop a field or the whole data type. Once created, UDTs can be used to define a
column in a table. Let's see how we do this on the next screen.
In this example, we create a new data type called ‘address’.
Once created, we can use it to define a column in our new table called ‘Location’.
We can insert data using the new ‘address’ data type,
and we can also drop the data type. In this video, you have learned that:
Cassandra supports built-in, collection, and user-defined data types
Both collection and user-defined data types offer a way to group and store data together
Collection data types can emulate one-to-many relationships
There are three types of collection data types: lists, maps, and sets
User-defined data types can emulate one-to-one relationships
User-defined data types can attach multiple data fields to a column