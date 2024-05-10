Task A: Modify the Database with the CLI
One of the tables in the database schema is aircrafts_data. You can take a look at the contents of that table by executing the following command in the PostgreSQL CLI:

1
SELECT * FROM aircrafts_data;
Copied!
This will show you the aircraft models in the database, their code, and their range in kilometers.

Screenshot showing aircraft models, aircraft codes, and aircraft ranges in database

Suppose a new model of aircraft is being added to the fleet, and you, as the database administrator, are responsible for updating the database to reflect this addition. The aircraft they wish to add is the Airbus A380, which has a range of 15,700 km and aircraft code “380”. You can do this by executing the following command in the PostgreSQL CLI:

1
INSERT INTO aircrafts_data(aircraft_code, model, range) VALUES (380, '{"en": "Airbus A380-800"}', 15700);
Copied!
To confirm that the information was entered into the database correctly, you can read out the aircrafts_data table again using:

1
SELECT * FROM aircrafts_data;
Copied!
The output will look like this:

Screenshot highlighting new entry

As you can see, there is a new entry in the table corresponding to the new aircraft added to the fleet.

Task B: Backup your Database using pgAdmin
Now that you modified the database (minor modification for demonstration - in reality there would likely be far more additions) it is good practice to backup your database in case of accidental deletion.

To back up the demo database, first exit the PostgreSQL CLI by either entering:

1
\q
Copied!
Next, open the pgAdmin Graphical User Interface by clicking the “pgAdmin” button in the Cloud IDE interface.

Screenshot highlighting pgAdmin button

Once the pgAdmin GUI opens, click on the Servers tab on the left side of the page. You will be prompted to enter a password.

Screenshot highlighting Servers tab

To retrieve your password, click on the “PostgreSQL” tab near the top of the interface.

Click on the Copy icon to the left of your password to copy the session password onto your clipboard.

Screenshot highlighting PostgreSQL tab and copy icon

Navigate back to the “pgAdmin” tab and paste in your password, then click OK.

Click on Postgres > Databases.

Right click on demo and click the Backup button.

Screenshot highlighting Postgres dropdown menu, Databases dropdown, Demo dropdown, and Backup button

Enter a name for the backup (For example, “demo_backup”), set the Format to Tar, then click the “Backup” button.

Screenshot highlighting Filename, Format, and Backup button