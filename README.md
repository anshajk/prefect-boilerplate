# Prefect orchestration boilerplate

The focus of this project is to create a complete data engineering solution using the [Prefect workflow engine](https://www.prefect.io/).

## Requirements

- [Docker Compose](https://docs.docker.com/compose/install/)
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

## Development setup

- Create a python environment with ```conda create -n prefect-env python=3.8```
- Activate the python environment with ```conda activate prefect-env```
- Install the requirements with `pip install -r requirements.txt`
- Create a [user token](https://docs.prefect.io/orchestration/tutorial/configure.html#create-a-personal-access-token) and add it to the prefect CLI with ```prefect auth login -t <COPIED_TOKEN>```
- [Create a runner token](https://docs.prefect.io/orchestration/tutorial/configure.html#create-a-runner-token) and save this token in the .env file
- Start an agent with ```prefect agent start --name "<Name of the agent>" --token <RUNNER TOKEN>```
