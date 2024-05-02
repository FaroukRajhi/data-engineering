# Layers od a data platform architecture

1. Data Ingestion or data collection layer
Is responsible for connecting to the source systems and bringing the data from theses systems into data platform.
Transfer data from data sources to the data platform in streaming and batch modes.
Maintain information about the data collected in the metadata repository.
Tools:
Data flow GCP
IMB streams amazon kinesis

2.  storage and integration layer
Store data for processing and long-term use.
Transform and merge extracted data either logically or physically
Relational databases:
Mysql server
Imb db2
Postgresql server
Database as a service
No-SQL databases

Check database integration tools

3. Data processing layer
Read data in batch or streaming modes from storage and apply transformations.
Support popular querying tools and programming languages
Scale to meet the processing demands of a growing dataset.
Provide a way for analysts and data scientists to work with data in the data platform.

Transformation tasks:
Structuring -Actions that change the form and scheme of the data.
Normalization - Cleaning the database of unused data and reducing redundancy and inconsistency.

De-normalization: Combining data from multiple tables into a single table so that it can be queried more efficiently.
Data cleaning : Fixing irregularities in data to provide credible data for downstream applications and uses.
Tools:
spreadsheets, openRefine Google dataPrep and more.

4. Analysis and user interface layer
Delivers processed data to data consumers include:
BI Analyst
Business stakeholders
Data scientist and data analysts
And other applications and services
Querying tools and programming languages.
SQL, python, R, and java
APIs that can be used to run reports on data for both online and offline processing.
APIs that can consume data from the storage in real-time for use in other applications and services.
Dashboarding

5. Data pipeline
Overlaying the data ingestion, data storage and integration, and data processing layers is tha data pipeline layer with the extract, transform, and load tools.
This layer is responsible for implementing and maintaining a continuously flowing data pipeline.
Solutions:
AirFlow and Data flow