import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#read the csv file
gadgets_df = pd.read_csv("gadget_sales_report.csv", encoding="utf-8")


#create sales summary
total_sales= gadgets_df["Sales"].sum()
average_rating= round(gadgets_df["Rating"].mean(), 2)
sales_by_product= gadgets_df.groupby("Product")["Sales"].sum()
top_seller= sales_by_product.idxmax()
lowest_seller= sales_by_product.idxmin()
best_rated = gadgets_df.loc[gadgets_df["Rating"].idxmax()]["Product"]
worst_rated = gadgets_df.loc[gadgets_df["Rating"].idxmin()]["Product"]

# Question and answer section
def answer_question(question):
  print ('\n QUESTION AND ANSWER SUMMARY SECTION.')

  if "total sales" in question:
    print(f"Total units sold: {total_sales}")
  elif "average rating" in question:
    print(f"Average customer rating: {average_rating}")
  elif "highest sales" in question or "top seller" in question:
    print(f"The top-selling product was: {top_seller}")
  elif "lowest sales" in question or "worst seller" in question:
    print(f"The lowest-selling product was: {lowest_seller}")
  elif "best rated" in question or "highest rating" in question:
    print(f"Highest-rated product: {best_rated}")
  elif "worst rated" in question or "lowest rating" in question:
    print(f"Lowest-rated product: {worst_rated}")
  else:
      print("Sorry, I don't understand that question. Try asking about total sales, average rating, top seller, lowest sales etc.")

# Create a function for bar chart
def show_chart():
  sorted_sales = sales_by_product.sort_values(ascending=False)
  product_sales= sales_by_product.reset_index() #coverts the series into a dataframe so it can be used in a chart

  plt.figure(figsize=(10,6))
  sns.barplot(x="Product",
              y="Sales",
              data= product_sales,
              hue="Product",
              palette="muted",
              legend=False
              )
  plt.title(" 2025 Gadget Sales by Product Report", fontsize="20", fontweight="heavy")
  plt.xlabel("Products")
  plt.ylabel("Units Sold")
  plt.xticks(rotation=75)
  plt.tight_layout()
  plt.savefig("sales_chart.png", dpi=300)
  plt.show()

#Menu Bar
def show_menu():
  print("\n📋 MENU OPTIONS")
  print("1. Ask a Question")
  print("2. Show Sales Chart")
  print("3. Exit")

while True:
  try:
    show_menu()
    choice = input("Choose an option (1-3): ").strip()

    if choice == "1":
      question = input("Your question: ").lower().strip()
      answer_question(question)
    elif choice == "2":
      show_chart()
    elif choice == "3":
      print("Thanks for using the Gadget Sales Analyzer!")
      break
    else:
      print("Invalid choice. Please select a number from 1 to 3.")
  except:
    print('Go back and read instructions carefully .Baka!')

