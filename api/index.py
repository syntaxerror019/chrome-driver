from flask import Flask, render_template
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # URL of the JSON data
    url = "https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json"

    # Fetch the JSON data
    response = requests.get(url)
    data = response.json()

    # Extract values to populate the table
    table_data = []
    for version in data['versions']:
        version_info = {
            'version': version['version'],
            'platforms': []
        }
        for download in version['downloads']['chrome']:
            platform_info = {
                'platform': download['platform'],
                'url': download['url']
            }
            version_info['platforms'].append(platform_info)
        table_data.append(version_info)

    # Render the HTML template with the table data
    return render_template('index.html', table_data=table_data)
