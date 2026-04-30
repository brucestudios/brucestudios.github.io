import click
import requests
import sys
from typing import Optional, Dict, Any

API_BASE = "https://wttr.in"

def fetch_weather(location: str = "", format: str = "j1") -> Dict[str, Any]:
    """Fetch weather data from wttr.in API."""
    url = f"{API_BASE}/{location}?format={format}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        if format == "j1":
            return response.json()
        else:
            return {"text": response.text}
    except requests.RequestException as e:
        click.echo(f"Error fetching weather data: {e}", err=True)
        sys.exit(1)

@click.group()
@click.version_option(version="0.1.0")
def cli():
    """A simple command-line tool to get current weather and forecasts."""
    pass

@cli.command()
@click.argument("location", required=False, default="")
def current(location: str):
    """Get current weather for a location."""
    data = fetch_weather(location)
    if "text" in data:
        click.echo(data["text"])
    else:
        current_condition = data.get("current_condition", [{}])[0]
        area = data.get("nearest_area", [{}])[0]
        location_name = f"{area.get('areaName',[{}])[0].get('value','')}, {area.get('country',[{}])[0].get('value','')}"
        click.echo(f"Weather for {location_name}:")
        click.echo(f"  {current_condition.get('weatherDesc',[{}])[0].get('value','')}")
        click.echo(f"  Temperature: {current_condition.get('temp_C','')}°C ({current_condition.get('temp_F','')}°F)")
        click.echo(f"  Feels like: {current_condition.get('FeelsLikeC','')}°C ({current_condition.get('FeelsLikeF','')}°F)")
        click.echo(f"  Humidity: {current_condition.get('humidity','')}%")
        click.echo(f"  Wind: {current_condition.get('windspeedKmph','')} km/h {current_condition.get('winddir16Point','')}")

@cli.command()
@click.argument("location", required=False, default="")
@click.option("--days", "-d", default=3, help="Number of days for forecast (1-3).")
def forecast(location: str, days: int):
    """Get weather forecast for a location."""
    if days < 1 or days > 3:
        click.echo("Error: days must be between 1 and 3", err=True)
        sys.exit(1)
    data = fetch_weather(location)
    if "text" in data:
        click.echo(data["text"])
    else:
        area = data.get("nearest_area", [{}])[0]
        location_name = f"{area.get('areaName',[{}])[0].get('value','')}, {area.get('country',[{}])[0].get('value','')}"
        click.echo(f"Forecast for {location_name}:")
        for i, day in enumerate(data.get("weather", [])[:days]):
            date = day.get("date", "")
            click.echo(f"\n{date}:")
            click.echo(f"  {day.get('hourly',[{}])[0].get('weatherDesc',[{}])[0].get('value','')}")
            click.echo(f"  Max temp: {day.get('maxtempC','')}°C ({day.get('maxtempF','')}°F)")
            click.echo(f"  Min temp: {day.get('mintempC','')}°C ({day.get('mintempF','')}°F)")
            click.echo(f"  Avg humidity: {day.get('avghumidity','')}%")

if __name__ == "__main__":
    cli()