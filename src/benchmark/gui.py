import tkinter as tk
import tkinter.ttk as ttk
from multiprocessing import Queue, Process
import requests
from enum import Enum
import time
from abc import ABC, abstractmethod

BASE_URL = "http://localhost:7070"


def sendBalance(queue: Queue, count: int) -> None:
    a = {"fromId": "send_test_1", "toId": "send_test_2", "amount": 100.0, "id": 1, "currTimeStamp": 1665620981727,
         "publicKey": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAoiaNsbX2uVEgLarjXvUK2L9ToqH0wmvb4ksJa58dNkox4woq/+0ssbRd+y3Z/+Oq4fVy0sY0omWwc13w5GG6ohCxDh6LkgdtxWX2n4/P2hp1VfX5LnJwZxrc896d6o2fBCxgpSWZEJgQI9Kqy/6jkT/l1/KhcGXTC+a0V0texUUbt1/0175vnhJ5jKcf5OPWBB65UvGAYvoYvuADc5/Dekbo/BxQXba8oWv+og0c/12gkGV60RceHnpP9p1b3om4Djo9u48Z6oF7sDm7NVls3Si+g/X1QpMio+3DrCrfNjEu2XyVfM9WH53vpXVZ88vT1aiaF/k6+vYdCLJ3ETNFnQIDAQAB"}

    b = {"fromId": "send_test_2", "toId": "send_test_1", "amount": 100.0, "id": 1, "currTimeStamp": 1665620982188,
         "publicKey": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAroN9QOhUDCucn7ewEW+VqWUEKmQ41bLGIyIDXRSpW2mtAqCXaPfvmHFSnu+zdH5QCd2v65OhyEDhnuX9Iq4tIhEVDEV2r6rheq7H8IKl6XpRnUzdKDUnSAnFhqLN5sGHqFUX7x2MSN3A8GMN/o0C33XAJNXi5zIIdtvYJ1tUlPPJovDzGED3inlfalOp3vUuV0f0Z7WQaERs/uNIt9aVSfLUXDDvhVhDKT+Q9sB63ep8dEd9rkcVxVVfslqJlwgFmVkqiiOyh1gdgXCKcAZDGn3JZdjnG2UzDsKeN+2lbWq75a2QPSpdhjUFT1CGcMmt4i3Xr7f80+I2v4j6PYLnuwIDAQAB"}

    start = time.time()
    for i in range(count):
        requests.post(BASE_URL + "/send", json=a)
        requests.post(BASE_URL + "/send", json=b)

    end = time.time()
    queue.put("send balance time taken: {} ms".format(
        round((end - start) * 1000) / count))


def getBalance(queue: Queue, count: int) -> None:
    print("get balance")
    start = time.time()
    payload = {"accountId": "get_balance_test", "id": 120, "currTimeStamp": 1665619888613, "publicKey": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxIKl8Er55y/+7LJWbacVMfP4k+BF7iXlWO5bQBlb5P3BrvmXPOVMq87dncmPOQVgZ5DUKZMVveNabdM+iC74x9bgtkG/UCVj5kE24vpJqYnHYt1j6oHtY1bWSp/UlSd4fSbeIKSQkZQEjVHrDseDDEnet2eHp8BKJrHOs7wGVUK8WPuwo3G1CbeWb7FYGZlUeag/ScdsuHIUIf5Ab59FWhPBewfw+bLy93fy5QkueqfMwqy2jVJymkhJVhbbRruEjbMAAW7SiW63HrVTnsvhIDelUmZsK2OFGiGSxRI5RWtULWWSY+MBR73nLmWsx+YbUFeFVb2vGVaJL3dqVmdF6wIDAQAB",
               "signature": "grBuRiK80UmDtwup/Mti4SrIzvN0Qo/54H9f/TSMEdiSRE4t0DweNCE3H0vupI7yv5OZpXkYs4k0lRHP8E/+hEfT7y/riSSMG60BeBnIX+45IeES2z69UiY7sIkEB+YdFF/B5wJZkwlngW6pDMNGVi+TbXm9PXxHXcG16jHiIzthxfv9ctrN16YM/153Z/jw46dsvKo/qE+at9Sp78+KEzMeIwMLgVdOZlB1JduB4IAzJkp34hUqLIB1ypO/WhuVRNidP1MJB01OTt2Uwa7YxVtFtpb//u0f9vTvxYJ+OyY+kXCVyfAp6CzReRf6CoDOdMPRvg1FTf4S0obcmRSIEw\u003d\u003d"}

    for i in range(count):
        requests.post(BASE_URL + "/get-balance", json=payload)

    end = time.time()
    queue.put("get balance time taken: {} ms".format(
        round((end - start) * 1000) / count))


class BenchmarkFrame(ABC, ttk.Frame):
    @abstractmethod
    def sendRequest(self, count: int):
        pass

    def __init__(self, master: tk.Tk, queue: Queue, **kw):
        super().__init__(master=master, **kw)
        self.queue = queue

        self.controllerFrame = ttk.Frame(master=self)

        # count label and text box
        self.countFrame = ttk.Frame(
            master=self.controllerFrame)
        self.countLabel = ttk.Label(
            master=self.countFrame, text="count", anchor=tk.CENTER)
        self.countTextbox = tk.Text(master=self.countFrame, height=1)

        # start button to send request to server
        self.startButton = ttk.Button(
            master=self.controllerFrame, text='start', command=self._on_start)

        # for displaying time taken for server response
        self.resultTextbox = tk.Text(master=self)

        self.countLabel.pack(side=tk.LEFT)
        self.countTextbox.pack(side=tk.LEFT, expand=True, fill=tk.X)

        self.countFrame.pack(side=tk.TOP, fill=tk.X)
        self.startButton.pack(side=tk.TOP, expand=True, fill=tk.X)

        self.controllerFrame.pack(side=tk.TOP, fill=tk.X)
        self.resultTextbox.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        self.pack(expand=True, fill=tk.BOTH)

    def _on_start(self):
        self.startButton["state"] = "disabled"
        try:
            count = int(self.countTextbox.get('1.0', 'end-1c'))
            self.sendRequest(count)
        except Exception as ex:
            self._insert_display("{}".format(ex))
            self.enable_start_button()

    def enable_start_button(self):
        print("enable start button")
        self.startButton["state"] = "enabled"

    def runQueueTask(self):
        try:
            while True:
                result = self.queue.get_nowait()
                self._insert_display(result)
                self.enable_start_button()
        except:
            pass
        finally:
            self.after(1000, self.runQueueTask)

    def _insert_display(self, text: str):
        self.resultTextbox.insert('1.0', text + '\n')


class GetBalanceFrame(BenchmarkFrame):
    def __init__(self, master: tk.Tk, queue: Queue, **kw):
        super().__init__(master, queue, **kw)

    def sendRequest(self, count):
        Process(target=getBalance, args=[self.queue, count]).start()


class SendFrame(BenchmarkFrame):
    def __init__(self, master: tk.Tk, queue: Queue, **kw):
        super().__init__(master, queue, **kw)

    def sendRequest(self, count: int):
        sendBalance(self.queue, count)


if __name__ == "__main__":
    window = tk.Tk()
    window.title('Benchmark')

    notebook = ttk.Notebook(window)
    notebook.pack(pady=10, expand=True, fill=tk.BOTH)

    sendBalanceQueue = Queue()
    sendBalanceBenchmarkFrame = SendFrame(
        master=notebook, queue=sendBalanceQueue)
    window.after(1000, sendBalanceBenchmarkFrame.runQueueTask)

    getBalanceQueue = Queue()
    getBalanceBenchmarkFrame = GetBalanceFrame(
        master=notebook, queue=getBalanceQueue)
    window.after(1000, getBalanceBenchmarkFrame.runQueueTask)

    notebook.add(sendBalanceBenchmarkFrame, text='Send Balance')
    notebook.add(getBalanceBenchmarkFrame, text='Get Balance')
    window.mainloop()
