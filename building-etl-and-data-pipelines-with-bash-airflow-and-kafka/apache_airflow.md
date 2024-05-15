# Overview

A platform that lets you build and run workflows.
A workflow is represented as a DAG (Directed Acyclic Graph), and contains individual pieces called tasks.
Is not a data streaming solution, It is primarily a workflow manager.

#  Architecture

- Scheduler:
Handles the triggering of all scheduled workflows.
Is responsible for submitting individual tasks from each scheduled workflow to the executor.

- Executor:
Handles the running of these tasks by assigning them to workers, which then run the tasks.

- Web server:
Serves airflow's powerful interactive UI.

- DAG Directory:
Contains all of your DAG files, ready to be accessed by the scheduler.

- Metadata database:
Airflow hosts a metadata information, which is used by the scheduler. executor, and the web server to store state of each DAG and its tasks.

# Advantages of Using Data Pipelines as DAGs in Apache Airflow

DAG

- Graph - a simple graph consist of nodes and edges
Circles called nodes and lines connecting pairs of nodes are called edges.
Edges connecting nodes
Acyclic - no loops (cycles) 

**DAG in airflow**
DAG represent workflow
Each task performed by your data pipeline is represented as a node in a DAG
Each of these dependencies is represented as a directed edge.

# Tasks (nodes) and operators
Tasks are written in python
Tasks  implement operators, for example, python, SQL, or bash operators

# DAG definition components
Python script blocks:
Library imports
DAG arguments
DAG definition
Task definitions
Task pipelines

