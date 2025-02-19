# Health Tracking App

A web-based health tracking application built with Django, designed for monitoring daily weight, basal body temperature, and menstrual cycle. The app provides an intuitive interface for data entry and visualization through interactive charts.

## Features

- **Daily Health Tracking**: Log weight, basal body temperature, and menstrual cycle status.
- **Interactive Charts**: Visualize trends over time using Chart.js.
- **Mobile-Friendly Design**: Optimized UI for various screen sizes.
- **Admin Controls**: Easily delete records from a dedicated management interface.
- **Secure Data Handling**: Built with Django’s security best practices.

## Technologies Used

- **Backend**: Django
- **Frontend**: Bootstrap, Chart.js, AJAX
- **Database**: SQLite
- **Deployment**: Local (Linux server)

## Installation

To set up the project locally:

```bash
# Clone the repository
git clone https://github.com/MagUsagi/health_tracker.git
cd health-tracker

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

## Usage

1. Navigate to `http://127.0.0.1:8000/` in your browser.
2. Enter health data using the form.
3. View trends through interactive charts.
4. Manage records via the database page.

## Demo

![App Demo](demo.gif)

## Future Enhancements

- User authentication for personalized tracking
- Cloud-based deployment (AWS, Render)
- Export data as CSV/PDF
- AJAX-Powered Navigation: Smooth month transitions without full-page reloads.


## Contact

For inquiries or contributions, feel free to connect via [LinkedIn](https://www.linkedin.com/in/akane-klauenboesch/) or check out more projects on [GitHub](https://github.com/MagUsagi/).

