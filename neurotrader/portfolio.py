"""
這邊要有什麼功能：與持有股票相關的東西都會放這
1-1從資料庫(目前還不會資料庫，所以用.txt檔案代替)讀取使用者持有的股票資訊，
如：持有股票標的、數量、購入價格、該標的目前價位、目前持有該標的盈虧等等，有關所持有股票的相關訊息。
這部份是要在程式打開的同時(initialize)，就要去資料庫裡面找數據(目前是從.txt檔裡面讀取)
1-2持有標的一覽表頁面，目前暫定放在這裡(show_menu()的1.持股管理)
1-3買入、賣出股票後，可以手動更新持股資料(日後若有券商API可以自動更新)。

"""
# 第一步：建立資料結構'

class Stock:  # 單一個股
    def __init__(self, stock_code, name, quantity, cost_price, buy_date):
        self.stock_code = stock_code
        self.name = name
        self.quantity = quantity
        self.cost_price = cost_price
        self.buy_date = buy_date
        self.current_price = 0 #收盤價，有即時報價數據時才是現在當下的價格

    def get_profit_loss(self):  # 計算損益
        return (self.current_price - self.cost_price) * self.quantity * 1000

    def get_profit_loss_percentage(self):
        if self.cost_price == 0:
            return 0
        return (self.current_price - self.cost_price) / self.cost_price * 100


class Portfolio:  # 投資組合
    def __init__(self):
        self.stocks = {}
        """
            stock = {
                {stock_code: Stock}
            }
            """

    def add_stock(self, stock):
        self.stocks[stock.stock_code] = stock

    def get_total_value(self):  # 總市值
        return sum(s.current_price * s.quantity * 1000 for s in self.stocks.values())

    def get_total_cost(self):  # 總成本
        return sum(s.cost_price * s.quantity * 1000 for s in self.stocks.values())

    def total_profit_loss(self):  # 總損益
        return self.get_total_value() - self.get_total_cost()
