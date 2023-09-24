# Devil's Advocate

Website Link: [Devil's Advocate](https://devils-advocate-afu.herokuapp.com/)

An e-commerce website selling 'devil fruits' from the 'One Piece' series. Data scraped from a third party site, complete with a cart system and authentication.

Technologies used:

- [React](https://reactjs.org/) - Frontend framework
- [Redux](https://redux.js.org/) - State container for managing cart system, authentication, and storing shared variables
- [React Router](https://reactrouter.com/) - Routing
- [Styled Components](https://styled-components.com/) - CSS styling written into custom components, gets rid of having to use separate css files
- [Node.js](https://nodejs.org/en/) - Backend runtime environment
- [Express](https://expressjs.com/) - API for fetching and storing data to database
- [MongoDB](https://www.mongodb.com/) - Database
- [Scrapy](https://scrapy.org/) - Webscraping framework used to gather all the products displayed from a third party site
- [JWT](https://en.wikipedia.org/wiki/JSON_Web_Token) - Reliable authentication

Features in this version:

- User authentication
- Displays all major fruits in the series
- Adding and removing fruits to cart
- Fruit amounts adjustable
- Cart contents linked to user
