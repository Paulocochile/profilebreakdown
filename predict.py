from google.cloud import automl_v1beta1 as automl


import csv

# You must first create a dataset, using the `eu` endpoint, before you can
# call other operations such as: list, get, import, delete, etc.
client_options = {'api_endpoint': 'eu-automl.googleapis.com:443'}


project_location = f"projects/profilebreakdown/locations/eu"


project_id = "profilebreakdown"
model_id = "TCN7649583869414342656"
content = "Coronavirus will be solved very soon, no more people will die"

prediction_client = automl.PredictionServiceClient(client_options=client_options)

# Get the full path of the model.
model_full_id = "projects/1047356004045/locations/eu/models/TCN7649583869414342656"

# Supported mime_types: 'text/plain', 'text/html'
# https://cloud.google.com/automl/docs/reference/rpc/google.cloud.automl.v1#textsnippet


        
def my_function():
    text_snippet = automl.TextSnippet(
        content=content, mime_type="text/plain"
    )
    payload = automl.ExamplePayload(text_snippet=text_snippet)

    response = prediction_client.predict(name=model_full_id, payload=payload)

    for annotation_payload in response.payload:
        if annotation_payload.classification.score>0.5:
            row.append(annotation_payload.display_name)
    writer.writerow(row)
        
with open('test.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    writer = csv.writer(open('output.csv', 'w'))
    for row in spamreader:
        print(', '.join(row))
        content = row[0]
        my_function()
