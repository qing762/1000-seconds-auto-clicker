import requests
import sys


class Main():
    async def checkUpdate(self):
        try:
            resp = requests.get(
                "https://api.github.com/repos/qing762/1000-seconds-auto-clicker/releases/latest"
            )
            latestVer = resp.json()["tag_name"]

            if getattr(sys, 'frozen', False):
                import version  # type: ignore
                currentVer = version.__version__
            else:
                with open("version.txt", "r") as file:
                    currentVer = file.read().strip()

            if currentVer < latestVer:
                print(f"Update available: {latestVer} (Current version: {currentVer})\nYou can download the latest version from: https://github.com/qing762/1000-seconds-auto-clicker/releases/latest")
                return currentVer
            else:
                print(f"You are running the latest version: {currentVer}")
                return currentVer
        except Exception as e:
            print(f"An error occurred: {e}")
            return currentVer

    def testProxy(self, proxy):
        try:
            response = requests.get("http://www.google.com", proxies={"http": proxy, "https": proxy}, timeout=5)
            return True, response.status_code
        except Exception:
            return False, "Proxy test failed! Please ensure that the proxy is working correctly. Skipping proxy usage..."


if __name__ == "__main__":
    print("This is a library file. Please run main.py instead.")
