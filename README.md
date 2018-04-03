# Gym plane!
2D STG plane war game, author is [@buaawyz](https://github.com/buaawyz)

Learning how to make simple games from **FishC**'s blog.

This can be use as a gym-environment for Reinforcement Learning or other experiments.

# Installation
Download this repo or clone it locally.

# How to use
- First run `python main.py`. This will create a socket server and wait for client
- Then in another shell or scipt `from client import Client` and then `client = Client()` to create a client to connect to the server established by `main.py`
- Finally, use `client.send(commands)`to control plane, where commands can be 
```json
{
    '0': nothing, 
    '1': up, 
    '2': down, 
    '3': left, 
    '4': right, 
    '9': disconnect
}
```

- Enjoy!

# Dependency
- pygame
