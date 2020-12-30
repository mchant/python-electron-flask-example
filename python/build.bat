pyinstaller -F --add-data "templates;templates" --add-data "static;static" flask_server.py
copy dist\flask_server.exe  ..\electron\flask_server.exe /y
