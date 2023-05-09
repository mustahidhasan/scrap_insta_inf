import os
import csv
import time
from selenium.webdriver.common.by import By
from driver_setup import DriverSetup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
"""
InstagramInfluencer class.



"""
class InstagramInfluencer:
    def __init__(self, keyword, url):
        """
        Initialize the InstagramInfluencer class.

        Parameters:
        keyword (str): The keyword as link to be searched.
        """
        # initialize variables to be used in the class
        self.keyword = keyword
        self.driver = None
        # set the URL to be opened by the web driver
        self.url = url

    def init_driver(self):
        """
        Initialize the web driver.

        Returns:
        None
        """
        try:
            print(self.url)
            driver_setup = DriverSetup(self.url)
            driver_setup.init_driver_local_chrome()
            self.driver = driver_setup.driver
        except Exception as e:
            print(f"Error initializing the driver: {e}")
            self.close_driver()
            raise e
    
    def login(self):
       """
         Login the Instagram with the credential.

       """
       try:
        self.driver.get(self.url)
        time.sleep(5)

        get_user_name = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
        get_user_name.send_keys("mustahidhasan9@gmail.com")
        time.sleep(5)

        get_password = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
        get_password.send_keys("19171518-Sagor")

        get_login_btn = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]")
        get_login_btn.click()
        time.sleep(5)
       except Exception as e:
              print(f"Error login the Instagram: {e}")
              self.close_driver()
              raise e
       
    def search_influencer(self):
        try:
            # get the search box
            print("into the search influencer")
            time.sleep(5)
            # clieck not now
            click_not_now = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div")
            click_not_now.click()
            time.sleep(5)


            # click notification not now
            click_notification_not_now = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
            click_notification_not_now.click()
            time.sleep(10)

            # get the search option not working
            click_search_option = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]")
            self.driver.execute_script("arguments[0].scrollIntoView();", click_search_option)
            click_search_option.click()
            time.sleep(5)

            #get the search box & search the influencer
            get_search_box = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input")
            get_search_box.send_keys(self.keyword) 
            time.sleep(5)
            get_search_box.send_keys(Keys.ENTER)
            time.sleep(2)
            get_search_box.send_keys(Keys.ENTER)


            time.sleep(50)
            #click the search option
            # click_search_option.click()
            
        except Exception as e:
            print(f"Error search the influencer: {e}")
            self.close_driver()
            raise e
    def close_driver(self):
        """
        Close the web driver.

        Returns:
        None
        """
        self.driver.quit()

    def run(self):
        """
        Run the Instagram influencer information.. 

        Returns:
        None
        """
        self.init_driver()
        self.login()
        self.search_influencer()
        print(f"{self.keyword} done")
        # self.close_driver()

# get the Instagram influencer information from command.py and app.py file
def get_insta_inf_info(url, keyword_item, func):
    """
    Get the Instagram influencer information.

    Parameters:
    url (str): The URL to be searched.
    keyword_item (str): The keyword to be searched.
    func (str): The function to be called.

    Returns:
    None
    """
    # print("linee 174", keyword_item, url, func)

    # initialize the InstagramInfluencer class
    insta_info_info = InstagramInfluencer(keyword_item,url)
    # run the InstagramInfluencer script
    try:
        insta_info_info.run()
    except Exception as e:
        print(f"Error running the Instagram script: {e}")
        insta_info_info.close_driver()
        raise e




