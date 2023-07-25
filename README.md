
# The Lazy Electricians Helper App
Hello, my name is Anthony and Im an Electrician who loves doing projects with what little free time I have. My most recent project is an app ive been working on the make my work day a little easier. Check it out......<br><br>
This github repository is a on going project for developing the best electrical helper you will ever have. Guarenteed better than even your best apprentice on your crew. It started off as a simple **PWA**(Progressive Web App) to calculate the amount of material you need to order based off of how many plugs/switches/etc... the print on your job calls for. It has grown into an app that will allow you to download a custom material sheet, ready to be turned straight into the boss. It can also connect to a google account(currently only mine) and will make a whole set of google sheet documents for the entire course of the job. It will generate job specific **To-Do Lists** with the same info you gave the app to generate the **Material List**. It lists each task in order of a typical job with the quantity of items per task(see below). All you have to do is count the amount of Bracket Boxes/switch boxes/lights that were installed that day, update the To-Do list and you will have an overall percentage of completion for the job. It splits the projects up into 3 sections for each inspection that needs to be called: **Walls, Ceilings** and **Trim**. There is also a **Calendar** spreadsheet that can be used to be keep track of all ongoing jobs in your company. 

**Calendar Columns**
 - Job Name
 - Phase of Project
 - Schedulued dates on site
 - Complete-by Dates
 - Invoiced(or not)
 - Job Number
 - Percentage Complete 
  
 The Percentage Complete column is connected to each jobs' set of documents so that it is always up to date as long as the jobs Forman updates his documents regularly. It also has a custom **Apps Script** button in the Google Sheets menu bar that will use all of the names and dates from the calendar spreadsheet to generate a google calendar so that you can keep tracks of all on going jobs. Each Job document also has a set of other commonly used documents during the course of a job-
 
 **Templates**
 - Change Order Form
 - A Cross reference sheet for your actual available Panel and Circuit #s vs. Print Circuit #s
 - Panel Schedules(30 breakers(1-30), 42 breakers(1-42), 42 breakers(43-82), 84 breakers(1-84)
 - Job Lists(Optional- If used: when adding new jobs on the calendar it will give you a drop down of all jobs and will auto fill the job number)


Additionally, back in the app, there is a **Counter Helper** that simply allows you to type in what ever type of material item/Installed items you are needing to count up, whether in the field or while infront of your print, and it will create a tile that when clicked will increase in value by 1. You can make as many object tiles as you would like and add to it throughout the day. Its also useful for when you are walking your job trying to count how many lights were installed that day and people keep trying to talk to you making you loose track over and over. 


**PWA**
For the uninformed, a Progressive Web App is just a WebPage that has added functionallity to it. It is platform agnostic so it can be installed on your computer, iphone, android, google pixel, etc. All you have to do is go to a PWA enabled website, click the send button in your browser(if on phone) and click save to home page. This allows you open it from your mobile devices home page. It takes the browsers search bar away and allows it to function offline and push notifications to the phone just like a normal app. 

**Run your own server**
There are many ways you can use the code included in this github repo to run the app on your own server. That will enable you to change code, add features, stylize it, and add your own Google API credentials so that you can benifit from more than just a generated material list. Heres how-
**Python-**

 1. Download Python
 2. Clone or download the code in this project and go to the root folder
 3. Install a python virtual environment -`pip install virtualenv`
 4. Create a new virtual envirnment`python -m venv materialapp`
 5. Activate your virtual environment `source env/bin/activate`
or for Windows `cd venv\Scripts` then `.\activate`
 6. From your root directory run `python final.py` 
 7. Now go to your browser and type in "localhost:5050" 
 8. Thats it, you now have your own app server

**Docker Container**
I have included a Docker file as well as a docker-compose file. If you know what that is than i will assume you know how to get the server up and running with either one. If not, i suggest you look into it because docker has provided countless hours of learning and entertainment for myself. I am very proud to say that I was able to make  and upload my own docker container to DockerHub after years of being on the downloading side of things. Here is some screen shots of the app in action

**Home Screen**
<img src="https://github.com/materialapp/Public/blob/main/screenshots/Homescreen.PNG" width="1200" />
**In-app Material List**
<img src="https://github.com/materialapp/Public/blob/main/screenshots/In-app_material_list.PNG " width="1200" />
**Google Sheets Upload**
<img src="https://github.com/materialapp/Public/blob/main/screenshots/sheetsUpload.PNG" width="1200" />
**Counter Helper**
<img src="https://github.com/materialapp/Public/blob/main/screenshots/Counter%20Helper.PNG" width="1200" />
**Job Documents**
<img src="https://github.com/materialapp/Public/blob/main/screenshots/Job%20Documents.PNG" width="1200" />
**Material List**
<img src="https://github.com/materialapp/Public/blob/main/screenshots/material%20list.PNG" width="1200" />
**Walls Progress Sheet**
<img src="https://github.com/materialapp/Public/blob/main/screenshots/Wall_Progress_Sheet.PNG" width="1200" />
**Calendar**
<img src="https://github.com/materialapp/Public/blob/main/screenshots/Calendar.PNG" width="1200" />
**Production Calendar**
<img src="https://github.com/materialapp/Public/blob/main/screenshots/Production_Calendar.PNG" width="1200" />
**Circuitry Cross Reference Sheet**
<img src="https://github.com/materialapp/Public/blob/main/screenshots/Makeup%20Sheet.PNG" width="1200" />
**Panel Schedule**
<img src="https://github.com/materialapp/Public/blob/main/screenshots/panel%20schedule_1-42.PNG" width="1200" />



