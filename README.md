# Fedreal_Reserve_Meeting_minutes Project
Web scrapes of the Federal Reserve meeting minutes


#### fed_mins_notes:
Scrapy spider of the [Federal Reserve webpage](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm) that pulls all the meeting minutes of the Federal Open Market Committee since 2014. The notes can be found of in the fed_mins_2019_08_25.csv (the date the data was pulled was on 08/25/2019). I learned most of the techniques for this project from the [Datacamp web scraping course] https://www.datacamp.com/courses/web-scraping-with-python.


#### all_names:
Juypter notebook of the data cleaning process of the fed_mins.csv. Output creates a csv file to create a [Tableau dashboard](https://public.tableau.com/profile/richy.castellanos#!/vizhome/shared/368GSW29W). 


#### fed_mins:
HTML of all FOMC meeting minutes since 2014. Note this csv is slightly differnet than fed_mins_2019_08_25.csv. fed_mins includes the entire HTML while fed_mins_2019_08_25 includes only the TEXT!! This is done for easy name extraction. 
