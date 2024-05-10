Identify bottlenecks
Fine-tune queries
REduce response times

RDBMs optimization commands
- Mysql:  OPTIMIZE TABLE
reorganizes physical storage of table data and associated index to reduce storage space and improve efficiency (defragmentation)
Requires SELECT and INSERT privileges.

- PostgreSQL: VACUUM and REDINDEX 
VACUUM
Garbage collection , can also analyze
Reclaims lost storage space consumed by 'dead' tuples
frees up space on all tables
VACUUM table_name : on specified table.
Reclaims more space, locks database table, takes longer to run.

REINDEX
Rebuild an index using the data stored in the index's table and replace the old version.
Must be owner of index, table, or database
dropping and recreating an index
REINDEX INDEX myindex;

rebuilds a sing index: REINDEX TABLE mytable;
Rebuilds all indexes on a table:

- db2: RUNSTATS and REORG

RUNSTATS
Updates statistics in system catalog about characteristics(records, pages, avg record length) of tables, associated indexes, or statistical views.
For table : table reorganized.

REORG
reconstructing rows to eliminate fragmented data and by compacting.
On a partitioned table, you can reorganize a single partition.
Reorganize all indexes that are defined on a table by rebuilding the index data into unfragmented, physically continuous pages