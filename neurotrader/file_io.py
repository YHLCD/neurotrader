import os
from os import mkdir

from neurotrader.portfolio import Stock, Portfolio

"""持股資料檔案讀寫"""


class PortfolioFileIO:
    def __init__(self, filepath='./data/portfolio.txt'):  # 從檔案讀取資料
        self.filepath = filepath

    def load_from_file(self):
        """
               從檔案讀取持股
               檔案格式（CSV）：
               stock_code,name,quantity,cost_price,buy_date
               2330,台積電,10,950,2024-01-15
               2454,聯發科,5,850,2024-02-20
        """
        portfolio = Portfolio()
        if not os.path.exists(self.filepath) or os.path.getsize(self.filepath) == 0:
            print('持股檔案不存在：', self.filepath)
            print('將建立空投資組合')
            return portfolio
        with open(self.filepath, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, start=1):
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                try:
                    parts = line.split(',')
                    if len(parts) != 5:
                        print(f'第{line_num}行格式有誤，跳過')
                        continue
                    stock = Stock(stock_code=parts[0].strip(),
                                  name=parts[1].strip(),
                                  quantity=parts[2].strip(),
                                  cost_price=parts[3].strip(),
                                  buy_date=parts[4].strip()
                                  )
                    portfolio.add_stock(stock)
                except (ValueError, IndexError) as e:
                    print(f'第 {line_num}行解析失敗：{e}')
        print(f'載入 {len(portfolio.stocks)} 檔持股')
        return portfolio

    def save_to_file(self, portfolio):
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)  # 確保"資料夾"存在
        with open(self.filepath, 'w', encoding='utf-8') as f:
            f.write('# NeuroTrader Portfolio\n')
            f.write('# 格式：股票代號,名稱,張數,成本價,買入日期')
            f.write('\n')
            for stock in portfolio.stocks.values():
                f.write(f'{stock.stock_code},{stock.name},{stock.quantity},{stock.cost_price},{stock.buy_date}\n')
        print(f"✓ 儲存 {len(portfolio.stocks)} 檔持股")
        
    # 未來預計變成 load_portfolio_from database，這裡不使用API更新的原因，
    # 是因為有些券商不一定有API，這樣的話持股就採取手動輸入的方式，更新到資料庫內，每次打開程式就到資料庫裡面找有哪些股票就可。
    # 若要即時股價就交給爬蟲或其他API執行
