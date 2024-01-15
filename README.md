# Target Practice Game for [Badger 2040](https://shop.pimoroni.com/products/badger-2040?variant=39752959852627)
The first program I wrote for the Badger, based on [a simple game a friend send me]()

## Aim of the game
The aim is to move your sights over the top of the target using the A, C and UP, DOWN arrows:

Sights:
```
| x |
```
Target:
```
----
| 0 |
-----
```

You must line up the aim with the target as quickly as you can. Once you have sucsessfully done this for 10 targets, you have completed the game and your time will be shown.
![image](https://github.com/Zoobdude/target-pactice/assets/96008479/9cdf9ee2-da5a-4329-a739-596928cd5b12)



### Todo
* Optimise and refactor. I wrote this over two years ago and it is by no means the most efficient method that could be used. I intend to put all the coodinates into a large dictionary.
* Multiple game lengths. Let the user choose the length of the game they would like to play.
* Different game modes. Rather than 
* High score. Store the the lowest time in a file to be used as a high score.
* Introduce the B button as a Fire Button
* Currently the time ellapsed only updates when a button is pressed. This means it can be very outdated if no buttons are pushed for a while. A partial update could be used every second to keep the timer updated.
