from prefect import Client
import prefect
from prefect.utilities.exceptions import ClientError

client = Client(api_token="i_K-XUdHypXSw8HhrdwdVA")
try:
    client.create_project("boilerplate")
except prefect.utilities.exceptions.ClientError as ex:
    print(ex.args[0][0]["message"])
except Exception:
    raise
