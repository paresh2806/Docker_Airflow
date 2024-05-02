# Project Name: Airflow Data Pipeline

## Description

Airflow Data Pipeline is a project aimed at demonstrating the setup and usage of Apache Airflow for orchestrating data workflows. This README provides instructions for installing Apache Airflow using Docker and examples of basic usage.

## Problem Statement

![Alt Text](https://github.com/paresh2806/Docker_Airflow/blob/main/images/task_2_overview.png "Apache Airflow Lifecycle")

Imagine you have a task to hit an API endpoint that provides various data in JSON format, including details about upcoming space launches. You use the following command to retrieve the data:
```bash
$ curl -L "https://ll.thespacedevs.com/2.0.0/launch/upcoming"
```

The response contains a list of upcoming launches, each with details such as ID, URL, launch name, scheduled launch time, and associated images.

```bash
{
  "results": [
    {
      "id": "528b72ff-e47e-46a3-b7ad-23b2ffcec2f2",
      "url": "https://.../528b72ff-e47e-46a3-b7ad-23b2ffcec2f2/",
      "launch_library_id": 2103,
      "name": "Falcon 9 Block 5 | NROL-108",
      "net": "2020-12-19T14:00:00Z",
      "window_end": "2020-12-19T17:00:00Z",
      "window_start": "2020-12-19T14:00:00Z",
      "image": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launch_images/falcon2520925_image_20201217060406.jpeg",
      "infographic": ".../falcon2520925_infographic_20201217162942.png"
    },
    ...
  ]
}
```

This task might seem simple, but it's actually composed of three complex sub-tasks. Managing these tasks concurrently could become difficult, especially if one task depends on the output of another. This is where Apache Airflow comes in. It allows you to define dependent tasks as a pipeline and execute them in an orderly manner. Additionally, with Airflow's ability to treat pipelines as code, you can easily manage and version control your data processing workflows.

Your ultimate goal is not just to retrieve this data, but also to notify the API hitter that their task was successful. This means you need to process the JSON response, extract relevant information, and possibly send a notification to the user indicating the successful completion of the task.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Contributing](#contributing)
4. [License](#license)

### Prerequisites
- Docker installed on your machine. You can download Docker from [here](https://www.docker.com/get-started).

## Installation
1. ### Clone Apache Airflow Repository
```bash
git clone https://github.com/paresh2806/Docker_Airflow.git apache-airflow 
```
2. ###(optional) If you are not willing to see examples at boot set parameter 
```
If you are not willing to see examples at boot set parameter AIRFLOW__CORE__LOAD_EXAMPLES: 'true' >> 'false'
```
3. Initialize the database services
```bash
docker-compose up airflow-init 
```
4. Running Airflow
```bash
docker-compose up  
```

5. to cleanup the voluems or Down the container
```bash
docker-compose down -v 
```
- **Username**: `airflow`
- **Password**: `airflow`

![airflow dashboard (http://localhost:8080/)](images\homepage.png)
![airflow dag page (http://localhost:8080/)](images\dag.png)



### Usage
Here there are 2 Examples are stated based on complaxity
example dags can be found in ``/dags`` folder
### 1. Task- 1 (Print Hello From user)
![airflow task_1 (http://localhost:8080/)](https://github.com/paresh2806/Docker_Airflow/blob/main/images/task_1.png)

which genrally prints the statement pre-written by user

![airflow task_1 (http://localhost:8080/)](https://github.com/paresh2806/Docker_Airflow/blob/main/images/task_1_res.png)

### 2. Task -2 (Fetch >> Download >> Notify )

![airflow task_1 (http://localhost:8080/)](https://github.com/paresh2806/Docker_Airflow/blob/main/images/task_2.png)

Over iteraring multiple dag invokes we got certain results    

![airflow task_1 (http://localhost:8080/)](https://github.com/paresh2806/Docker_Airflow/blob/main/images/Capture-3.png)

## Contributing

Your contributions are what make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## License

Information about the project's license and any usage restrictions.
