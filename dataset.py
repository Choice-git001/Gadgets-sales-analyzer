#GADGET SALES ANALYZER
import pandas as pd
import random

# Define products and months
products = [
    "Smartphones", "Laptops", "Tablets", "Smartwatches","Headphones", "Bluetooth Speakers", "Gaming Consoles", "Drones", "VR Headsets", "Smart Glasses",
    "Home Robots", "GPS Trackers"
]
months = pd.date_range(start="2025-01-01", end="2025-12-01", freq="MS")

# Define review
great_reviews = [
    "Absolutely fantastic!😍", "Highly recommended!🔥", "Exceeded expectations.💯", "Top-notch quality.👌", "Amazing performance.⭐", "Would buy again!🚀",
    "Flawless experience. ✨", "Premium feel. 👑",  "Blew me away! 🎉", "Perfect in every way.🪽"

]
good_reviews = [
    "Pretty good overall.👍", "Satisfied with the product.😇", "Works as expected.✅","Decent value for money.💸",
    "No major issues.🙌", "Solid choice.📌","Smooth experience. 🧊", "Happy with the purchase. 😌", "Reliable performance. 🔧","Meets expectations. 🎯",
]
bad_reviews = [
    "Not worth the price.😭", "Disappointing experience.😞", "Poor quality.🤒", "Feels poorly made. 🧃", "Frustrating to use. 😤",
    "Stopped working quickly. ⚠️", "Wouldn't recommend.🚫", "Needs improvement.🛠️", "Glitchy and unreliable. 🐞", "Regret buying it.😪", "Oh God, Never again.👎"
]

# Generate sample data
data = []
for month in months:
  for product in products:
        sales = random.randint(100, 1000)
        rating = round(random.uniform(1.0, 5.0), 1)

        # use if-elif-else statement to match reviews to ratings
        if rating >= 4.3:
            review = random.choice(great_reviews)
            sentiment= "Great"
        elif rating >= 2.5:
            review = random.choice(good_reviews)
            sentiment= "Good"
        else:
            review = random.choice(bad_reviews)
            sentiment= "Bad"

        data.append({
            "Date": month.strftime("%Y-%m-%d"),
            "Product": product,
            "Sales": sales,
            "Rating": rating,
            "Review": review,
            "Sentiment": sentiment
        })

# Convert to DataFrame
df = pd.DataFrame(data)

#Save to CSV
df.to_csv("gadget_sales_report.csv", index=False, encoding="utf-8")

# Preview code
df = df[["Date", "Product", "Sales", "Rating", "Sentiment", "Review"]]
print(df.head())
