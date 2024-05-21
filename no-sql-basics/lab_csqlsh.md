# Start Cassandra
Open a new terminal, by selecting Terminal->New Terminal from the menu bar, as in the image below.



This will open a new terminal at the bottom of the screen as in the image below.



Run the below command on the newly opened terminal. (You can copy the code by clicking on the little copy button on the bottom right of the codeblock below and then paste it, wherever you wish.)

1
start_cassandra
Copied!
This will start the cassandra server. It will also give you the command to connect to your instance of cassandra, as in the image below.


The command will look similar to the one given below.

1
cqlsh --username cassandra --password MTg3MzMtcnNhbm5h
Copied!
The command contains the username and password to connect to cassandra server. Your output would be different from the one shown above. Copy the command given to you, and keep it handy. You will need it in the next step.

# Find host details

show host

# Find the version of the server

show version

# List keyspaces

describe keyspaces