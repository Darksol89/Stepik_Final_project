__author__ = 'achubarov', 'ichistov'

from selenium.webdriver.common.by import By

class Errors(object):
    ERROR_OK = (By.ID, 'OKdlgCancelPIEEE')
    ERROR_TEXT = (By.ID, 'dlgPIEEE')
    ERROR_YES = (By.ID, 'YESdlgCancelPIEEE')
    ERROR_NO = (By.ID, 'NOdlgCancelPIEEE')
    ERROR_HELP = (By.ID, 'PIEEE_help_1694')

class SetPointButtons(object):
    ADD = (By.ID, 'outAddBtn_rem')
    REMOVE = (By.ID, 'outRemBtn_rem')
    EDIT = (By.ID, 'outEdtBtn_rem')

class Login():
    LOGIN_FIELD = (By.ID, 'username-field')
    PASSWORD_FIELD = (By.ID, "password-field")
    SUBMIT_LOGIN = (By.ID, 'login-submit-btn')
    ERROR_MESSAGE = (By.ID, 'LoginForm_password_em_')

    CONTINUE_LOGIN = (By.ID, 'dlg-continue')
    CANCEL_LOGIN = (By.ID, 'dlg-cancel')

    REGISTER = (By.XPATH, "//div[@class = 'authorizationBlock']/a[text() = 'Register']")


class Logout:
    LOGOUT = (By.XPATH, "//div[@class = 'authorizationBlock']/a[text() = 'Logout']")


class Localization(object):
    RUS_LANGUAGE = (By.XPATH, "//a[@href='ru']")
    ENG_LANGUAGE = (By.XPATH, "//a[@href='/site/login?_lang=en']")


class IndexPage(object):
    PRODUCT_SELECTOR_GUIDE = (By.CLASS_NAME, "psgLink")
    NEW_DESIGN = (By.CLASS_NAME, "npwLink")
    OPEN_DESIGN = (By.CLASS_NAME, 'openDesignLink')
    PREFERENCES = (By.CLASS_NAME, 'prefLink')


class FileManager(object):
    SELECT_ALL = (By.ID, 'fileManagerTable_c0_all')
    DELETE = (By.XPATH, "//button[@class='designBrwsrBtn deleteBtn']")
    DOWNLOAD = (By.XPATH, "//button[@class='designBrwsrBtn downloadBtn']")
    DIALOG_SUBMIT = (By.CLASS_NAME, 'dialog-submit')
    NO_RESULTS = (By.XPATH, "//span[@class='empty']")

    class Navigation:
        PREVIOUS = (By.XPATH, "//div[@class='pager']//li[@class='previous']")
        NEXT = (By.XPATH, "//div[@class='pager']//li[@class='next']")
        NEXT_HIDDEN = (By.XPATH, "//div[@class='pager']//li[@class='next hidden']")

    class Sort:
        BY_NAME = (By.XPATH, "//table[@class='items']//a[contains(@href, 'sort=Name')]")
        BY_MODIFIED = (By.XPATH, "//table[@class='items']//a[contains(@href, 'sort=IsChanged')]")
        BY_TYPE = (By.XPATH, "//table[@class='items']//a[contains(@href, 'sort=typeLabel')]")
        BY_DATE = (By.XPATH, "//table[@class='items']//a[contains(@href, 'sort=ModificationDate')]")
        BY_SIZE = (By.XPATH, "//table[@class='items']//a[contains(@href, 'sort=FileSize')]")


class DesignCreation(object):
    PIXLS = (By.ID, "dlgXls201")
    PIEXPERT = (By.ID, "dlgExpert201")
    CANCEL = (By.ID, 'dlgCancel201')


class DesignMenu(object):
    FILE = (By.XPATH, "//div[@id='mainMbMenu']//span")
    FILE_NEW = (By.XPATH, "//span[text()='New	']")
    FILE_PRODUCT_SELECTOR_GUIDE = (By.XPATH, "//span[text()='Product Selector Guide	']")
    FILE_FILE_MANAGER = (By.XPATH, "//span[text()='File Manager']")
    FILE_CLOSE = (By.XPATH, "//a[@id='mainMenuClose']")
    FILE_SAVE = (By.XPATH, "//span[text()='Save	']")
    FILE_SAVE_AS = (By.XPATH, "//span[text()='Save As…']")
    FILE_EXPORT = (By.XPATH, "//div[@id='mainMbMenu']//li//li[@class='parent']")
    FILE_EXPORT_TO_EXCEL = (By.XPATH, "//a[@id='mainMenuExportXLS']")
    FILE_EXPORT_TO_PDF = (By.XPATH, "//a[@id='mainMenuExportPDF']")
    FILE_EXPORT_TO_RTF = (By.XPATH, "//a[@id='mainMenuExportRTF']")
    FILE_EXPORT_FOR_ALL_TO_PDF = (By.XPATH, "//a[@id='mainMenuExportAllPDF']")
    FILE_PRINT = (By.XPATH, "//span[text()='Print...	']")

    TOOLS = (By.XPATH, "//span[text()='Tools']")
    TOOLS_GOAL_SEEK = (By.XPATH, "//span[text()='Goal Seek...']")
    TOOLS_GOAL_SEEK = (By.XPATH, "//span[text()='Goal Seek...']")

    EDIT = (By.XPATH, "//span[text()='Edit']")
    EDIT_UNDO = (By.XPATH, "//span[text()='Undo	']")
    EDIT_REDO = (By.XPATH, "//span[text()='Redo	']")

    class CloseDialog(object):
        YES_BUTTON = (By.CLASS_NAME, 'dialog-submit')
        NO_BUTTON = (By.CLASS_NAME, 'dialog-cancel')
        HELP_BUTTON = (By.ID, 'Help_PIE_Introduction')

    class GoalSeek(object):
        PARAMETER_NAME_TO_SET = (By.XPATH, "//select[@id='1']")
        PARAMETER_TARGET_VALUE = (By.XPATH, "//input[@id='2']")
        BY_PARAMETER_NAME = (By.XPATH, "//select[@id='3']")

        DIALOG_OK = (By.ID, 'dlgOK180')
        DIALOG_CANCEL = (By.ID, 'dlgCancel180')
        DIALOG_HELP = (By.ID, 'Help_PIE_dlgGoalSeek')

