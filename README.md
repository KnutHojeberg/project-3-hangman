# Hangman game 

## This game is a word game where the goal is to guess the word by selecting different letters until the word is complete. The user is presented with a number of blank spaces representing the missing letters that they will need to find. This game was created to complete the third portfolioprodject for Code Insitute's Full Stack Software Developer course.

#### Live Site [Here](https://hangman-knut.herokuapp.com/)

#### How to play
- The user need to type in their name and press enter.
- The user need to select a letter.
- If the user selected letter is present in the answer, all empty spaces where that letter is present will be filled with that letter.
- The user has a total of seven attempts.
- The user can only answer with letters, numbers and characters are not approved to use.
- If the user cant guess the word within the seven attempts, the man will be hanged and the game is over.
- If the user guesses correctly, it will say "Congratulations, you guessed the right word, you win" and the game is over.

## Features
- The user is greeted with a welcome message. When the user starts the game, it will ask the user to enter their name. The user then presses enter and  a hello message will appear displaying their name and the game will begin.
![alt text](controllers/assets/images/start.png)

- It is only possible for the user to guess at letters, numbers and characters do not work.
![alt text](controllers/assets/images/not-valied-number.png)

- It is only possible for the user to guess the same letter once, if repeated guesses the game will say already guess.
![alt text](controllers/assets/images/already-used.png)
- If the letter guessed by the user is incorrect, the hangman picture will be populated piece by piece, starting from head to the legs.
- If the user is unable to guess the word in 7 attempts, the hangman will be completed and the user will have lost the game. If the user fails to guess the correct word, the correct word will be determined when the game is over. To replay the game, the user will need to chose Y/N and press enter and if Y the game will restart.
![alt text](controllers/assets/images/lost.png)

- If the user can guess the word, the user will receive a congratulations message and they will have won the game. To replay the game, the user will need to chose Y/N and press enter and if Y the game will restart. If N is chose the game will not restart.
![alt text](controllers/assets/images/won.png)


## Technologies used
- Language
Python

## Frameworks, Deployement & Libraries

* [Github](https://github.com/)

* [Gitpod](https://gitpod.io)

## Testing

* Testing was done throughout the project mainly by running the program in the terminal. I tried to commit the codes to github after writing every new list or code.

* I used the deployed site to manually type correct and incorrect data to see how the game responded.

## Accessibility

* This project was built by using python, no other languages were therefore used.

## Issues and bugs
- I realized that the user can write his name with both letters and numbers.

## Fixed bugs
- problem: I had problems with dockstrings as I didn't understand where they should be.
- Solution: I turned to slack and the internet in the search for the solution.
- problem: I unindented spaces within the code.
- Solution: I turned to slack and the internet in the search for the solution.



## Validator Testing
I ran through my file in [](https://pep8ci.herokuapp.com/)
![alt text](controllers/assets/images/pep-validator.png)

## Deployment

I followed the below steps when deploying my project to Heroku, based on the Code Institute instructions:

* Add to requirements.txt file:-
pip3 freeze > requirements.txt
Commit changes to Github:
git commit -m "Add requirements for deployment”

In HEROKU after creating the account:

1. "Create new App"

2. Give the App a unique name and enter region

3. Click on "Create App"

4. Click on "Settings" on your new App Dashboard

5. Scroll down to Config Vars where in my instance I only inserted KEY: PORT and VALUE: 8000 since I have no creds.json files to add.

6. Press Add-button

7. Scroll down to Buildpacks and press the icon for Python, click Save Changes, then press the icon for Nodejs and save changes. These Buildpacks need to be in below order:

Python NodeJS

8. Go to Deploy section tab and scroll down to Deployment Method. I connected to my Github pages and could thereafter search for my Github Repository "Parents Allowance Calculator" and then click connect.

9. Scroll down to Automatic and Manual Deploys sections. I clicked on Automatic Deployment so that my changes that I push to github automatically updates in Heroku.

10. Then in the Manual Deploy section, press Deploy Branch.

11. After project has been deployed successfully I clicked the View-button to see the program run in the terminal.

## Credits

[Kite] https://www.youtube.com/watch?v=m4nEnsavl6w
My whole project is based on his youtube tutorial. however, I have tried to change a bit but have largely coded with him in his video.

Pages I used to solve errors and other problems and some code: 
https://stackoverflow.com/ 
https://www.programiz.com/python-programming/docstrings
https://www.edureka.co/blog/indentation-error-in-python/
https://www.w3schools.com/python/python_conditions.asp
https://www.geeksforgeeks.org/python-docstrings/

## Special Thanks

A big thank you to my mentor Jubril Akolade who helped me with planning and understading of this project.