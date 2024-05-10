#  Enable Error Logging and Observe Logs

first, to enable error logging on your PostgreSQL server instance, you will need to configure your server to support it. You can do so by using the Cloud IDE file explorer to open postgresql.conf, which stores the configuration parameters that are read upon server startup. Let’s go ahead and do it.

With the configuration file open, scroll down to line 431. Replace logging_collector = off with logging_collector = on and uncomment the parameter by removing the # before the line.

Confirm that the configuration parameter was successfully changed and loaded into the PostgreSQL instance by entering the following command into the CLI:


SHOW logging_collector;

# View the Server Logs

SHOW log_directory;

Open up the file explorer on Cloud IDE and navigate through postgres > data >log
You will see a file with a name of the form postgresql-YYYY-MM-DD-<numbers>.log