class DesignTabs(object):
    SCHEMATIC = (By.XPATH, '//a[@href="#tab1"]')
    DESIGN_RESULTS = (By.XPATH, '//a[@href="#tab2"]')
    BOARD_LAYOUT = (By.XPATH, '//a[@href="#tab3"]')
    BOM = (By.XPATH, '//a[@href="#tab4"]')
    TRANSFORMER_CONSTRUCTION = (By.XPATH, '//a[@href="#tab5"]')


class Bom(object):

    class Upload(object):
        FILE_INPUT = (By.ID, 'bom_file')
        UPLOAD_BUTTON = (By.ID, 'upload_btn')
        HELP_BUTTON = (By.ID, 'submitH')

    class StartPage(object):
        START_BUTTON = (By.CLASS_NAME, 'startbutton')

    class DesignPage(object):
        DIGIKEY = (By.XPATH, "//img[contains(@src, 'digikey_logo2.jpg')]")
        MOUSER = (By.XPATH, "//img[contains(@src, 'mouser-reg-logo.gif')]")
        DIGIKEY_DISABLED = (By.XPATH, "//img[contains(@src, 'digikey_logo2_disabled.jpg')]")
        MOUSER_DISABLED = (By.XPATH, "//img[contains(@src, 'mouser-reg-logo-disabled.png')]")

        DIGIKEY_CHECKBOX = (By.NAME, "Checkbox0")
        MOUSER_CHECKBOX = (By.NAME, "Checkbox3")

        PI_BOM = (By.XPATH, "//div[@id='tab4']/*/tr[/td[contains(., 'Power Integrations')]]")

class NavTree(object):
    SPEC_INPUT = (By.XPATH, '//span[contains(text(), "Specification")]/..//a[contains(text(), "Input")]')
    SPEC_OUTPUT = (By.XPATH, '//span[contains(text(), "Specification")]/..//a[contains(text(), "Output")]')
    SPEC_SAF_TERM = (By.XPATH, '//span[contains(text(), "Specification")]/..//a[contains(text(), "Safety and Thermal")]')
    STACKING = (By.XPATH, '//span[contains(text(), "Specification")]/..//a[contains(text(), "Stacking")]')


    DESIGN_OPTIONS = (By.XPATH, '//span[contains(text(), "Design")]/..//a[contains(text(), "Options")]')
    KEY_PARAM = (By.XPATH, '//span[contains(text(), "Design")]/..//a[contains(text(), "Key Parameters")]')

    RECTIFIER_FUSE = (By.XPATH, '//span[contains(text(), "Input Section")]/..//a[contains(text(), "Rectifier, Fuse, Surge")]')

    UV_OV = (By.XPATH, '//span[contains(text(), "PI Device")]/..//a[contains(text(), "UV/OV")]')
    HEATSINK = (By.XPATH, '//span[contains(text(), "PI Device")]/..//a[contains(text(), "Heatsink")]')
    OUTPUT_OVP = (By.XPATH, '//span[contains(text(), "PI Device")]/..//a[contains(text(), "Output OVP")]')

    PRIMARY_AND_BIAS = (By.XPATH, '//span[contains(text(), "Winding Construction")]/..//a[contains(text(), "Primary and Bias")]')
    SHIELDS = (By.XPATH, '//span[contains(text(), "Winding Construction")]/..//a[contains(text(), "Shields")]')
    PIN_ALLOCATION = (By.XPATH, '//span[contains(text(), "Winding Construction")]/..//a[contains(text(), "Pin Allocation")]')

    RBIAS = (By.XPATH, '//span[contains(text(), "Primary BIAS")]/..//a[contains(text(), "RBIAS circuit components")]')
    DIODE_AND_RECTIFIERS = (By.XPATH, '//span[contains(text(), "Output Stage")]/..//a[contains(text(), "Diodes and Rectifiers")]')
    BUS_SWITCH = (By.XPATH, '//span[contains(text(), "Output Stage")]/..//a[contains(text(), "Bus Switch")]')

    FEEDBACK = (By.XPATH, '//span[contains(text(), "Feedback")]/..//a[contains(text(), "Components")]')
    FEEDBACK_BIAS = (By.XPATH, '//span[contains(text(), "Feedback")]/..//a[contains(text(), "Bias")]')
    CLAMP = (By.XPATH, '//span[contains(text(), "Clamp")]/..//a[contains(text(), "Components")]')

    DESIGN_DEFAULTS = (By.XPATH, '//span[contains(text(), "Design Settings")]/..//a[contains(text(), "Defaults")]')