import Locators
import Family_Name
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class MainMenuPage(BasePage):
    """
    Special class for all actions on the Main Menu page
    """

    def create_pixls_design(self, family):
        """
        Create PIXls design
        """
        # Click New Design button
        self.click(self.browser, Locators.IndexPage.NEW_DESIGN)
        self.waiting_loading_element(self.browser)
        # Web driver selecting family name from list
        self.click(self.browser, (By.XPATH, ''.join(['//', Family_Name.FAMILY_NAME_DICT[family]])), sleep_time=2)
        self.waiting_loading_element(self.browser)
        # Click PIXLs button
        self.click(self.browser, Locators.DesignCreation.PIXLS)
        self.waiting_loading_element(self.browser)

    def create_piexpert_design_with_pdp(self, family, pdp=20, optimization=False):
        """
        Create design with PDP parameter
        """
        self.click(self.browser, Locators.IndexPage.NEW_DESIGN)
        self.waiting_loading_element(self.browser)
        # Web driver selecting family name from list
        self.click(self.browser, (By.XPATH, ''.join(['//', Family_Name.FAMILY_NAME_DICT[family]])), sleep_time=2)
        self.waiting_loading_element(self.browser)
        # Click PIExpert button
        self.click(self.browser, Locators.DesignCreation.PIEXPERT)
        self.waiting_loading_element(self.browser)
        # Next -> Next to PDP page
        self.click(self.browser, Locators.DesignWizardPages.NEXT_PAGE_1)
        self.waiting_loading_element(self.browser)
        self.click(self.browser, Locators.DesignWizardPages.NEXT_PAGE_2)
        self.waiting_loading_element(self.browser)
        # Set PDP value
        pdp_field = self.browser.find_element(*Locators.DesignWizardPages.PDP_FIELD)
        pdp_field.send_keys(str(pdp))
        pdp_field.send_keys(Keys.ENTER)
        self.waiting_loading_element(self.browser)
        # Next -> Finish
        self.click(self.browser, Locators.DesignWizardPages.NEXT_OUTPUTS_PDP)
        self.waiting_loading_element(self.browser)
        self.click(self.browser, Locators.DesignWizardPages.FINISH_BUTTON)
        self.waiting_loading_element(self.browser)
        # Optimization yes or no
        if optimization:
            self.click(self.browser, Locators.SolutionFilter.SOL_FILTER_OK)
            self.waiting_loading_element(self.browser)
            self.click(self.browser, Locators.SolutionFilter.SOL_TOP_OK)
            self.waiting_loading_element(self.browser)
        else:
            self.click(self.browser, Locators.SolutionFilter.SOL_FILTER_CANCEL)
            self.waiting_loading_element(self.browser)



    def should_be_index_in_link_page(self):
        assert 'Index' in self.browser.current_url, "Design isn't created"

    def should_be_smth(self):
        pass