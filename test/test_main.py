from main.main import max_profit

def test_stock_price_combo():
    prices = [7, 1, 5, 3, 6, 4]
    
    result = max_profit(prices)
    
    assert result == 7

def test_stock_price_sell_at_the_end():
    
    prices = [1, 2, 3, 4, 5]
    
    result = max_profit(prices)
    
    assert result == 4
    
def test_no_profit():
    
    prices = [7, 6, 4, 3, 1]
    
    result = max_profit(prices)
    
    assert result == 0

def test_check_profit():
    
    prices = [7, 8, 9, 4, 3, 1]
    
    result = max_profit(prices)
    
    assert result == 2