When you select a particular row from a table, the processor must check each row in turn it finds the one that you want.
On a large table, this can be a very slow way of location a row.
You can create an index on  table to easily locate the specified row or set of rows you require.

An index works by sorting pointers to each row in the table so when you request a particular row, the SQL processor can use index to quickly locate the row.
By default, when you create a primary key on a table an index, is automatically created on that key, but you can also create your own indexes on regularly searched columns.

Syntax:

CREATE UNIQUE INDEX unique_book_id ON book(book_id)