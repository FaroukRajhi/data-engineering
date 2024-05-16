Welcome to “Verifying Data Quality.”
After watching this video, you will be able to:
Define data quality verification.
Identify why organizations verify data.
List examples of data quality concerns.
Outline a process for handling bad data.
Data verification includes checking your data for:
Accuracy⏤ Is your data correct?
Completeness⏤Is there missing data?
Consistency⏤ Are fields consistently entered? and,
Currency⏤Is your data up to date?
Data verification is about managing data quality and enhancing its reliability.
High-quality data enables successful integration of related data and its complex relationships.
Data verification also provides you with a complete and connected view of your organization,
data that is ready for advanced analysis, statistical modeling and machine learning,
and ultimately, more confidence in your insights and decision-making.
Unfortunately, data quality is not a top concern among the daily chaos of running
a company.
According to Harvard Business Review, IBM’s 2016 estimate of the yearly cost of poor
data quality, in the US alone, was over 3 trillion dollars.
Let’s identify data quality concerns that organizations contend with.
The first is accuracy.
Accuracy includes ensuring a match between source data and destination data.
How can accuracy become an issue?
Data migrating from source systems often contains duplicated records.
When users enter data manually, typos can find their way into the data records, yielding
out-of-range values, outliers, and spelling mistakes.
Sometimes large chunks of data become misaligned, causing data corruption.
For example, a CSV file might contain a legitimate comma, which the new system can misinterpret
as a column separator.
Another data quality concern is completeness.
Data is incomplete when the business finds missing values, such as voids or nulls in
fields that should be populated, or haphazard use of placeholders such as “9 9 9” or
“minus 1” to indicate a missing value.
Entire records can also be missing due to upstream system failures.
Consistency is another important data quality concern.
Are there deviations from standard terminology?
Are dates entered consistently?
For example, year-month-day and month-day-year formats are incompatible.
Is data entered consistently? For example, Mr. John Doe and John Doe might refer to the
same person in the real world, but the system will see them as distinct.
Are the units consistent? For example, you are expecting ”kilograms,” but you might
have entries based on “pounds,” or you are expecting 'dollar amounts,” but you
might have entries based on “thousands of dollars.”
Lastly, currency is an ongoing data quality concern for most businesses.
Currency is about ensuring your data remains up to date.
For example, you might have dimension tables that contain customer addresses, some of which
might be outdated.
In the US, you could check these against a change-of-address database and update your
table as required. Another currency concern would be name changes as customers can change
their names for various reasons.
Determining how to resolve and prevent bad data can be a complex and iterative process.
First, you’ll implement rules to detect bad data.
Then you’ll apply those rules to capture and quarantine any bad data.
You might need to report any bad data and share the findings with the appropriate domain
experts.
You and your team can investigate the root cause of each problem, searching for clues
upstream in the data lineage. Once you diagnose each problem, you can begin
correcting the issues.
Ultimately, you want to automate the entire data cleaning workflow as much as possible.
For example, you need to validate the quality of data in the staging area before loading
the data into a data warehouse for analytics.
You determine that data from certain data sources consistently has data quality issues
including:
Missing data,
Duplicate values,
Out-of-range values, and
Invalid values.
Here’s how an organization might manage and resolve these issues.
First, write SQL queries to detect these issues and test for them.
Next, address some of the quality issues that you’ve repeatedly identified by creating
rules for treating them, such as removing rows that have out-of-range values.
Create a script that runs queries to detect data quality issues that happen during the
nightly loads to the data warehouse.
This script applies corrective measures and transformations for some of these known issues.
Next, create a second script that automates the script you created in step 3.
After the data is extracted from the various data sources, this script automatically runs
the prior script’s SQL data validation queries every night in the staging area.
The script you created in step 3 generates a report of any remaining issues that could
not be automatically resolved. The administrator can review this report and address the unresolved
issues.
Some of the leading vendors and their tools for data quality solutions include:
IBM InfoSphere Server for Data Quality,
Informatica Data Quality,
SAP Data Quality Management,
SAS Data Quality,
Talend Open Studio for Data Quality,
Precisely Spectrum Quality,
Microsoft Data Quality Services,
Oracle Enterprise Data Quality,
And an open-source tool called OpenRefine.
Each of these solutions has its own strengths. Let's look at one of these solutions.
The “IBM InfoSphere Information Server for Data Quality” is an example of a product
that can help you perform data verification in a unified environment.
“InfoSphere Information Server for Data Quality” enables you to continuously monitor
the quality of your data, and keep your data clean on an ongoing basis, helping you turn
your data into trusted information.
In addition, the “IBM InfoSphere Information Server for Data Quality” comes with built-in,
end-to-end data quality tools to:
Help you understand your data and its relationships.
Monitor and analyze data quality continuously.
Clean, standardize, and match data; and
Maintain data lineage, which is the history of the data’s origin and what happened to
the data along the way.
In this video, you learned that:
Data verification includes checking your data for accuracy, completeness, consistency, and
currency.
Data verification is about managing data quality, enhancing data reliability, and maximizing
data value.
Determining how to resolve and prevent bad data can be a complex and iterative process.
Enterprise-grade tools such as “IBM InfoSphere Information Server for Data Quality” can
help you perform data verification in a unified environment.