"""
NeuroTrader -- 台股量化交易系統
"""
from colorama import init
from neurotrader.utils.system_initialize import Initialize
from neurotrader.utils.user_interface import UserInterface


def main():
    sys_init = Initialize()
    ui = UserInterface()
    init()

    sys_init.initialize_process()
    ui.show_main_menu()
    ui.show_new_feature()
    print()


if __name__ == '__main__':
    main()
