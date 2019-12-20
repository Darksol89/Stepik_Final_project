from selenium.webdriver.common.by import By

__author__ = 'achubarov', 'ichistov'


def field_by_p_name_locator_generator(text):
    """
    Return locator of <input> siblinged with <p> containing *text*

    :type text: str
    :return: tuple
    """

    return By.XPATH, '//label[contains(text(), "{name}")]/../input'.format(name=text)

def field_by_select_name_locator_generator(text):
    """
        Return locator of <select> siblinged with <label> containing *text*

        :type text: str
        :return: tuple
        """

    return By.XPATH, '//label[contains(text(), "{name}")]/../select/options[@selected]'.format(name=text)

def field_by_report_table_locator_generator(text):
    """
        Return locator of <input> siblinged with <td> containing *text*

        :type text: str
        :return: tuple
        """

    return By.XPATH, '//td[contains(text(), "{name}")]/../td/input'.format(name=text)


def component_field_locator_generator(component, field):
    """
    Return locator for *field* of some *component*

    :type component: str
    :type field: str
    :return: tuple
    """

    return By.XPATH, '(//table//p[contains(text(), "{name}")]/../../following-sibling::*' \
                     '//p[contains(text(), "{change_name}")]/../../td[2]/p|' \
                     '//table//p[contains(text(), "{name}")]/../following-sibling::*' \
                     '//p[contains(text(), "{change_name}")]/../../td[3]/p)[1]'.format(
                         name=component,
                         change_name=field)


def simple_component_field_locator_generator(component, index):
    """
    Return locator of field of simple (only one parameter) component (with horizontal *index*)

    :type component: str
    :type index: int
    :return: tuple
    """

    return By.XPATH, '//p[contains(text(), "{name}")]/../../td[{index}]/p'.format(name=component, index=index)


def table_cell_locator(row, column):
    """
    Get locator from PIXls table by row and column.

    :type row: int
    :type column: int
    """

    return By.XPATH, "//div[@class='pixls']/table/tbody/tr[{row}]/td[{column}]".format(row=row, column=column)


def design_dialog_locator(dialog_family, sub_dialog):
    """
    Get locator for PIExpert's dialog.

    :type dialog_family: str
    :type sub_dialog: str
    """

    return By.XPATH, "//span[contains(text(), '{dialog_family}')]/..//a[contains(text(), '{sub_dialog}')]".format(
        dialog_family=dialog_family, sub_dialog=sub_dialog)

def schematic_dialog_locator(dialog_family, sub_dialog):
    """
    Get locator for PIExpert's dialog.

    :type dialog_family: str
    :type sub_dialog: str
    """

    return By.XPATH, "//div[@varid='', '{dialog_family}']/..//a[contains(text(), '{sub_dialog}')]".format(
        dialog_family=dialog_family, sub_dialog=sub_dialog)
