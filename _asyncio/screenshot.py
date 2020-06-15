"""
 Created by liwei on 2020/6/14.
"""
import asyncio
from pyppeteer import launch


def screen_size():
    """使用tkinter获取屏幕大小"""
    import tkinter
    tk = tkinter.Tk()
    width = tk.winfo_screenwidth()
    height = tk.winfo_screenheight()
    tk.quit()
    return width, height


async def main():
    browser = await launch()
    page = await browser.newPage()
    width, height = screen_size()
    await page.setViewport({  # 最大化窗口
        "width": width,
        "height": height
    })
    await page.goto('http://www.baidu.com/')
    await page.screenshot({'path': '/Users/zipee/Downloads/screenshot.png'})
    await browser.close()


asyncio.run(main())
