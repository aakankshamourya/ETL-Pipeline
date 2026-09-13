# 📚 Books Data ETL Pipeline

An end-to-end **ETL (Extract, Transform, Load) data engineering pipeline** built using Python, Pandas, and PostgreSQL to process a raw and partially unclean books dataset.

The project demonstrates how raw, inconsistent data can be transformed into a **clean, validated, structured, and database-ready dataset** through an automated ETL workflow.

---

## 🚀 Project Overview

Real-world datasets are rarely clean.

The input books dataset used in this project contains issues such as:

- Missing values
- Inconsistent data formats
- Incorrect or inconsistent data types
- Duplicate records
- Unnecessary whitespace
- Inconsistent categorical values
- Invalid dates
- Invalid ratings
- Incomplete records
- Formatting inconsistencies

Instead of manually cleaning the dataset, I developed an automated ETL pipeline that performs:

```text
                 RAW BOOK DATASET
                        │
                        ▼
              ┌──────────────────┐
              │     EXTRACT      │
              │                  │
              │ Read raw dataset │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │     PROFILE      │
              │                  │
              │ Inspect columns  │
              │ Missing values   │
              │ Data types       │
              │ Duplicates       │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │    TRANSFORM     │
              │                  │
              │ Clean data       │
              │ Handle missing   │
              │ Normalize values │
              │ Convert types    │
              │ Remove duplicates│
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │     VALIDATE     │
              │                  │
              │ Schema checks    │
              │ Data quality     │
              │ Business rules   │
              └────────┬─────────┘
                       │
                  Validation
                     Passed
                       │
                       ▼
              ┌──────────────────┐
              │       LOAD       │
              │                  │
              │ PostgreSQL       │
              │ Database         │
              └────────┬─────────┘
                       │
                       ▼
                CLEAN BOOK DATA
ETL Architecture
                                  ┌────────────────────┐
                    │   Raw Dataset      │
                    │                    │
                    │   Books CSV/Excel  │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │      EXTRACT       │
                    │                    │
                    │ Read source data   │
                    │ Load into Pandas   │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │      PROFILE       │
                    │                    │
                    │ Schema             │
                    │ Null analysis      │
                    │ Data types         │
                    │ Duplicate analysis │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │     TRANSFORM      │
                    │                    │
                    │ Cleaning           │
                    │ Standardization    │
                    │ Type conversion    │
                    │ Missing values     │
                    │ Deduplication      │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │      VALIDATE      │
                    │                    │
                    │ Schema validation  │
                    │ Data validation    │
                    │ Business rules     │
                    └─────────┬──────────┘
                              │
                         PASS / FAIL
                              │
                              ▼
                    ┌────────────────────┐
                    │        LOAD        │
                    │                    │
                    │    PostgreSQL      │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │   Clean Database  │
                    │      Dataset       │
                    └────────────────────┘
Database Used
PostgreSQL

PostgreSQL is used as the target relational database.

The cleaned dataset is loaded into PostgreSQL after successful validation.

SQL

SQL is used for:

Database/table creation
Querying records
Data verification
Aggregations
Filtering
Data quality checks
