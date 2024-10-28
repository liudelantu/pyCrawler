# =============================================================================
# 程序名: tao_bao.py
# 功能: 获取 淘宝 网站的信息
# 作者: afeng
# 日期: 2024-10-24
# 描述：
#
# 例子：
# =============================================================================

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, executable_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe')
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://www.taobao.com/")

    page.locator('input.search-suggest-combobox-imageSearch-input').fill('美容器')
    with context.expect_page() as new_page_info:
        page.locator('button.btn-search.tb-bg').click()
    new_page = new_page_info.value
    new_page.wait_for_load_state()

    while True:
        pass
    # browser.close()