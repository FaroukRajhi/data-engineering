# Primary key

You can use primary key to uniquely identify every row in a table.
Unique attribute of entity.
For example: the book id of the the book or the employee ID number of a staff member.

- Creating primary key

CREATE TABLE book (book_id INT NOT NULL, ..., PRIMARY KEY (book_id));

- To add primary key

ALTER TABLE book ADD primary key (book_id, ISBN);

# Foreign key

Is a column in a table which contains the same information as the primary key in another table

- Create a foreign key

CREATE TABLE copy( copy_id INT, book_id INT,... CONSTRAINT fk_copy_book FOREIGN KEY(book_id), REFERENCES book(book_id) );