import sys
import requests

def get_weather(location=None):
    base_url = "http://wttr.in"
    params = {
        'format': '%l:+%C+%t+%w+%h+%p\n',  # Location: Condition temperature wind humidity precipitation
    }
    if location:
        url = f"{base_url}/{location}"
    else:
        url = base_url
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException as e:
        return f"Error fetching weather data: {e}"

def main():
    location = sys.argv[1] if len(sys.argv) > 1 else None
    print(get_weather(location))

if __name__ == "__main__":
    main()