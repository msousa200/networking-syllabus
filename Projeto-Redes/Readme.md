Web Application with NGINX, Flask, and Docker

This project is a secure and scalable web application built using Flask and Docker, with NGINX as the load balancer and reverse proxy. The application provides a simple task list with basic CRUD (Create, Read, Update, Delete) operations. The communication is secured using HTTPS with a self-signed SSL certificate.
Objective

The goal of the project is to:

    Develop a web application that demonstrates the ability to handle network configurations, security, and load balancing.
    Implement a REST API that handles CRUD operations for managing tasks.
    Ensure high availability through load balancing with NGINX and use Docker for containerization.

Table of Contents

    Features
    Architecture
    Requirements
    Setup
    Usage
    API Endpoints
    Security
    Contributions

Features

    NGINX Load Balancer: Handles SSL termination and forwards requests to the Flask app.
    Task Management API: REST API with endpoints for CRUD operations on tasks.
    Secure Communication: All communication with the web application is secured using HTTPS.
    Dockerized Application: The application and its services are containerized using Docker.

Project Structure

Here is the structure of the project:

.
├── app
│   ├── app.py
│   ├── requirements.txt
│   └── templates
│       └── index.html
├── certs
│   ├── server.crt
│   └── server.key
├── docker-compose.yml
├── Dockerfile
├── nginx.conf
└── README.md

    app/: Contains the Flask application code and templates.
        app.py: The main Flask application with the task management API.
        requirements.txt: Lists the Python dependencies for the Flask application.
        templates/index.html: The HTML template for the task list UI.

    certs/: Contains the SSL certificate and key files for HTTPS.
        server.crt: The self-signed SSL certificate.
        server.key: The private key for the SSL certificate.

    docker-compose.yml: Defines the multi-container setup for the app, NGINX, and other services.

    Dockerfile: Contains instructions for building the Flask application image.

    nginx.conf: The NGINX configuration file for setting up SSL and reverse proxy.

    README.md: This file.

Requirements

    Docker: Ensure Docker and Docker Compose are installed on your machine.
    SSL Certificate: A self-signed SSL certificate (server.crt and server.key) is included for HTTPS communication.

Setup

    Clone the repository:

git clone <repository-url>
cd <repository-folder>

Build and start the containers:

Build and start the application using Docker Compose:

docker-compose up --build

This command will build the application images and start the containers defined in docker-compose.yml.

Access the application:

Once the containers are up and running, you can access the application at:

    https://localhost

    The application will be available via HTTPS on port 443.

Usage

The web application provides a simple task list with the ability to add, edit, and delete tasks.
Adding a Task

    Navigate to the web page and enter a task in the input field.
    Click on the "Add" button to add a new task.

Viewing Tasks

    The list of tasks is displayed on the main page.

Editing a Task

    Click on the "Edit" link next to a task to change its name.

Deleting a Task

    Click on the "Delete" link next to a task to remove it.

API Endpoints
1. GET /api/tasks

    Description: Fetch all tasks.

    Response: A JSON array of tasks.

    Example:

    {
      "tasks": [
        { "id": 0, "task": "Task 1" },
        { "id": 1, "task": "Task 2" }
      ]
    }

2. POST /api/tasks

    Description: Create a new task.

    Request Body: JSON object with the task name.

    Example:

{ "task": "New Task" }

Response: JSON object containing the newly created task's ID and name.

Example:

    { "id": 2, "task": "New Task" }

3. PUT /api/tasks/<task_id>

    Description: Update an existing task.

    Request Body: JSON object with the updated task name.

    Example:

    { "task": "Updated Task" }

    Response: JSON object containing the updated task.

4. DELETE /api/tasks/<task_id>

    Description: Delete a task by its ID.

    Response: JSON object containing the deleted task.

    Example:

    { "task": "Task to Delete" }

Security

This application uses SSL/TLS to encrypt communication. The SSL certificates (server.crt and server.key) are self-signed for local development purposes. For production use, it is recommended to replace the self-signed certificate with a trusted certificate from a Certificate Authority (CA).

The NGINX configuration file is set up to:

    Listen on port 443 (HTTPS).
    Forward traffic to the Flask app securely using SSL termination.

SSL Configuration

The NGINX configuration file (nginx.conf) contains the necessary SSL/TLS settings:

server {
    listen 443 ssl;
    server_name app.com;

    ssl_certificate /etc/nginx/certs/server.crt;
    ssl_certificate_key /etc/nginx/certs/server.key;

    location / {
        proxy_pass http://app;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
