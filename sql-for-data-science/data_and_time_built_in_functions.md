**Date Functions**

YEAR(); MONTH(); DAY(), DAYOFMONTH(), DAYOFWEEK(), DAYOFYEAR(), WEEK(), HOUR(), MINUTE(), SECOND(),

Extract a day portion from a date

select DAY(RESCUEDATE) from PETRESCUE where ANIMAL= 'Cat'

In the WHERE clause:

select COUNT(*) from PETRESCUE where MONTH(RESCUEDATE) = '05'

- Special registers:
CURRENT_DATE, CURRENT_TIME

select FROM_DAYS(DATEDIFF(CURRENT_DATE, RESCUDATE)) from table