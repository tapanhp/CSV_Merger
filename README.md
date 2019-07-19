# CSV_MERGER

This project aggregate some specific formatted CSV files and after add some columns and data at last



### Requirement

We have a group of separate spread sheets that have company contact information.  We have to edit the contact information in the spread sheets.

The spread are stored locally as csv files.

We need a python script that will execute the following.

**Select the following column values from each csv file:**

First name 
Last name 
Title 
Client name
Direct phone 
Main phone 
Cell phone 
Permanent Address 1
Permanent address city
Permanent address state 
Permanent address zip
Primary email 
Skills

That needs to be combined into a new csv file.

In the new csv file, we need to **add a column** called `Contact Owner`.

In that column we need to be able to insert an email value so we should have a **placeholder such as** `someone@example.com`.

Then in each spread sheet we need to take every `,` or comma value and replace it with a semi-colon `;` value.

Then once this is done for each csv, we need a function that can take each newly formatted csv and combine them into one csv file.

So we have two tasks:

1. Edit each individual csv file
2. Combine the edited csv files into one

We can separate them out into separate functions and for the first one we can provide the option to input multiple csv files at a time.





#### Sample data files are available inside [here](csv_merger) 

- python-sample-01.csv
- python-sample-02.csv



### How to use the script?

- Put the script inside the folder where all CSV files are stored
- Run the script with this command `python merger.py`



That's all to do.  The result file will be available inside the **output folder** with current time stamp value. 