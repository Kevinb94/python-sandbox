# PySpark Practice Script
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, count, desc, upper

# === File path variables ===
CSV_INPUT_PATH = "../sample_data/sample_customers.csv"
PARQUET_OUTPUT_PATH = "./customers_out.parquet"

def show_summary_statistics(df):
    """
    Show summary statistics for numerical columns.
    """
    print("\n=== Summary statistics ===")
    df.describe().show()

def count_customers_by_gender(df):
    """
    Count how many customers of each gender.
    """
    print("\n=== Count customers by gender ===")
    df.groupBy("gender").count().show()

def get_average_age(df):
    """
    Calculate the average age of customers.
    """
    print("\n=== Average age ===")
    df.agg(avg("age").alias("average_age")).show()

def show_top_ages(df, n=3):
    """
    Show the most common ages and how many times they appear.
    """
    print(f"\n=== Top {n} most common ages ===")
    df.groupBy("age").count().orderBy(desc("count")).show(n)

def uppercase_names(df):
    """
    Return a DataFrame with first and last names uppercased.
    """
    print("\n=== Uppercased names ===")
    df2 = df.withColumn("first_name_upper", upper(col("first_name"))) \
            .withColumn("last_name_upper", upper(col("last_name")))
    df2.select("first_name_upper", "last_name_upper").show(5)
    return df2

def save_to_parquet(df, path=PARQUET_OUTPUT_PATH):
    """
    Save the DataFrame as a Parquet file.
    """
    print(f"\n=== Saving DataFrame to {path} ===")
    df.write.mode("overwrite").parquet(path)
    print("Done saving.")

def main():
    spark = SparkSession.builder.appName("PySparkPractice").getOrCreate()

    # Read the sample CSV file
    df = spark.read.csv(CSV_INPUT_PATH, header=True, inferSchema=True)
    
    print("\n=== Show first 5 rows ===")
    df.show(5)
    df.printSchema()
    
    # Select and show only names and ages
    print("\n=== Select names and ages ===")
    df.select("first_name", "last_name", "age").show(5)
    
    # Filter customers older than 40
    print("\n=== Customers older than 40 ===")
    df.filter(df.age > 40).show(5)

    # Additional practice functions:
    show_summary_statistics(df)
    count_customers_by_gender(df)
    get_average_age(df)
    show_top_ages(df)
    df2 = uppercase_names(df)
    save_to_parquet(df2)
    
    spark.stop()

if __name__ == "__main__":
    main()
