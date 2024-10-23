# =============================================================================
# 程序名: shi_xi_seng.py
# 功能: 获取 实习僧求职网站的信息
# 作者: afeng
# 日期: 2024-10-23
# 描述：
#
# 例子：
# =============================================================================

from playwright.sync_api import sync_playwright
import asyncio

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, executable_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe')
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://www.shixiseng.com/")
    page.locator('input.nonal').fill('python')
    with context.expect_page() as new_page_info:
        page.locator('input.form--button').click()
    new_page = new_page_info.value
    new_page.wait_for_load_state()

    # 最后页码数字
    page_btn = new_page.locator('li.number')
    pages = int(page_btn.nth(page_btn.count() - 1).text_content())

    # 32次翻页动作
    for i in range(pages - 1):
        print(f'正在获取{i+1}页的数据.....')
        new_page.wait_for_selector('a.title.ellipsis.font')  # 等待页面上的所有a.title.ellipsis.font完全加载
        job_des = new_page.locator('a.title.ellipsis.font')
        job_cnt = job_des.count()

        for i in range(job_cnt):
            detail_url = job_des.nth(i).get_attribute('href')
            detail_page = context.new_page()
            detail_page.goto(detail_url)

            job_name = detail_page.locator('div.new_job_name span').text_content()
            job_ptime = detail_page.locator('div.job_date span.cutom_font').text_content()
            job_salary = detail_page.locator('span.job_money').text_content()
            job_position = detail_page.locator('span.job_position').text_content()
            job_academic = detail_page.locator('span.job_academic').text_content()
            job_week = detail_page.locator('span.job_week').text_content()
            job_times = detail_page.locator('span.job_time').all_text_contents()
            combined_job_time = '+'.join(job_times)
            job_good_list = detail_page.locator('div.job_good_list').text_content()
            job_detail = detail_page.locator('div.job_detail').text_content()

            print(job_name, job_ptime, job_salary, job_position, job_academic, job_week, combined_job_time, job_good_list)
            detail_page.close()
        new_page.wait_for_selector('button.btn-next')
        new_page.locator('button.btn-next').click()
    
    while True:
        pass
    browser.close()