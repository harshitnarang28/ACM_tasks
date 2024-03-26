import requests
import subprocess
import time

web_browser = "www.google.com"
creds_file = "credentials.txt"
login_link = "https://phc.prontonetworks.com/cgi-bin/authlogin?URI=http://captive.apple.com/hotspot-detect.html"

def get_browser(website):
    try:
        subprocess.check_output(['ping', '-q', '-c', '1', website], stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError:
        return False
def getlogin_credentials():
    try:
        with open(creds_file, "r") as file:
            reg_no = file.readline().strip()
            password = file.readline().strip()
    except Exception as e:
        print(f"Error reading credentials file: {e}")
        return '', ''
    return reg_no, password


 
def login_to_portal(reg_no, password):
    info = {
        "userId": reg_no,
        "password": password,
        "Submit22": "Login",
        "serviceName": "ProntoAuthentication"
        }
    try:
        response = requests.post(login_link, data=info, verify=False)
        if response.ok:           
            print("You are now connected to the VIT wifi. You can now freely browse the internet.")
        elif response.status_code == 401:
            print("Invalid credentials")
        else:
            print("Login failed, unknown error")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to the portal: {e}")

def main():
    user_id, password = getlogin_credentials()
    while True:
        if get_browser(web_browser):
            time.sleep(15)
        else:
            login_to_portal(user_id, password)
            time.sleep(5)

if __name__ == "__main__":
    main()