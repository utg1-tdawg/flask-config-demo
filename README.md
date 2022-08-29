## Key resources
- https://flask.palletsprojects.com/en/2.2.x/config/
- https://github.com/pallets/flask/blob/main/src/flask/config.py

## Overview
There are two key places to load a Flask app's configuration values from - config files (.py or .cfg etc) or environment variables. \
Ideally, both should be used in tandem - store public dev vs prod configs in configs files and store sensitive configs as environment variables. 

## Using config files
Configurations can be stored in classes or just within the file directly. Both can be loaded using `app.config.from_object()`. 
However, it might be easier to distinguish between dev and prod configs using classes. 
\
[Note: do not store sensitive information in config files (classes or not)](https://stackoverflow.com/questions/56580514/is-it-acceptable-to-commit-api-keys-and-env-files-to-a-private-business-repo)

## Using environment variables
Can store at machine-level and retrieve using `app.config.from_prefixed_env()` or store at repo-level using `dotenv` library (better). 
