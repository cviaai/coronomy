[![Python](https://img.shields.io/badge/python-3.7-blue.svg)](https://python.org)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)


## Coronomy
A network for those people who lost their jobs due to COVID-19; those companies that went bankrupt; and those investors who want to help recover the economy.

# A UNESCO 'Code the Curve' Hackaton submission

<p align="center">
<img src="/imgs/logo.png" width="300" alt>
</p>

An online demo of the project is available at https://www.coronomy.online

# Mission

Our solution is essentially a facebook for the unemployed and for the owners of the bankrupt companies. So that they can find each other. Network will connect the job-seeking people and the sinking employers based on their reputation - the snapshot from just a couple of months ago.

Through this database, venture capital and government recovery funds could find the matched pairs of employees and employers to revive the most important areas of the damaged economy. Service architecture is based on the Python-Flask framework and utilizes cloud solutions. As of today, we have an online-platform that features a web application, cloud-based model services and a MySQL database. 

<p align="center">
<img src="/imgs/map.jpg" width="600" alt>
</p>
<p align="center">
<em>Map of the companies experiencing difficulties with finance/salary payments/rent etc. during the COVID-19 pandemic.</em>
</p>

PLatform takes the advantage of the intelligent AI-based planning and matching algorithms such as the developed C-scoring system used to match the available resources of the nearby companies and would-be employees:

<p align="center">
<img src="/imgs/companies.png" width="600" alt>
</p>
<p align="center">
<em>Demo results fetched from the database based on the skills and location of a user.</em>
</p>

For a demo-login:
```
https://coronomy.online/login
```
With the following credentials:
```
Login: abc@d.io
Password: secret
```

## Installation as a project repository:

```
git clone https://github.com/coronomy.git
```

In this case, you need to manually install the dependencies.



## Deploy on Heroku (free)
First, edit the app.json and replace the value of the `repository`:
```
"repository": "https://github.com/cviaai/coronomy"
```
with the URL to the forked repository.

Then click on the button:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
