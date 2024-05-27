# Data-Masking
This is a pre-built, customizable Python script for Data Masking.
<img width="1423" alt="Screenshot 2024-05-27 at 5 17 44 PM" src="https://github.com/Malik-Girondin/Data-Masking/assets/132381912/660cda20-2bbf-402a-85a6-5cd789253a38">
## Explanation

### Sample Data
A sample data frame `data` is created for demonstration purposes. In a real project, you would replace this with your actual data.

### Shuffle Last Names
The `shuffle_last_names` function shuffles the last names within the dataset.

### First Name Masking
- First name lists for the US and Sweden are defined.
- The `generate_first_name` function selects a new first name based on gender and country.
- The `mask_first_names` function iterates through the dataset and assigns new first names.

### Date of Birth Masking
The `mask_date_of_birth` function sets all birth dates to the first day of the same month and year.

### Group Shuffle Addresses
To maintain consistency, the `group_shuffle_addresses` function shuffles street, house number, postal area, and city.

### Generate SSNs
The `generate_ssn` function generates new SSNs based on a sequence.

### Applying Data Masking
- Each masking function is applied to the sample data in sequence.
- The final masked data is printed.

You can run this script to see how the data masking works. Replace the sample data with your actual dataset for practical use. If you need further assistance or modifications, feel free to ask!
