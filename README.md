# Auto-Connect to Wi-Fi with Captive Portal Login

## Overview

This Python script automates the process of connecting to a Wi-Fi network that redirects to a login page (captive portal). It continuously checks for internet connectivity and, if not connected, attempts to log in to the captive portal using the provided credentials.

## Prerequisites

- Python 3.x
- `requests` library
- `subprocess` library

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/yourrepository.git
    ```

2. Navigate to the project directory:

    ```bash
    cd yourrepository
    ```

3. Create a `credentials.txt` file in the project directory and add your login credentials in the following format:

    ```
    Your_Registration_Number
    Your_Password
    ```

## Usage

Run the Python script using the following command:

```bash
python auto_connect_wifi.py
