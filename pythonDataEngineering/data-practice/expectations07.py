import great_expectations as gx 
import pandas as pd 
import logging 


logging.basicConfig(level=logging.INFO)

messy_data = {
    "order": [
        "phone",
        "laptop",
        "watch",
        "tablet",   # Bad: not an allowed order
        "phone",
        "laptop",
        "watch"
    ],
    "quantity": [
        2,
        1,
        5,
        3,
        0,          # Bad: below 1
        7,          # Bad: above 5
        4
    ],
    "price": [
        799.99,
        1500.00,
        249.99,
        600.00,
        -20.00,     # Bad: below 0
        12000.00,   # Bad: above 10,000
        0.00         # Bad: must be more than 0
    ]
}


df = pd.DataFrame(messy_data)








def validate_orders(df) -> bool:
    context = gx.get_context()
    batch = context.data_sources.pandas_default.read_dataframe(df)

    results = [
        batch.validate(
            gx.expectations.ExpectColumnValuesToBeBetween(
                column="price",
                min_value=1,
                max_value=9999
            )
        ),

        batch.validate(
            gx.expectations.ExpectColumnValuesToBeBetween(
                column="quantity",
                min_value=1,
                max_value=5
            )
        ),

        batch.validate(
            gx.expectations.ExpectColumnValuesToBeInSet(
                column="order",
                value_set=["phone", "laptop", "watch"]
            )
        )
    ]

    all_passed = all(r.success for r in results)

    if all_passed:
        logging.info("All passed")
    else:
        failed = [r for r in results if not r.success]
        logging.error(f"{len(failed)} expectations were not successful")

    return all_passed


print(validate_orders(df))

  