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

resp_get_active_orders = 'Trade ID ({id}):' \
                    '\tOrder type: {type}\n' \
                    '\tStatus: {status}\n' \
                    '\tPrice: {price}\n' \
                    '\tSize: {quantity}\n' \
                    '\tSide: {side}\n' \
                    '\tCumulative size: {cumQunatity}\n' \
                    '\tTime in Force: {timeInForce}\n' \
                    '\tCreated at: {timestamp}\n' \
                    '\tUpdated at: {timestamp}\n' \
                    '\tClient Order ID: {clientOrderId}\n' \
                    '\tOriginal Request Client Order ID: {originalRequestClientOrderId}\n' \
                    '\tReport type: {reportType}\n'

resp_get_trading_balance = 'Wallet: {currency}\n' \
                      '\tAvailable: {available}\n' \
                      '\tReserved: {reserved}\n'

resp_place_order = 'Successfully placed a new order via websocket!\n' \
              '\tTrade ID ({id}):' \
              '\t\tOrder type: {type}\n' \
              '\t\tStatus: {status}\n' \
              '\t\tPrice: {price}\n' \
              '\t\tSize: {quantity}\n' \
              '\t\tSide: {side}\n' \
              '\t\tCumulative size: {cumQunatity}\n' \
              '\t\tTime in Force: {timeInForce}\n' \
              '\t\tCreated at: {timestamp}\n' \
              '\t\tUpdated at: {timestamp}\n' \
              '\t\tClient Order ID: {clientOrderId}\n' \
              '\t\tReport type: {reportType}\n'

resp_cancel_order = 'Successfully cancelled an order via websocket!\n' \
              '\tTrade ID ({id}):' \
              '\t\tOrder type: {type}\n' \
              '\t\tStatus: {status}\n' \
              '\t\tPrice: {price}\n' \
              '\t\tSize: {quantity}\n' \
              '\t\tSide: {side}\n' \
              '\t\tCumulative size: {cumQunatity}\n' \
              '\t\tTime in Force: {timeInForce}\n' \
              '\t\tCreated at: {timestamp}\n' \
              '\t\tUpdated at: {timestamp}\n' \
              '\t\tClient Order ID: {clientOrderId}\n' \
              '\t\tReport type: {reportType}\n'

resp_cancel_replace_order = 'Successfully replaced an order via websocket!\n' \
                       '\tTrade ID ({id}):' \
                       '\t\tOrder type: {type}\n' \
                       '\t\tStatus: {status}\n' \
                       '\t\tPrice: {price}\n' \
                       '\t\tSize: {quantity}\n' \
                       '\t\tSide: {side}\n' \
                       '\t\tCumulative size: {cumQunatity}\n' \
                       '\t\tTime in Force: {timeInForce}\n' \
                       '\t\tCreated at: {timestamp}\n' \
                       '\t\tUpdated at: {timestamp}\n' \
                       '\t\tClient Order ID: {clientOrderId}\n' \
                       '\t\tOriginal Request Client Order ID: {originalRequestClientOrderId}\n' \
                       '\t\tReport type: {reportType}\n'

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
