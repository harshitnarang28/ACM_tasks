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
    git clone https://github.com/harshitnarang28/ACM_tasks
    ```

2. Navigate to the project directory:

    ```bash
    cd ACM_tasks
    ```

3. Create a `credentials.txt` file in the project directory and add your login credentials in the following format:

    ```
    Your_Registration_Number
    Your_Password
    ```

## Usage

Run the Python script using the following command:

```bash
python auto_login.py

```

## Code Explanation

### `get_browser(website)`

This function checks for internet connectivity by pinging a specified website (`www.google.com`). If the website is reachable, it returns `True`; otherwise, it returns `False`.

### `getlogin_credentials()`

This function reads login credentials from the `credentials.txt` file. It attempts to open the file and read the first two lines, which are assumed to be the registration number and password, respectively.

### `login_to_portal(reg_no, password)`

This function performs the login operation to the captive portal using the provided credentials. It constructs a dictionary containing the user ID (`reg_no`), password (`password`), and other necessary form data. Then, it sends a POST request to the login URL (`login_link`) with this data.

- If the login is successful (HTTP status code 200), it prints a success message.
- If the credentials are invalid (HTTP status code 401), it prints an "Invalid credentials" message.
- For any other errors, it prints an "Unknown error" message.

## Troubleshooting

- If you encounter any issues with the script, please ensure that the `credentials.txt` file is correctly formatted and contains valid credentials.
- Ensure that the Wi-Fi network you are connecting to redirects to a login page (captive portal).
