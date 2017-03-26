def future_value_chunk(payment, growth, periods):
    a = (1 + growth) ** periods
    b = ( a - 1 ) / growth
    return payment * b

def future_value_lump(present, inflation, periods):
    return present * ( ( 1 + inflation ) ** periods)

def run():
    # print("VTI")
    # print(future_value_lump(10000, 0.0723-0.0005, 10))

    # print("VB")
    # print(future_value_lump(10000, 0.081-0.0008, 10))    
    
    # print("VDC")
    # print(future_value_lump(10000, 0.1012-0.001, 10))    
    print(future_value_lump(2000, 0.07, 1))    
run()