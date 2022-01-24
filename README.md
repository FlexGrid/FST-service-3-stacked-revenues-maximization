# Flexgrid Pricing API server

This project is the implementation of the API server for the Use Case 4.2 of the
[FlexGrid project](https://flexgrid-project.eu).

The project provides two endpoints, one for submitting a simulation of pricing
algorithm, and one for retrieving the results. The definition of the API may be
found at
[https://pricing-api.flexgrid-project.eu/swagger/](https://pricing-api.flexgrid-project.eu/swagger/).

## Updating the swagger definition file

In order to make changes to this project, you can edit the the swagger
definition file, located in the path
[./swagger/pricing.yml](./swagger/pricing.yml). After editing the file, use the
script at [./regenerate.sh](./regenerate.sh) to update the server files. The
procedure is a follows:

1. Make sure that any changes are either committed or staged in `git`. Otherwise
   they risk being overwritten by the script.

2. Run `./regenerate.sh`.

3. Inspect the changes that are made with `git diff`.

4. For all the changes that are shown, you should decide which to keep and which
   to remove. Use `git checkout path/to/file` to use the original version of the
   file, or `git add path/to/file` to use the new version. If you run
   `./regenerate.sh checkout` the script will checkout the most common thinks
   that should bot be changed by the script.

5. In addition you will need to manually edit the controller files. If you
   haven't changed the any controller methods in the swagger file, you can keep
   your version with `git checkout swagger_server/controllers/controller_name.py`. Otherwise, you will need to
   merge the new definitions with the implementations from the codegen tool.

## Running the server locally for development

1. Checkout the project with the submodules, use:

   ```bash
   git clone --recurse-submodules https://github.com/FlexGrid/pricing
   ```

   If you already checked it without the submodules, use:

   ```bash
   git submodule init
   git submodule update
   ```

2. Create a python3 virtual environment (This only needs to be done the first
   time):

   ```bash
   python3 -m venv testenv
   ```

3. Activate the python virtual environment with:

   ```bash
   source testenv/bin/activate
   ```

   You should now see `(testenv)` before your username on the command line, To
   exit the environment run `deactivate` or close the terminal.

4. Install the dependencies with `pip`. If `pip` is not installed follow the
   instructions from
   [https://pip.pypa.io/en/stable/installation/](https://pip.pypa.io/en/stable/installation/).

   Afterwards install the dependencies from `requirements.txt` for the main
   project and the dependencies with

   ```bash
   pip install -r requirements.txt
   cd BRTP/
   pip install -r requirements.txt
   cd ..
   ```

5. To run the server using local data, without connecting the central database,
   use:

   ```bash
   FLASK_ENV=development SAMPLE_DATA=1 python -m swagger_server
   ```

6. Run the `celery` program to execute the background tasks. From the project's
   root directory, and after the `testenv` virtual environment has been loaded,
   run

   ```bash
   celery -A workers.tasks worker --loglevel=INFO
   ```

7. Submit a new job with:

   ```bash
   curl --location --request POST 'http://0.0.0.0:8080/pricing' \
   --header 'Content-Type: application/vnd.api+json' \
   --header 'Authorization: Bearer XXXX' \
   --data-raw '{
       "start_datetime": "2021-11-11T00:00:00Z",
       "end_datetime": "2021-11-12T00:00:00Z",
       "dr_prosumers": [ "user_1_High","user_2_High"],
       "flex_request": "flex_request_1_High",
       "profit_margin": 34.4,
       "gamma_values": [0, 1.0],
       "callback": {
           "url": "http://localhost:8080/pricing",
           "headers": {
               "Authorization": "Bearer O85XHy79Jz4H4Zir4C46MZexsmm7Ki",
               "Content-Type": "application/vnd.api+json"
           }
       }
   }
   '
   ```

   When using the sample data, the the allowed values for the `dr_prosumers`
   attributes are the following:

   ```json
   [
     "user_1_Low",
     "user_2_Low",
     "user_3_Low",
     "user_4_Low",
     "user_5_Low",
     "user_6_Low",
     "user_7_Low",
     "user_8_Low",
     "user_9_Low",
     "user_10_Low",
     "user_1_Medium",
     "user_2_Medium",
     "user_3_Medium",
     "user_4_Medium",
     "user_5_Medium",
     "user_6_Medium",
     "user_7_Medium",
     "user_8_Medium",
     "user_9_Medium",
     "user_10_Medium",
     "user_1_High",
     "user_2_High",
     "user_3_High",
     "user_4_High",
     "user_5_High",
     "user_6_High",
     "user_7_High",
     "user_8_High",
     "user_9_High",
     "user_10_High"
   ]
   ```

   Also, when using the sample data, the allowed value for the `flex_request`
   parameter is `"flex_request_1_High"`

   You should see new output in the window running the server, and also some
   output in the window running celery.

   The server will return a `job_id` value, that will be used for querying the
   status and the results of the simulation run.

   The definition of the API for this may be found at
   [https://pricing-api.flexgrid-project.eu/swagger/](https://pricing-api.flexgrid-project.eu/swagger/).

8. Get the result of the simulation using the previously obtained `job_id`.

   ```bash
   curl --location --request GET 'http://0.0.0.0:8080/pricing/d465eafa-0f5b-478c-b138-fd7098e5457a' \
   --header 'Content-Type: application/vnd.api+json' \
   --header 'Authorization: Bearer XXXX' \
   ```

   Once the simulation has been completed, you will results like:

   ```json
   {
     "date_done": "2022-01-24T14:08:09+00:00",
     "job_id": "b3597ec4-b131-4fdc-ab2a-a0f557637a2f",
     "result": {
       "callback_result": "['status: 400\\n\\n{\\n  \"detail\": \"\\'dr_prosumers\\' is a required property\",\\n  \"status\": 400,\\n  \"title\": \"Bad Request\",\\n  \"type\": \"about:blank\"\\n}\\n']",
       "plots": {
         "AUW_vs_GAMMA": {
           "plot_type": "scatter",
           "serries": [
             {
               "legend": "γ = 1.0 ",
               "xvalues": [0.0, 1.0],
               "yvalues": [null, null]
             }
           ],
           "title": "Ratio between AUW with B-RTP and AUW with RTP as a function of γ",
           "xlabel": "γ",
           "ylabel": "AUW with B-RTP(γ) / AUW with RTP (γ = 0)"
         },
         "FINAL_ECC": [
           {
             "plot_type": "scatter",
             "serries": [
               {
                 "legend": "Initial ECC",
                 "xvalues": [
                   1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0,
                   12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0,
                   22.0, 23.0, 24.0
                 ],
                 "yvalues": [
                   2.0814, 2.0814, 2.0814, 0.1961, 0.1961, 0.1961, 0.1961,
                   0.1961, 0.1961, 0.7979, 0.1961, 0.1961, 0.1961, 2.3413,
                   0.8053999999999999, 0.8053999999999999, 0.8053999999999999,
                   0.8053999999999999, 5.3648, 1.2332999999999998,
                   1.2332999999999998, 1.2332999999999998, 0.624, 0.624
                 ]
               },
               {
                 "legend": "Final ECC",
                 "xvalues": [
                   1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0,
                   12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0,
                   22.0, 23.0, 24.0
                 ],
                 "yvalues": [
                   0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                   0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
                 ]
               }
             ],
             "title": "Initial vs Final ECC (γ = 0.0)",
             "xlabel": "Time (h)",
             "ylabel": "Power Consumption (kW)"
           },
           {
             "plot_type": "scatter",
             "serries": [
               {
                 "legend": "Initial ECC",
                 "xvalues": [
                   1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0,
                   12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0,
                   22.0, 23.0, 24.0
                 ],
                 "yvalues": [
                   2.0814, 2.0814, 2.0814, 0.1961, 0.1961, 0.1961, 0.1961,
                   0.1961, 0.1961, 0.7979, 0.1961, 0.1961, 0.1961, 2.3413,
                   0.8053999999999999, 0.8053999999999999, 0.8053999999999999,
                   0.8053999999999999, 5.3648, 1.2332999999999998,
                   1.2332999999999998, 1.2332999999999998, 0.624, 0.624
                 ]
               },
               {
                 "legend": "Final ECC",
                 "xvalues": [
                   1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0,
                   12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0,
                   22.0, 23.0, 24.0
                 ],
                 "yvalues": [
                   1.3752118391908537, 1.3752118391908292, 1.3752118222612801,
                   1.269611142650799, 1.2411533567061659, 0.1961, 0.1961,
                   0.1961, 0.1961, 0.7978999999999901, 0.19610000000001104,
                   0.19610000000002384, 0.1961, 1.3074487589939092,
                   1.0381015562299152, 0.977275674674156, 0.6003953672813509,
                   0.6230941045615795, 2.06334292173531, 1.9222210624136888,
                   1.8882235073618179, 0.9220902391291911, 0.47034225742803887,
                   0.47009282777022365
                 ]
               }
             ],
             "title": "Initial vs Final ECC (γ = 1.0)",
             "xlabel": "Time (h)",
             "ylabel": "Power Consumption (kW)"
           }
         ],
         "FLEX_QUANTITY": {
           "plot_type": "bar",
           "serries": [
             {
               "xvalues": [0.0, 1.0],
               "yvalues": [0.0, 9.344611916256792]
             }
           ],
           "xlabel": "γ",
           "ylabel": "Flexibility Quantity Delivered (kW)"
         },
         "FLEX_REVENUES": {
           "plot_type": "bar",
           "serries": [
             {
               "xvalues": [0.0, 1.0],
               "yvalues": [0.0, 30.952882518717516]
             }
           ],
           "xlabel": "γ",
           "ylabel": "Flexibility Revenues (€)"
         },
         "UW_BAR": [
           {
             "plot_type": "bar",
             "serries": [
               {
                 "xvalues": [1.0],
                 "yvalues": [null]
               }
             ],
             "xlabel": "Users",
             "ylabel": "UW with B-RTP(γ)/UW with RTP"
           },
           {
             "plot_type": "bar",
             "serries": [
               {
                 "xvalues": [1.0],
                 "yvalues": [null]
               }
             ],
             "xlabel": "Users",
             "ylabel": "UW with B-RTP(γ)/UW with RTP"
           }
         ]
       },
       "raw_data": {
         "AUW_BRTP": [0.0, -36.2351327661877],
         "BB_BRTP": [0.0, -30.078507306324365],
         "FINALCONS": [
           [
             0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
             0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
           ],
           [
             1.3752118391908537, 1.3752118391908292, 1.3752118222612801,
             1.269611142650799, 1.2411533567061659, 0.1961, 0.1961, 0.1961,
             0.1961, 0.7978999999999901, 0.19610000000001104,
             0.19610000000002384, 0.1961, 1.3074487589939092,
             1.0381015562299152, 0.977275674674156, 0.6003953672813509,
             0.6230941045615795, 2.06334292173531, 1.9222210624136888,
             1.8882235073618179, 0.9220902391291911, 0.47034225742803887,
             0.47009282777022365
           ]
         ],
         "FLEX_Q": [0.0, 9.344611916256792],
         "FLEX_R": [0.0, 30.952882518717516],
         "TC_BRTP": [0.0, 0.8109857642068504],
         "uw_bar_plot": [[0.0], [-36.2351327661877]]
       }
     },
     "status": "SUCCESS"
   }
   ```

## Connect to the central database

In production the [central FlexGrid
database](https://db.flexgrid-project.eu/swagger/) will be used for obtaining
the simulation data.

You will need credentials to connect to the database server, which may be
obtained from the ICCS team from the [FlexGrid
project](https://flexgrid-project.eu)

The credentials needed will be:

- The `CLIENT_ID`
- The `USERNAME`
- The `PASSWORD`

These credentials should be placed in a file name `.env` in the project's root
directory.

The file will look like this:

```bash
CENTRAL_DB_BASE_URL=https://db.flexgrid-project.eu
CENTRAL_DB_CLIENT_ID=uBik...
CENTRAL_DB_USERNAME=myuser
CENTRAL_DB_PASSWORD=dsfafjnskdfn
```

Then you will be able to run the server without the `SAMPLE_DATA=1` environment
variable, and the real data will be used. Follow the same steps as before, but
this time use

```bash
FLASK_ENV=development python -m swagger_server
```

to start the server.

Don't forget to load the python virtual environment `testenv`, and to start the
celery service as mentioned before.

Now you will be able to obain the valid `dr_prosumers` object names, and the
valid `flex_requst` names from the central DB API. You the following requests
for this:

- [https://db.flexgrid-project.eu/swagger/#/Dr_prosumer/getdr_prosumers](https://db.flexgrid-project.eu/swagger/#/Dr_prosumer/getdr_prosumers)

- [https://db.flexgrid-project.eu/swagger/#/Flex_request](https://db.flexgrid-project.eu/swagger/#/Flex_request)

## Develop using local database

If you want to try a local copy of the central database, you can use the
repository at
[https://github.com/FlexGrid/central-db-api](https://github.com/FlexGrid/central-db-api),
and the set the `.env` file with the appropriate `CENTRAL_DB_BASE_URL` value,
such as `http://localhost:5000`, and also set the credentials set in your local
copy of the database.

## Deployment instructions

Deployment has been tested with `nginx` with `uwsgi`, using `systemd` to start
and enable the api service and the celery program for the background tasks.

Sample configuration files for these services may be found at the
[./config/](./config/) subdirectory, but changes are needed to set your oun url,
file paths, and user names.

---

Original README.md from upstream

## Swagger generated server

### Overview

This server was generated by the
[swagger-codegen](https://github.com/swagger-api/swagger-codegen) project. By
using the [OpenAPI-Spec](https://github.com/swagger-api/swagger-core/wiki) from
a remote server, you can easily generate a server stub. This is an example of
building a swagger-enabled Flask server.

This example uses the [Connexion](https://github.com/zalando/connexion) library
on top of Flask.

### Requirements

Python 3.5.2+

### Usage

To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m swagger_server
```

and open your browser to here:

```
http://localhost:8080//ui/
```

Your Swagger definition lives here:

```
http://localhost:8080//swagger.json
```

To launch the integration tests, use tox:

```
sudo pip install tox
tox
```

### Running with Docker

To run the server on a Docker container, please execute the following from the
root directory:

```bash
# building the image
docker build -t swagger_server .

# starting up a container
docker run -p 8080:8080 swagger_server
```
