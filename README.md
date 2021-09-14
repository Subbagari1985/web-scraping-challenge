# Web-scraping-challenge
Build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. User shall be able to scrape the data on the website by click of a button and view the information on the web page.

# Process:
1) Use Jupyter notebook to visit different websites and scrape the information as needed.

  A) Used BeautifulSoup to parse the HTML of the website "https://redplanetscience.com/" and retreive the title and paragraph of the news.
  
  B) Used BeautifulSoup to parse the HTML of the website 'https://spaceimages-mars.com/' to retrieve and concatenate the image URL with the Website URL.
  
  C) Used pandas to read the html tables for Mars facts from 'https://galaxyfacts-mars.com/', added the column names to the first table, set the index on the table and convert the table to HTML string.
  
  D) Used BeautifulSoup to parse the HTML of the website 'https://marshemispheres.com/' to retrieve the title and image URLfor all 4 Hemispheres.
  
  E) Create a Dictionary with all the information gathered from the above steps.
  
  
 2) Create Flask_app.py fileReturn template and data.
 
    A) Create an instance of Flask website.
    
    B) Use flask_pymongo to set up mongo connection.
    
    C) Route to render index.html (Home page) template using data from Mongo.
    
         Find one record of data from the mongo database.
         
         Return template and data.
         
    D) Route to Scrape method - accessed from the button on the home page.
    
        Update the Mongo database using update and upsert=True.
        
    E) Since website (development) is not live, debug is True.   
    
    
 3) Create index.html and use Bootstrap to align the information and table on the web page.
 
     
  

# Conclusion:

Screenshot of the website in full window - Image 1.
![Website in Full Window 1](https://user-images.githubusercontent.com/85588653/133193276-e0c743c1-7042-4ab8-b42f-db1982645c8a.png)

Screenshot of the website in full window - Image 2.
![Website in Full Window 2](https://user-images.githubusercontent.com/85588653/133193368-38551c6a-6093-4af6-ba35-6a8d23a656a2.png)

Screenshot of the website in minimized window - Image 1:
![Website in Minimized window 1](https://user-images.githubusercontent.com/85588653/133193411-39a3e5e8-4524-4b27-9cb1-424a07561740.png)

Screenshot of the website in minimized window - Image 2:
![Website in Minimized window 2](https://user-images.githubusercontent.com/85588653/133193443-6bf8adac-76c6-4c62-92aa-8a34f83bb910.png)



