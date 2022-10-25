import requests
import time

BASE_URL = "http://localhost:7070"


def createAccount():
    a = {"accountId": "send_test_1", "initialAmount": 12435.24, "id": 1, "currTimeStamp": 1665621993181,
                      "publicKey": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA5+J1C+VOUVFzxj22VeJtAAPpqrIKTWDBHSUyiVboReSyjE0RT1REd6FLv9eOecn1fq2paAvWg6/rnh2P35GrcNw1BImHs1WIWcQrjKN24e9lHcyCZNBbalF/LRp+AjnXm0zdzpN5euT0vKEVaTyEkVsrp1iN46w0ONVRyQaHTxSHOF9uMJagN9jD/9SFpFsN/KuS6qlpN/msW8WECv7f/KsgpsooHtYBVV4O+f92Wp8Mz66/wyWLDo6+AVukuZ3YTKNzFDMGI8qBFnxG0jVcxn9XtIk7SCZljvv8ae2BWxSXUDBJ9b/uXBI923ASXHfGmU+zsUaFXSQbUtGJ+usPXwIDAQAB"}
    b = {"accountId": "send_test_2", "initialAmount": 12435.24, "id": 1, "currTimeStamp": 1665621993475,
                      "publicKey": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvsMaAa3I3lcuF/WeWpY7U7mevKPbs+hE++y2TGEI6hPnaMU78EqimH1qzAY5LEjEdtPanSO0a9z50vL9EBX5cuDTbEKWr+e2z1UBtV50wCiB78W39GOPpD/V96FLQ2AnSY+W+5lhlT0lM4+c6s42TRGcfq/ijjY5CcqjdjLuoKOHN1mA6hig4CgumKRdz+YIkXVl+JZfi7MU8GkPMoUpfa2aFDHHSsEKvE87aoK6pmG4PJ3cf/GxAM/e52OE2xgyCZRe7CYuGIO4Lal9XbuMa8o8y2cRVuzLMQt6t+pW6LEpLfBzSwPu3SQPAsUk4dmijyTFK4xUzjfhYOwBUT3ALwIDAQAB"}

    requests.post(BASE_URL + "/register", a)
    requests.post(BASE_URL + "/register", b)


if __name__ == '__main__':
    a = {"fromId": "send_test_1", "toId": "send_test_2", "amount": 100.0, "id": 1, "currTimeStamp": 1665620981727,
         "publicKey": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAoiaNsbX2uVEgLarjXvUK2L9ToqH0wmvb4ksJa58dNkox4woq/+0ssbRd+y3Z/+Oq4fVy0sY0omWwc13w5GG6ohCxDh6LkgdtxWX2n4/P2hp1VfX5LnJwZxrc896d6o2fBCxgpSWZEJgQI9Kqy/6jkT/l1/KhcGXTC+a0V0texUUbt1/0175vnhJ5jKcf5OPWBB65UvGAYvoYvuADc5/Dekbo/BxQXba8oWv+og0c/12gkGV60RceHnpP9p1b3om4Djo9u48Z6oF7sDm7NVls3Si+g/X1QpMio+3DrCrfNjEu2XyVfM9WH53vpXVZ88vT1aiaF/k6+vYdCLJ3ETNFnQIDAQAB"}

    b = {"fromId": "send_test_2", "toId": "send_test_1", "amount": 100.0, "id": 1, "currTimeStamp": 1665620982188,
         "publicKey": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAroN9QOhUDCucn7ewEW+VqWUEKmQ41bLGIyIDXRSpW2mtAqCXaPfvmHFSnu+zdH5QCd2v65OhyEDhnuX9Iq4tIhEVDEV2r6rheq7H8IKl6XpRnUzdKDUnSAnFhqLN5sGHqFUX7x2MSN3A8GMN/o0C33XAJNXi5zIIdtvYJ1tUlPPJovDzGED3inlfalOp3vUuV0f0Z7WQaERs/uNIt9aVSfLUXDDvhVhDKT+Q9sB63ep8dEd9rkcVxVVfslqJlwgFmVkqiiOyh1gdgXCKcAZDGn3JZdjnG2UzDsKeN+2lbWq75a2QPSpdhjUFT1CGcMmt4i3Xr7f80+I2v4j6PYLnuwIDAQAB"}

    count = 1000
    start = time.time()
    for i in range(count):
        requests.post(BASE_URL + "/send", json=a)
        requests.post(BASE_URL + "/send", json=b)

    end = time.time()
    print("time taken: {} ms".format(round((end - start) * 1000) / count))
