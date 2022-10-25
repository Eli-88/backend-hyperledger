import requests
import time

BASE_URL = "http://localhost:7070"


def createAccount():
    payload = {"accountId": "get_balance_test", "initialAmount": 10000.2, "id": 1, "currTimeStamp": 1665621755716,
               "publicKey": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqb7GUiMf2UbOSZ2GHfeVNHLlOm3t5BKZWamFXc1GwPeBrXL/L4kN9FWKqHwOPjCAmqnDc8l4midP1RjJ6saCZvWppe48568bNHuXbXxiYahJpy2GebUx6efnDHI31XkkkXkBLvsar3RCporoKEe3gaUjVi+NRKyFanQ/oeUt8q9p9bvPJCUouvywmGMlWMuj3Ks6ihbf7GXNskRDSCNGPF57KPKs2O2AcdLyslotwO6ayurt8nwyYob8x8nZJ9XR4e9QtYP2qyo7guRtqR1qXX97HUlOivIUOv3IMSWlQlzJSM+DR4+p+i0ncGJdHCIkEYSpC26AKQ0/9zsd8YByDwIDAQAB"}
    requests.post(url=BASE_URL + "/register", json=payload)


if __name__ == '__main__':
    payload = {"accountId": "get_balance_test", "id": 120, "currTimeStamp": 1665619888613, "publicKey": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxIKl8Er55y/+7LJWbacVMfP4k+BF7iXlWO5bQBlb5P3BrvmXPOVMq87dncmPOQVgZ5DUKZMVveNabdM+iC74x9bgtkG/UCVj5kE24vpJqYnHYt1j6oHtY1bWSp/UlSd4fSbeIKSQkZQEjVHrDseDDEnet2eHp8BKJrHOs7wGVUK8WPuwo3G1CbeWb7FYGZlUeag/ScdsuHIUIf5Ab59FWhPBewfw+bLy93fy5QkueqfMwqy2jVJymkhJVhbbRruEjbMAAW7SiW63HrVTnsvhIDelUmZsK2OFGiGSxRI5RWtULWWSY+MBR73nLmWsx+YbUFeFVb2vGVaJL3dqVmdF6wIDAQAB",
               "signature": "grBuRiK80UmDtwup/Mti4SrIzvN0Qo/54H9f/TSMEdiSRE4t0DweNCE3H0vupI7yv5OZpXkYs4k0lRHP8E/+hEfT7y/riSSMG60BeBnIX+45IeES2z69UiY7sIkEB+YdFF/B5wJZkwlngW6pDMNGVi+TbXm9PXxHXcG16jHiIzthxfv9ctrN16YM/153Z/jw46dsvKo/qE+at9Sp78+KEzMeIwMLgVdOZlB1JduB4IAzJkp34hUqLIB1ypO/WhuVRNidP1MJB01OTt2Uwa7YxVtFtpb//u0f9vTvxYJ+OyY+kXCVyfAp6CzReRf6CoDOdMPRvg1FTf4S0obcmRSIEw\u003d\u003d"}
    count = 1000
    start = time.time()
    for i in range(count):
        response = requests.post(BASE_URL + "/get-balance", json=payload)

    end = time.time()
    print("time taken: {} ms".format(round((end - start) * 1000) / count))
