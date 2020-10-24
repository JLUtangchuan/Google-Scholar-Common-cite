import time
import selenium
from selenium import webdriver


paperA = "Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization"
paperB = "Dual attention networks for multimodal reasoning and matching"


class GoogleScholarCommon:
    
    def __init__(self, p1, p2, wait_time=120, url="https://scholar.google.com.hk/?hl=zh-CN"):
        self.gs_url = url
        self.paperA = p1
        self.paperB = p2
        self.driver = webdriver.Chrome()
        self.wait_time = wait_time
        

    def isElementExist(self):
        flag=True
        browser=self.driver
        self.driver.implicitly_wait(3)

        try:
            browser.find_element_by_partial_link_text("下一页")
            return flag
        
        except:
            flag=False
            return flag


    def search_cite(self, paper):
        """搜索论文名，返回所有引用的论文名

        """
        li = []
        self.driver.implicitly_wait(self.wait_time)
        self.driver.get(self.gs_url)
        self.driver.find_element_by_xpath('//*[@id="gs_hdr_tsi"]').send_keys(paper)
        self.driver.find_element_by_xpath('//*[@id="gs_hdr_tsb"]').click()
        time.sleep(3)
        byycs_bt = self.driver.find_elements_by_partial_link_text("被引用次数")
        if len(byycs_bt) == 0:
            return []
        byycs_bt[0].click()
        # while 下一页 //*[@id="gs_n"]/center/table/tbody/tr/td[-1]/a/b

        # while self.driver.find_element_by_xpath('//*[@id="gs_n"]/center/table/tbody/tr/td[-1]/a/b'):
        while self.isElementExist():
            self.driver.find_element_by_partial_link_text("下一页").click()
            papers = self.driver.find_elements_by_css_selector('h3>a:nth-child(1)')    
            for i in papers:
                li.append(i.text)
            time.sleep(3)
        # time.sleep(3)
        return li

    def compare_paper(self, l1, l2):
        
        return list(set(l1).intersection(set(l2)))
    
    def go(self):
        
        # 搜索
        listA = self.search_cite(self.paperA)
        print(self.paperA, '被', len(listA), '篇论文引用')
        listB = self.search_cite(self.paperB)

        print(self.paperB, '被', len(listB), '篇论文引用')


        self.driver.quit()
        # 比较
        common_list = self.compare_paper(listA, listB)

        # 显示
        print('Common:')
        print(common_list)
        
        

if __name__ == "__main__":
    gs = GoogleScholarCommon(paperA, paperB)
    gs.go()