import pandas as pd

# Data: UCI Online Retail — https://doi.org/10.24432/C5BW33
orders = pd.read_excel("Online Retail.xlsx", engine="openpyxl")

columns = ["InvoiceNo", "InvoiceDate", "Quantity", "UnitPrice"]
data = orders[columns].dropna()
is_cancelled = data["InvoiceNo"].astype(str).str.upper().str.startswith("C")
sales = data.loc[
    ~is_cancelled & (data["Quantity"] > 0) & (data["UnitPrice"] > 0)
].copy()

sales["SalesGBP"] = sales["Quantity"] * sales["UnitPrice"]
sales["Month"] = pd.to_datetime(sales["InvoiceDate"]).dt.strftime("%Y-%m")
monthly_sales = sales.groupby("Month", as_index=False)["SalesGBP"].sum()
monthly_sales["SalesGBP"] = monthly_sales["SalesGBP"].round(2)

print(monthly_sales.to_string(index=False))
monthly_sales.to_csv("monthly_sales.csv", index=False)
