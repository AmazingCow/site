{!HTMLSTART!}
{!NAVIGATIONBAR!}

# CoreRandom


## Intro 

```CoreRandom``` is a easy to use random number generator inspired in C# 
System.Random class.


### Motivation:

Often in games we need a random generator. While this can be easily used using 
the c++11 ```<random>``` facilities, we think that must have a cleaner way.

This core is basically a glue between the ```std::mt19937``` generator and 
```std::uniform_int_distribution``` distribution - Nothing fancy, but yet 
very nice to use.

We tried to add an interface for ```CoreRandom::Random``` much alike of C# 
```System.Random``` - So is very easy to use the same ```CoreRandom::Random``` 
object to generate random values from arbitrary ranges each time :D

<br>

As usual, you are **very welcomed** to **share** and **hack** it.


## Links

* [Documentation](./doxygen/index.html)
* [Github Page](https://www.github.com/AmazingCow-Game-Core/CoreRandom/)


{!FOOTER!}
{!HTMLEND!}
