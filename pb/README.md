## Posterboy - A chatbot to serve movie posters

### Introduction



---

#### Prerequisites

- Install Anaconda - A packaged software which includes a lot of tools and libraries to build python and AI/ML programs

  https://www.anaconda.com/products/individual

- Open Anaconda prompt in administrator mode

- Create a conda virtual environment

  ``` conda create -n rasa python=3.6 anaconda ```

- Load conda venv

  ``` conda activate rasa ```

- upgrade pip

  ``` pip install -U pip```

- Install rasa-x

  ``` pip install rasa-x --extra-index-url https://pypi.rasa.com/simple ```

- Install spacy

  ``` pip install spacy ```

- Download English language pack

  ``` python -m spacy download en ```

- Download web pack

  ``` python -m spacy download en_core_web_md ```

- Link web and en

  ``` python -m spacy link en_core_web_md en --force ```

- Create a directory of your choice ( For eg. D:\code\chatbot) and move into that directory (cd D:\code\chatbot)

- Clone this repository 

  ``` git clone https://github.com/AdityaSP/posterboy ```

- cd to this repository

  ``` cd posterboy```

- Get a free api key from omdbapi
- Replace your apikey in actions.py

### How to use this code base

---

#### Train the NLU model

​	```rasa train nlu```

#### Test NLU

​	``` rasa shell nlu ```

#### Training the dialogue model

- Start the action server

  As we have a custom action "action_poster". We need to start an action server. This action server will host all the custom actions

  ``` rasa run actions ```

- Open a new anaconda terminal, change directory to posterboy, activate the rasa venv and train the model

  ```rasa train```

- Start the chatbot as a shell

  ``` rasa shell```

### Experiments

1. How does it work for multiple work movie names?
2. Can you correct the dialogue flow where it always expects a greeting to start with?



