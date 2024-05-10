- Full backups

Backups all the specified data.
Increased size
Multiple copies of the backup means storing many instances of a large file.
Only storing one copy risks data loss if file is corrupted.
Must secure backup files.

- Point-in-time recovery

Used logged transactions to restore an earlier point-in-time, you can use the information in the log file to reapply the transactions to the restore database.
=> Recover the data to a state that it was in at a particular time.

- Differential backups

A copy of any data that has changed since the last full backup was taken.
This make the backup file much smaller, example one backup every week, or month and restore every month or every week.

- Incremental backups

A copy of any data that has changed since the last backup of any type was taken.
For example, you could perform a full backup once a week on a Sunday and then run an incremental