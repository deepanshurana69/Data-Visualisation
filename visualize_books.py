"""
Personal Data Analytics Portfolio - Task 3: Data Visualization
Creates presentation-ready charts from the Task 1 dataset.
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parents[1]
INPUT = BASE / "Task1_Web_Scraping" / "data" / "books.csv"
OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)


def main():
    if not INPUT.exists():
        raise FileNotFoundError(
            "books.csv not found. Run Task1_Web_Scraping/scrape_books.py first."
        )

    df = pd.read_csv(INPUT)

    # 1. Rating distribution
    rating_counts = df["rating"].value_counts().sort_index()
    plt.figure(figsize=(8, 5))
    rating_counts.plot(kind="bar")
    plt.title("Books by Rating")
    plt.xlabel("Rating")
    plt.ylabel("Number of Books")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(OUT / "rating_distribution.png", dpi=150)
    plt.close()

    # 2. Price by rating
    avg_price = df.groupby("rating")["price_gbp"].mean()
    plt.figure(figsize=(8, 5))
    avg_price.plot(kind="bar")
    plt.title("Average Book Price by Rating")
    plt.xlabel("Rating")
    plt.ylabel("Average Price (GBP)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(OUT / "average_price_by_rating.png", dpi=150)
    plt.close()

    # 3. Top 10 most expensive books
    top10 = df.nlargest(10, "price_gbp").sort_values("price_gbp")
    plt.figure(figsize=(10, 6))
    plt.barh(top10["title"], top10["price_gbp"])
    plt.title("Top 10 Most Expensive Books")
    plt.xlabel("Price (GBP)")
    plt.tight_layout()
    plt.savefig(OUT / "top10_expensive_books.png", dpi=150)
    plt.close()

    # 4. Price vs rating
    plt.figure(figsize=(8, 5))
    plt.scatter(df["rating"], df["price_gbp"], alpha=0.65)
    plt.title("Book Price vs Rating")
    plt.xlabel("Rating")
    plt.ylabel("Price (GBP)")
    plt.xticks([1, 2, 3, 4, 5])
    plt.tight_layout()
    plt.savefig(OUT / "price_vs_rating.png", dpi=150)
    plt.close()

    print(f"Created 4 charts in {OUT}")


if __name__ == "__main__":
    main()
