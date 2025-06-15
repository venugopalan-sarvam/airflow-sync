import pandas as pd
def hello(name: str) -> str:
    df = pd.DataFrame()
    print(df)
    greeting = f"Hello {name}! Good day to you!"
    print(greeting)
    return greeting

def run_script_main():
    hello("Venugopalan")

run_script_main()