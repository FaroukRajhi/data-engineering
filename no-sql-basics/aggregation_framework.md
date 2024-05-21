Also refers to aggregation pipeline.
Is a series of operations that you apply on your data to get a desired outcome.

Process...Stages...Outcome
For example:
Average student score in each course for 2020

db.courseResult.aggregate([{$match: {"year": 2020}, {$group: {"_id": "$courseId, "avgScore": {$avg: "$score"}}}}])

- Aggregation stage

{$match: {"year": 2020}},: Filter out documents form year 2020
{$group: {"_id": "$courseId, "avgScore": {$avg: "$score"}}}: $group => to group documents form the last stage using 'courseId', and calculating the average in a field called 'avgScore'

There are common aggregation stages check documentation

