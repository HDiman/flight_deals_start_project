headers = {
    "Authorization": "Bearer " + AUTH_TOKEN,
}

body = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories,
    }
}

response_new_row_sheet = requests.post(url=NEW_ROW_SHEET_ENDPOINT, json=body, headers=headers)