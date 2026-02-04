# Library imports
import argparse
import csv

parser = argparse.ArgumentParser(description="Generate CSV with repeated letters from JSON config")
parser.add_argument(
    "--letter",
    type=str,
    required=True
)
parser.add_argument(
    "--number",
    type=int,
    required=True
)

args = parser.parse_args()
letter = args.letter
number = args.number


filename = f"output/output_{letter}_{number}.csv"
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Letter', 'Number', 'Repeated Letter'])
    repeated_letter = letter * number
    writer.writerow([letter, number, repeated_letter])
#print(f"CSV file '{filename}' generated successfully.")