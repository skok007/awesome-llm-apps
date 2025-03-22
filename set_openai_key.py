import os

def set_openai_key():
    try:
        with open('.openai_key', 'r') as file:
            api_key = file.read().strip()
            os.environ['OPENAI_API_KEY'] = api_key
            print("Successfully set OPENAI_API_KEY environment variable")
    except FileNotFoundError:
        print("Error: .openai_key file not found in root directory")
    except Exception as e:
        print(f"Error setting environment variable: {e}")

if __name__ == "__main__":
    set_openai_key() 