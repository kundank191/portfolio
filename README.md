# Project Name: README.md

## Description
This project is a Flask-based web application that serves as a portfolio website and offers some utility features. It provides information about the developer's projects and articles, allows users to connect with the developer, offers PDF cropping functionality, and enables users to update calendar events with alarms.

## Prerequisites
Before running this project, ensure you have the following prerequisites:
- Python 3.11.5
- Flask
- MongoDB
- Required Python libraries (Flask, mongoengine, etc.)

## Installation
1. Clone the repository to your local machine.

   ```bash
   git clone https://github.com/kundank191/portfolio.git
   ```

2. Change into the project directory.

   ```bash
   cd portfolio
   ```

3. Create a virtual environment (optional but recommended).

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment (if created).

   - **Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **macOS and Linux:**

     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies.

   ```bash
   pip install -r requirements.txt
   ```

6. Set up the MongoDB database by providing the `MONGO_URI` environment variable.

   ```bash
   export MONGO_URI="mongodb://username:password@localhost:27017/your-database"
   ```

   Replace `"username"`, `"password"`, `"localhost"`, `"27017"`, and `"your-database"` with your MongoDB configuration.

## Usage
1. Run the Flask application.

   ```bash
   python app.py
   ```

   The application will be accessible at `https://kundan.me/`.

2. Access the following routes:
   - `/`: This is the homepage that displays information about the developer's projects and articles.
   - `/connect_with_me`: Allows users to connect with the developer by providing their name, email, phone, and a message.
   - `/projects/calendar_optimization`: Displays the calendar optimization page.
   - `/projects/crop_pdf`: Displays the PDF cropping page.
   
3. Use the web application to explore its features.

## Features
- **Homepage**: Provides information about the developer's projects and articles.
- **Connect with Me**: Users can submit their contact details and a message to connect with the developer.
- **Calendar Optimization**: Access the calendar optimization page.
- **PDF Cropping**: Upload a PDF file, specify cropping parameters, and receive a cropped PDF as the output.
- **Update Calendar**: Upload a file to update calendar events with alarms.

## Contributions
Contributions to this project are welcome. Feel free to open issues and pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments
- Flask
- MongoDB
- Python libraries used in the project
- flat icon for icons
- unsplash for the images
- mobirise for the html templates
