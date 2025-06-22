import asyncio
import os
from lib.lib import Main
from DrissionPage import Chromium, ChromiumOptions


async def main():
    lib = Main()
    co = ChromiumOptions()
    co.auto_port().mute(True).incognito(True)

    print("Checking for updates...")
    await lib.checkUpdate()

    while True:
        browserPath = input(
            "\033[1m"
            "\n(RECOMMENDED) Press enter in order to use the default browser path (If you have Chrome installed)"
            "\033[0m"
            "\nIf you prefer to use other Chromium browser other than Chrome, please enter its executable path here. (e.g: C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe)"
            "\nHere are some supported browsers that are tested and able to use:"
            "\n- Chrome Browser"
            "\n- Brave Browser"
            "\nBrowser executable path: "
        ).replace('"', "").replace("'", "")
        if browserPath != "":
            if os.path.exists(browserPath):
                co.set_browser_path(browserPath)
                break
            else:
                print("Please enter a valid path.")
        else:
            break

    proxyUsage = input(
        "\nWould you like to use a proxy?\nPlease enter the proxy IP and port in the format of IP:PORT (Example: http://localhost:1080). Press enter to skip.\nProxy: "
    )
    if proxyUsage != "":
        if lib.testProxy(proxyUsage)[0] is True:
            co.set_proxy(proxyUsage)
        else:
            print(lib.testProxy(proxyUsage)[1])

    chrome = Chromium(addr_or_opts=co)
    page = chrome.latest_tab
    page.set.window.max()
    page.get("https://mattround.com/usvsth3m/1000-seconds/")
    page.ele('#button').wait.displayed(timeout=15)
    buttonEle = page.ele('#button')
    await asyncio.sleep(3)
    page.actions.hold(buttonEle)
    await asyncio.sleep(1005)
    page.actions.release(buttonEle)
    await asyncio.sleep(5)
    score = page.run_js("return document.getElementById('score').innerText")
    print(f'Score: {score}')
    page.get_screenshot(path='./screenshots', name='1000seconds.png', full_page=True)
    page.close()

if __name__ == "__main__":
    asyncio.run(main())
