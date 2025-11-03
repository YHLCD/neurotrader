import os, sys
from neurotrader.utils.user_interface import UserInterface

from colorama import Fore, Style
from tabulate import tabulate


class Initialize:
    def __init__(self):
        pass

    def initialize_process(self):
        """
        initialize environment...
        """
        UserInterface.print_banner(self)
        if not self.check_dependencies():
            sys.exit(1)
        self.verify_directories()
        self.demo_display()
        print(Fore.CYAN + 'Initialize complete.' + Style.RESET_ALL)
        print()

    def check_dependencies(self):
        """check environment"""
        print('checking dependencies...')

        required_packages = [
            ('pandas', None),
            ('numpy', None),
            ('requests', None),
            ('FinMind.data', 'DataLoader'),
            ('tabulate', None),
            ('colorama', None),
            ('tqdm', None),
            ('dotenv', 'load_dotenv'),

        ]
        all_ok = True

        for package_info in required_packages:
            package_name = package_info[0]
            try:
                if package_info[1]:
                    exec(f"from {package_name} import {package_info[1]}")
                else:
                    exec(f"import {package_name}")
                print(f" ✓ {package_name}")
            except ImportError:
                print(Fore.RED + f" ✗ {package_name} 未安裝" + Style.RESET_ALL)
                all_ok = False

        if all_ok:
            print(Fore.GREEN + " ✓ 所有依賴套件正常" + Style.RESET_ALL)
            print()
        else:
            print(Fore.RED + " ✗ 部分套件未安裝" + Style.RESET_ALL)
            print("請執行：pip install -r requirements.txt")

        return all_ok

    def verify_directories(self):
        """
        checking directories existence
        """
        print('checking directories existence...')

        required_dirs = ['cache', 'output', 'logs', 'data']

        for dir_name in required_dirs:
            if not os.path.exists(dir_name):
                print(f"{dir_name}/ 不存在，正在建立...")
                os.makedirs(dir_name)
            else:
                print(f" ✓ {dir_name}/")

        print(Fore.GREEN + " ✓ 資料夾結構正常" + Style.RESET_ALL)

    def demo_display(self):
        """
        初始化檢查：示範顯示功能
        確認表格和顏色能正常顯示
        """
        print()
        print(" 測試顯示功能...")
        print()

        # 示範表格
        data = [
            ['2330', '台積電', 1015, Fore.RED + '+5.2%' + Style.RESET_ALL],
            ['2454', '聯發科', 890, Fore.RED + '+4.8%' + Style.RESET_ALL],
            ['2317', '鴻海', 108, Fore.GREEN + '-1.2%' + Style.RESET_ALL]
        ]

        print(tabulate(
            data,
            headers=['代號', '名稱', '價格', '漲跌幅'],
            tablefmt='grid'
        ))

        print(Fore.GREEN + " 顯示功能正常" + Style.RESET_ALL)
        print()
