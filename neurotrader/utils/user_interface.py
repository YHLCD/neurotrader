from colorama import Fore, Style


class UserInterface:
    def __init__(self):
        pass

    def print_banner(self):  # 歡迎畫面
        print('=' * 60)
        print(Fore.CYAN + 'NeuroTrader -- 台股量化交易系統' + Style.RESET_ALL)
        print('=' * 60)
        print()

    def show_main_menu(self):
        """main menu"""
        print('=' * 60)
        print('Main Menu')
        print('=' * 60)
        print('1.持股管理')
        print('2.市場掃描')
        print('3.策略總覽')
        print('4.策略回測')
        print('5.設定')
        print('0.離開')

    def show_new_feature(self):
        print(Fore.YELLOW + 'New Feature Under Development' + Style.RESET_ALL)
