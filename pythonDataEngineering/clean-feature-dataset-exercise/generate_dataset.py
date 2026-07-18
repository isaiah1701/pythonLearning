"""Create a repeatable, deliberately messy orders dataset for cleaning practice."""

from __future__ import annotations

import csv
import random
from datetime import date, timedelta
from pathlib import Path


RANDOM_SEED = 20260718
UNIQUE_ROWS = 4_850
DUPLICATE_ROWS = 150
OUTPUT_PATH = Path(__file__).parent / "data" / "raw_orders_dirty_5000.csv"

CUSTOMER_IDS = [f"CUST-{number:04d}" for number in range(1, 401)]
PRODUCTS = [
    "wireless mouse",
    "mechanical keyboard",
    "usb-c hub",
    "laptop stand",
    "webcam",
    "monitor",
    "headset",
    "desk lamp",
    "external ssd",
    "notebook",
]
PRODUCT_PRICES = {
    "wireless mouse": (15, 45),
    "mechanical keyboard": (60, 180),
    "usb-c hub": (25, 90),
    "laptop stand": (20, 75),
    "webcam": (30, 130),
    "monitor": (120, 450),
    "headset": (25, 160),
    "desk lamp": (18, 65),
    "external ssd": (45, 220),
    "notebook": (3, 15),
}


def format_product(product: str, row_number: int) -> str:
    """Add ordinary casing and whitespace inconsistencies for cleaning practice."""
    variants = (product, product.title(), product.upper(), f" {product} ")
    return variants[row_number % len(variants)]


def format_date(order_date: date, row_number: int) -> str:
    """Return several common text date formats plus intentional invalid values."""
    if row_number % 89 == 0:
        return ""
    if row_number % 211 == 0:
        return "unknown"

    formats = (
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%b %d, %Y",
        "%m-%d-%Y",
    )
    return order_date.strftime(formats[row_number % len(formats)])


def create_base_rows(generator: random.Random) -> list[dict[str, str]]:
    start_date = date(2024, 1, 1)
    rows: list[dict[str, str]] = []

    for row_number in range(1, UNIQUE_ROWS + 1):
        product = generator.choice(PRODUCTS)
        low_price, high_price = PRODUCT_PRICES[product]
        row = {
            "order_id": f"ORD-{row_number:06d}",
            "customer_id": generator.choice(CUSTOMER_IDS),
            "product": format_product(product, row_number),
            "quantity": str(generator.randint(1, 8)),
            "price": f"{generator.uniform(low_price, high_price):.2f}",
            "order_date": format_date(
                start_date + timedelta(days=generator.randint(0, 730)), row_number
            ),
        }

        # Intentional missing data. The patterns make the dataset repeatable.
        if row_number % 101 == 0:
            row["customer_id"] = ""
        if row_number % 137 == 0:
            row["product"] = ""
        if row_number % 149 == 0:
            row["quantity"] = ""
        if row_number % 163 == 0:
            row["price"] = ""

        rows.append(row)

    return rows


def main() -> None:
    generator = random.Random(RANDOM_SEED)
    rows = create_base_rows(generator)
    rows.extend(generator.sample(rows, DUPLICATE_ROWS))
    generator.shuffle(rows)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    print(f"Created {OUTPUT_PATH} with {len(rows):,} rows.")
    print(
        f"Includes {DUPLICATE_ROWS} exact duplicate rows and controlled missing values."
    )


if __name__ == "__main__":
    main()
