# Download the helper library from https://www.twilio.com/docs/python/install
from dotenv import load_dotenv
import os
from twilio.rest import Client
import csv
import re
import json

load_dotenv()

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
content_sid = os.environ.get('CONTENT_SID')
message_service_id = os.environ.get('MESSAGE_SERVICE_ID')

client = Client(account_sid, auth_token)


def main():

    with open('results.csv', 'w', newline='') as file_csv:
        colums = ["name",
                  "phone",
                  "error_code",
                  "error_message",
                  "sid",
                  "status",
                  "date_sent"]
        writer_csv = csv.DictWriter(file_csv, fieldnames=colums)

        writer_csv.writeheader()

        contacts = get_contacts()
        for contact in contacts:

            response = send_message(contact["phone"], contact["name"])
            writer_csv.writerow({
                "name": contact["name"],
                "phone": contact["phone"],
                "error_code": response["error_code"],
                "error_message": response["error_message"],
                "sid": response["sid"],
                "status": response["status"],
                "date_sent": response["date_sent"]
            })
    print('Proceso completado')


def get_contacts() -> list:
    """Lee el csv de contactos y convierte en un listado de objetos

    Returns:
        list: Una lista de {"name":"nombre", "phone":"573000002233}
    """
    contacts = []
    csv_file_path = "./data/contacts.csv"

    with open(csv_file_path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)
        for row in csv_reader:
            contacts.append({
                "name": row[0],
                "phone": row[1]
            })

    return contacts


def send_message(phone: str, name: str):

    response = {
        "error_code": "",
        "error_message": "",
        "sid": "",
        "status": "",
        "date_sent": "",
    }

    try:
        message = client.messages \
            .create(
                    content_sid=content_sid,
                    from_=message_service_id,
                    to=f'whatsapp:+{phone}',
                    content_variables=json.dumps({
                        'name': name
                    }),
                    )

        response = {
            "error_code": message.error_code,
            "error_message": message.error_message,
            "sid": message.sid,
            "status": message.status,
            "date_sent": message.date_sent,
        }
    except Exception as e:

        patron = re.compile(r'Twilio returned the following information:(.*?)More information may be available here:', re.DOTALL) # noqa: 501

        coincidencias = patron.search(str(e))

        if coincidencias:
            informacion = coincidencias.group(1).strip()
            informacion_sin_saltos = informacion.replace('\n', '')
            response["error_message"] = informacion_sin_saltos
        else:
            print("No se encontró la información.")
            response["error_message"] = "other error"

    return response


if __name__ == "__main__":
    main()
