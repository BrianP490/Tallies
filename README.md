# Tallies
Django Social Blogging App with a Snake Game Mini-Game.
Create your own profile, and begin exploring the application. Spark up some interesting posts, and see what others are talking about. 
With each post and comment, you gain points added to your overall score.

This project is hosted on a live AWS EC2 instance with AWS S3 Static file server.

Available with URL --> http://54.67.48.3:8000 <--






DESIGN PLAN:

 LOGIN PAGE - DONE!!!
    first ask user to login always
    redirects to home page once correct user credentials entered
    create a user if they are new > DIRECTED TO SIGNUP PAGE

SIGN UP / Create User - DONE!!!
    Ask for email, username, pswd
    Ask for Profile Picture
    initialize user tally score

LOGOUT - DONE!!!
    On logout > redirect to login page

INDEX - HOME PAGE - DONE!!!
    personal posts (Your Tallies)
    explore button via logo click
    play snake mini-game
    Display User profile picture
    Display User Tally Score
    Edit user/profile page
    Delete a User

EXPLORE PAGE - DONE!!!
    limit number of blogs per page (DJANGO PAGINATION)
    next page option

BLOG DETAIL PAGE - DONE!!!
    topic
    people
    comment button
    write comment
    add comment (this should increase both the Blog Owner's score and the Commenter's score)
    Delete A Blog

NEW BLOG PAGE - DONE
    add new category

ABOUT US PAGE - DONE!!!
CONTACT PAGE - DONE!!!
TERMS PAGE - DONE!!!
PRIVACY PAGE - DONE!!!
