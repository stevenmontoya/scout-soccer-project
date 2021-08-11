![Logo](https://raw.githubusercontent.com/stevenmontoya/scout-soccer-project/main/docs/logo.png)

## Structure

The project is divided into:

- **Client:** It contains the implementation of dynamic dashboards using libraries such as Streamlit, Plotly, etc.

- **Server:** Api that is consumed to obtain the necessary resources to supply the client. Api that is consumed to obtain the necessary resources to supply the customer. The Api is implemented using the [FastApi](https://fastapi.tiangolo.com) python framework

- **Data:** This directory contains the csv file with the statistics for each Euro 2020 match and a Jupyter Notebook in which the data is processed and cleaned and then stored in a database.

## Installation

First you will need to have Python installed, you can find some guides to help you [Guides](https://realpython.com/installing-python/)

Clone the repository

```bash
git clone https://github.com/stevenmontoya/scout-soccer-project.git
```

Use the command below to install the project dependencies

```bash
cd scout-projec
pip install -r requirements.txt
```

Install Jupyter

```bash
cd scout-projec
pip install -r requirements.txt
```

## Run Locally

### Run Jupyter

Go to the data directory

```bash
cd data
jupyter notebook
```

In Jupyter you can run all cells to process and perform data cleansing. They can also be saved in a database by configuring environment variables.

Be patient, data processing may take a few minutes.

### Run Client

Start the Streamlit server

Go to the client directory

```bash
cd client
```

Start the Streamlit server

```bash
streamlit run main.py
```

### Run Server

```bash
cd server
cd src
```

Start the Streamlit server

```bash
uvicorn main:app --reload
```

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`FOOTBALL_DATA_API_TOKEN`

`MONGODB_URL`

- To add some interesting data, requests are made to the following api [football-data](https://www.football-data.org/), you can get an api token for free

- You can add a connection url to Mongodb (on-premises or in the cloud)

## Screenshots

### Dashboard

![Dashboard](https://raw.githubusercontent.com/stevenmontoya/scout-soccer-project/main/docs/dashboard.png)

### Navigation

![Navigation](https://raw.githubusercontent.com/stevenmontoya/scout-soccer-project/main/docs/navigation.png)

### Teams

![Teams](https://raw.githubusercontent.com/stevenmontoya/scout-soccer-project/main/docs/teams.png)

### Compare

![Compare](https://raw.githubusercontent.com/stevenmontoya/scout-soccer-project/main/docs/compare.png)

## License

[MIT](https://choosealicense.com/licenses/mit/)
