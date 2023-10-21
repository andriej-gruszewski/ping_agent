# ping_agent
Ping chosen IP and save status to Google Sheet databse


Hey,
This software let's you to run ping commands in your desired device and save its status to Google Sheet database. Whenever status of IP is changing ("UP" status as IP adress responding or "DOWN" status as IP adress not responding), agent will parse information to
your Google Sheet with information of device name, IP adress, status and timestamp whenever status is changing.

General setup:

1. Edit config_file.txt
   Provide IPs you want to ping on device, add device name as a top line in conigf_file.txt - config_file.txt is red as: 1st line -> name of device
                                                                                                                         2nd, 3rd, 4th etc... lines are IP adresses you want to ping
   DON'T PLACE EMPTY ROWS IN CONFIG FILE!

2. Add your Google domain token inside of main.py
3. Share Google Sheet as read/write permission to Google token user
4. You can export whole soft to one .exe file with pyinstaller lib with command "pyinstaller --onefile main.py"
   If you want to run soft as a service, without visible dialog box, you can convert main.py file to main.pyw and run same command

5. Run .exe file in your desired device

   That's it!
