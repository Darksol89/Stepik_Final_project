__author__ = 'achubarov', 'ichistov'


class Login(object):
    TITLE_NAME = "PI Expert Online Open Beta VSS Development - Login"
    PIExpertOnlineLink = "https://piexpertonline.power.com/site/login"
    PIExpertWebLink = "http://piexpertweb.vss.spb.ru/site/login/"
    PIExpertCloudLink = "http://piexpertweb.cloudapp.net/"


FAMILY_NAME_DICT = {'InnoSwitch3-CE Flyback': "a[@id='1090']",
                    'InnoSwitch3-CP Flyback': "a[@id='1091']",
                    'InnoSwitch3-EP Flyback': "a[@id='1092']",
                    'InnoSwitch3-Pro Flyback': "a[@id='1102']",
                    'InnoSwitch3-EP 900V Flyback': "a[@id='1106']",

                    'InnoSwitch-CH Flyback': "a[@id='1073']",
                    'InnoSwitch-CE Flyback': "a[@id='1081']",
                    'InnoSwitch-CP Flyback': "a[@id='1078']",
                    'InnoSwitch-EP Flyback': "a[@id='1079']",
                    'InnoSwitch-EP900V Flyback': "a[@id='1089']",

                    'LYTSwitch-0 Buck': "a[@id='1057']",
                    'LYTSwitch-1 Buck': "a[@id='1093']",
                    'LYTSwitch-2 Flyback': "a[@id='1052']",
                    'LYTSwitch-3 Buck': "a[@id='1075']",
                    'LYTSwitch-3 Buck Boost': "a[@id='1076']",
                    'LYTSwitch-3 Isolated Flyback': "a[@id='1080']",
                    'LYTSwitch-3 Non Isolated Flyback': "a[@id='1088']",
                    'LYTSwitch-3 Tapped Buck Boost': "a[@id='1087']",
                    'LYTSwitch-4 Flyback (Low-Line)': "a[@id='1053']",
                    'LYTSwitch-4 Flyback (High-Line)': "a[@id='1058']",
                    'LYTSwitch-4 Buck': "a[@id='1059']",
                    'LYTSwitch-4 Tapped Buck': "a[@id='1060']",
                    'LYTSwitch-5 Buck': "a[@id='1082']",
                    'LYTSwitch-5 Buck Boost': "a[@id='1083']",
                    'LYTSwitch-5 Isolated Flyback': "a[@id='1084']",
                    'LYTSwitch-5 Non Isolated Flyback': "a[@id='1085']",
                    'LYTSwitch-5 Tapped Buck Boost': "a[@id='1086']",
                    'LYTSwitch-7 Buck': "a[@id='1096']",
                    'LYTSwitch-6 Flyback': "a[@id='1200']",


                    'LinkZero-LP Flyback': "a[@id='1042']",
                    'LinkZero-AX Flyback': "a[@id='1041']",

                    'LinkSwitch-HP Flyback': "a[@id='1049']",
                    'LinkSwitch CV Flyback': "a[@id='1033']",
                    'LinkSwitch-3 Flyback': "a[@id='1061']",
                    'LinkSwitch-4 Flyback': "a[@id='1074']",
                    'LinkSwitch-LP Flyback': "a[@id='1016']",
                    'LinkSwitch-XT Flyback': "a[@id='1015']",
                    'LinkSwitch-XT2 Flyback': "a[@id='1099']",

                    'LinkSwitch-PL Flyback': "a[@id='1040']",
                    'LinkSwitch-PL Buck': "a[@id='1047']",
                    'LinkSwitch-PL Boost': "a[@id='1051']",
                    'LinkSwitch-PL Buck Boost': "a[@id='1046']",
                    'LinkSwitch-PL Tapped Buck': "a[@id='1048']",

                    'LinkSwitch-PH Flyback': "a[@id='1036']",
                    'LinkSwitch-PH Buck': "a[@id='1044']",

                    'LinkSwitch-II Flyback': "a[@id='1018']",
                    'LinkSwitch-II Flyback (LNK63X) ': "a[@id='1035']",
                    'LinkSwitch-II Tapped Buck': "a[@id='1019']",

                    'LinkSwitch-TN Flyback': "a[@id='1007']",
                    'LinkSwitch-TN Buck': "a[@id='1004']",
                    'LinkSwitch-TN Buck Boost': "a[@id='1006']",

                    'LinkSwitch-TN2 Flyback': "a[@id='1098']",
                    'LinkSwitch-TN2 Buck': "a[@id='1097']",


                    'TinySwitch-4 Flyback': "a[@id='1050']",
                    'TinySwitch-III Flyback': "a[@id='1009']",

                    'TOPSwitch-JX Flyback': "a[@id='1038']",
                    'TOPSwitch-HX Flyback': "a[@id='1032']",

                    'HiperLCS': "a[@id='1045']",
                    'HiperPFS Boost': "a[@id='1043']",
                    'HiperPFS-2 Boost': "a[@id='1056']",
                    'HiperPFS-3 Boost': "a[@id='1071']",
                    'HiperTFS-2 Forward': "a[@id='1055']",

                    'DPA-Switch Flyback': "a[@id='1025']",
                    'DPA-Switch Forward': "a[@id='1012']"}