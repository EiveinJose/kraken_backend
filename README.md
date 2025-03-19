# Kraken Backend Challenge - Meter Reading Importer
===================================================

## Overview
This Django project imports and processes **D0010 flow files**, which contain electricity meter readings.  
The system allows support staff to search for readings based on **MPAN** (Meter Point Administration Number) or **Meter Serial Number**.

## Project Structure

kraken_backend/
├── manage.py
├── readings/
│   ├── management/
│   │   ├── commands/
│   │   │   ├── import_d0010.py
│   ├── models.py
│   ├── admin.py
│   ├── views.py
├── kraken_backend/
│   ├── settings.py
│   ├── urls.py
├── db.sqlite3
├── requirements.txt
├── README.md

##  Setup Instructions

### 1. **Clone the Repository**

	git clone https://github.com/your-username/kraken-backend.git
	cd kraken-backend

###2. Create a Virtual Environment

	python -m venv venv
	source venv/bin/activate  # Mac/Linux
	venv\Scripts\activate  # Windows

3. Install Dependencies

	pip install -r requirements.txt

4. Apply Migrations

	python manage.py migrate

5. Create a Superuser (For Admin Panel)

	python manage.py createsuperuser

6. Run the Development Server

	python manage.py runserver

Access it at: http://127.0.0.1:8000/admin/


##Import a D0010 File

1.Ensure a sample D0010 file exists in your project folder.

2.Run the following command:

	python manage.py import_d0010 sample_d0010.txt

3.Imported readings will be available in the Django Admin Panel.


##Features

-Import and process D0010 files containing electricity meter readings.

-Admin Panel to search readings by MPAN or Meter Serial Number.

-Django Models to store and manage imported readings.


##Running Tests

To run unit tests, execute:

	python manage.py test readings


Author

EIVEIN JOSE

