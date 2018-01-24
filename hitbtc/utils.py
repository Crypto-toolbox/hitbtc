"""
Message templates to log when handling responses to requests that are SUCCESFUL.
Failed requests are logged using the error code contained in the response and its related message.
"""
resp_get_currency = '{currency}:\n' \
               '\t{fullName}({id}):' \
               '\tIs a cryptocurrency: {crypto}\n' \
               '\tDeposits available: {payinEnabled}\n' \
               '\tpayinPaymentId available: {payinPaymentId}\n' \
               '\tRequired confirmations on deposit: {payinConfirmations}\n' \
               '\tWithdrawals available: {payoutEnabled}\n' \
               '\tpayoutIsPaymentId available: {payoutIsPaymentId}\n' \
               '\tTransfers enabled: {transferEnabled}\n'

resp_get_currencies = '{fullname}({id}):' \
                 '\tIs a cryptocurrency: {crypto}\n' \
                 '\tDeposits available: {payinEnabled}\n' \
                 '\tpayinPaymentId available: {payinPaymentId}\n' \
                 '\tRequired confirmations on deposit: {payinConfirmations}\n' \
                 '\tWithdrawals available: {payoutEnabled}\n' \
                 '\tpayoutIsPaymentId available: {payoutIsPaymentId}\n' \
                 '\tTransfers enabled: {transferEnabled}\n'

resp_get_symbol = '{id}:\n' \
             '\tBase currency: {baseCurrency}\n' \
             '\tQuote currency: {quoteCurrency}\n' \
             '\tMinimum quantity increment: {quantityIncrement}\n' \
             '\tTick size: {tickSize}\n' \
             '\tMaker fee: {takeLiquidityRate}\n' \
             '\tTaker fee: {provideLiquidityRate}\n' \
             '\tFee currency: {feeCurrency}\n'

resp_get_symbols = '{id}:\n' \
              '\tBase currency: {baseCurrency}\n' \
              '\tQuote currency: {quoteCurrency}\n' \
              '\tMinimum quantity increment: {quantityIncrement}\n' \
              '\tTick size: {tickSize}\n' \
              '\tMaker fee: {takeLiquidityRate}\n' \
              '\tTaker fee: {provideLiquidityRate}\n' \
              '\tFee currency: {feeCurrency}\n'

resp_get_trades = 'Trade ID ({id}):' \
             '\tPrice: {price}\n' \
             '\tSize: {quantity}\n' \
             '\tSide: {side}\n' \
             '\tTimestamp: {timestamp}\n'


order_report_template = 'Trade ID ({id}): \tStatus: {status}\n' \
              'Order type: {type}' \
              '\t\tPrice: {price}' \
              '\t\tSize: {quantity}\n' \
              'Side: {side}\t' \
              '\t\tCumulative size: {cumQuantity}' \
              '\t\t\tTime in Force: {timeInForce}\n' \
              'Created at: {createdAt}' \
              '\t\t\t\t\tUpdated at: {updatedAt}\n' \
              'Client Order ID: {clientOrderId}' \
              '\t\t\t\tReport type: {reportType}'

original_request_clOrdID = 'Original Request Client Order ID: {originalRequestClientOrderId}'

resp_get_active_orders = order_report_template + original_request_clOrdID + '\n'


resp_get_trading_balance = 'Wallet: {currency}' \
                      '\t\tAvailable: {available}' \
                      '\t\tReserved: {reserved}\n'

resp_place_order = 'Successfully placed a new order via websocket!\n' + order_report_template + '\n'

resp_cancel_order = 'Successfully cancelled an order via websocket!\n' + order_report_template+ '\n'

resp_cancel_replace_order = 'Successfully replaced an order via websocket!\n' + order_report_template + original_request_clOrdID + '\n'

resp_subscribe_ticker = 'Succesfully subscribed to {symbol} ticker data!'
resp_subscribe_book = 'Succesfully subscribed to {symbol} order book data!'
resp_subscribe_trades = 'Succesfully subscribed to {symbol} trade data!'
resp_subscribe_candles = 'Succesfully subscribed to {symbol} candle data!'
resp_subscribe_reports = 'Succesfully subscribed to account reports!'
resp_login = 'Successfully logged in!'

response_types = {'getCurrency': resp_get_currency, 'getCurrencies': resp_get_currencies,
                  'getSymbol': resp_get_symbol, 'getSymbols': resp_get_symbols,
                  'getTrades': resp_get_trades,
                  'getOrders': resp_get_active_orders,
                  'getTradingBalance': resp_get_trading_balance,
                  'subscribeTicker': resp_subscribe_ticker,
                  'subscribeOrderbook': resp_subscribe_book,
                  'subscribeTrades': resp_subscribe_trades,
                  'subscribeCandles': resp_subscribe_candles,
                  'subscribeReports': resp_subscribe_reports,
                  'newOrder': resp_place_order, 'cancelOrder': resp_cancel_order,
                  'cancelReplaceOrder': resp_cancel_replace_order,
                  'login' : resp_login}
