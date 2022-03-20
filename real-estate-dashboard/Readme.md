### Background
In this project you are going to create a dashboard to present important Real Estate data to users interested in purchasing a house. The user understands the housing market is very hot and homes are selling for higher than their listed or appriased prices.  In order to better understand the dynamics of bidding on a house, this dashboard will present data and visualizations to help with their bidding decisions.

Please keep in mind this project is intended to showcase your skill in delivering a small toy project and is not intended for actual production use.  Please spend no more than **4** hours on this unless it is something you genuinely feel interested in working on.  Anything delivered *in addition* to the requirements below will still be considered as part of our assessment. There is plenty of room for you to add your own design and stylistic elements to make it a more pleasing or effective UX/UI experience.

### Requirements
1. Create a new React App using [create-react-app](https://create-react-app.dev/) to serve as the basis for the Real Estate Dashboard described above.
2. Override the [fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) with a custom function that returns data from JSON objects to mimic fetching data from a remote REST API.  The static data is available in [house_sales](data/house_sales.json).
3. Add a Town selector dropdown with the available towns that can be selected from.
4. Using [AG Grid](https://www.ag-grid.com/react-data-grid/getting-started/), display a list of House Sales for the selected Town.
5. Using [Nivo](https://nivo.rocks/) create a scatter plot that plots the % Premium ((Sold Price - List Price) / List Price * 100) versus Closed Date to show the trend of home premiums over time.  The data for this grid should also be filtered on selected Town (from #3).

### Deliverables
1. Push the solution into a GitHub repository of your choosing.  Make sure the repository visibility is set to public.
2. Give a small write-up in a root-level Readme file that describes where one can find the solutions to each of the items above. Include how much time you spent.  Additionally, include a list of areas for improvement or further consideration if you were going to take this project and make it production ready.
3. Be prepared to discuss your solution if asked.
