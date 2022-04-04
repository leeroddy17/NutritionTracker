# NutritionTracker

Project Description: The function of this tool is to help users get the nutritional facts about a variety of foods from restaurants and grocery stores. This will allow the user to find what food they would like to eat that fits their diets and needs. It allows the user to be aware of what they are eating and be more conscious about it. We would expect people looking to be more aware of what they are eating to use and benefit from this tool so that they can look up nutrition facts about various foods in order to plan their diet. We would expect users of all ages and genders to use our app and many people would benefit from it because it allows them to keep track of their eating habits and could lead them to live a healthier life.

How to run code:

Requirements Python 3.7

IDE: Any works as long Python can be run on so posssible IDEs include VS Code, Pycharm, and etc.

Libraries that are needed: 
Request
operator 
math

# Files

app.py - This file contains the flask code that serves as the route for all of our web pages. Here, we can
add new routes to our application as well as using python to do our backend and passing our outputs to the front-end
(such as the search() function running python code before rendering the pages)


templates - holds the html files \\

    - base.html - The base file that contains the navbar, since it is consistent across all pages, other pages will 
                    inherit from this class and build on top of it.
                    
    - index.html - Our home page, contains the search bar to query for foods
    
    - search.html - Once you search for an item, this page will print the top 10 items directly from the API. We can
                    decide later how we want this page to look, I was just making sure the backend algos and frontend 
                    were connected
                    
    - about.html - Incomplete, "About Us" page from the sketch


query.py - Contains our core algorithms
