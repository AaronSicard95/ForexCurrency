### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
syntax and scope

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
the try method
using default value

- What is a unit test?
testing a small sample of code

- What is an integration test?
testing the code within the application it's used in

- What is the role of web application framework, like Flask?
to communicate between the client and the server

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
whether it's the main focus of the page or just additional information

- How do you collect data from a URL placeholder parameter using Flask?
like passing a variable to a function ie "function'(parameter)

- How do you collect data from the query string using Flask?
request.args

- How do you collect data from the body of the request using Flask?
request.form

- What is a cookie and what kinds of things are they commonly used for?
information stored on the client.  Passwords, recent searches

- What is the session object in Flask?
An object that holds data for the current session between the server and that specific client

- What does Flask's `jsonify()` do?
turn flask data into a JSON string