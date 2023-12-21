# Connecticut College Computer Science Career Site

This project is a comprehensive career resource website developed specifically for the Connecticut College Computer Science department. It aims to centralize various career resources, facilitating students in exploring career options, preparing for interviews, and connecting with alumni.

## Description

The site offers a range of features to enhance student engagement, success in the field, and employability. It includes resources like interview preparation materials, connections to alumni, job and internship listings, and more.

## Technologies

- **Python/Django**: Versatile, powerful, and readable web framework.
- **JavaScript**: For dynamic and interactive client-side scripting.
- **HTML**: Structured and accessible markup language.
- **MySQL**: Robust, high-performance database system.
- **CSS**: Responsive and stylish designs.
- **cPanel**: For scalable and easy deployment.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- MySQL
- A virtual environment (recommended)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/LemsonMureya/CS-Career-Site.git
    ```
2. Navigate to the project directory:
    ```bash
    cd careerSite
    ```

### Setting Up a Virtual Environment

Create and activate a virtual environment to isolate the project dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

## Installing Dependencies
Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Running the Application

Run the application:
```bash
python manage.py runserver
```

Make migrations and migrate the database when you make any changes to the database:
```bash
python manage.py makemigrations
python manage.py migrate
```

Creating an Admin User
To access the admin panel and manage the application:

```bash
python manage.py createsuperuser
Follow the prompts to create an admin user.
```

## Usage
After starting the server, visit http://127.0.0.1:8000/ in your web browser to access the application.

## Contributing
We welcome contributions! Please read our contributing guidelines to get started.

Project Link: https://github.com/LemsonMureya/CS-Career-Site
