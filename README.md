# assignment-2-nidhidhar02
assignment-2-nidhidhar02 created by GitHub Classroom

# Introduction
The goal of this dashboard is to provide an interactive way to analyse the performance of countries participating in the 2020 Tokyo Olympics. The dataset for this dashboard was obtained from Kaggle and can be found [here](https://www.kaggle.com/piterfm/tokyo-2020-olympics/version/2).
<br />
While the dataset contains a number of features related to the participating countries- the number of medals they won, the athletes representing these countries and details of their coaches, this dashboard limits its analysis to just understanding the distribution of medals across countries, and taking a closer look at a performance of a particular country.
<br />

# Design Decisions
### World Map showcasing medal distribution
The first question that came to mind when I had a look at the dataset was to see the number of medals each country had won, and what the breakup of their medal count was. In order to answer this question, I decided to use Altair to plot the distribution of medals by country on a world map. The visualisation also includes a filter for a particular medal type depending on whether we wish to seet the distribution of Gold, Silver, Bronze or all medals. Initially, I was considering making use of a bar plot to represent this information but that came with a lot of cognitive overload, the visualisation became very overwhelming and it was hard to process the information being conveyed. The use of colour density on a world map proved to be a more intuitive way to convey the same information, and hence I went ahead with this approach.
<br />
### Country Specifics Visualisations
Once I had taken a look at the overall medal distribution amongst all countries, I was curious to see how my own country had performed. More specifically, I wanted to see how many medals my country had won, which sports we had won the medals in, and the atheletes who were responsible for winning these medals.
In order to represent this information, I deicded to keep a country specific filter which would limit the data displayed in all subsequent visualisations to only that specific countrys data.
<br />
<br />
I made use of a donut plot, to visualise the breakup of medals for a specific country. I chose the use of a donut plot for this, because it made it easier to visualise that out of 100% of the medals my country had won, what percent was Gold, Silver and Bronze. This was information that was a lot harder to gauge from other visualisations like bar plots, histograms etc.
<br />
<br />
I also made use of bar plots to visualise who were the top scoring athletes, and which were the top scoring sports for a particular country. A bar plot representing the top N athletes/sports in descending order was a very clear way of representing this information and hence I chose to go ahead with it.
<br />

# Development Process
- I first explored Kaggle to identify interesting datasets.
- Once I came across the Olympics dataset, I analysed it a little further to see what all feautres it had. I thought about what all information could be conveyed from the data in the dataset, and decided to limit the scope of my dashboard (and data), to analysing the distribution of medals amongst different countries, and breaking down the performance of a specific country.
- I then drew out a wireframe of what the dashboard would look like. This was done keeping in mind the information I wanted to gauge from the data and the visualisations that would best help me gauge that information.
- Once I knew what visualisations I would be creating, I preprocessed the data to keep only the relevant features. I also added the ISO country codes, and latitude and longitude data which would help me plot the medal distribution on a world map.
- Once all the data was in place, I proceeded with using streamlit to actually plot the visualisations.
- I then finetuned the flow of information in the dashboard, and deployed it.
<br />
This entire process took me about 10-12 hours. The part that took the longest for me was deciding what visualisations I wanted to plot, and also plotting the medal distribution on the worldmap. I looked up a lot of Altair documentation for this, Medium blogs and did a bit of trial and error to get the visualisation working as expected.
