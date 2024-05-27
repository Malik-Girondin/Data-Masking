import pandas as pd
import random
import numpy as np

# Sample data
data = pd.DataFrame({
    'Last_name': ['Smith', 'Johnson', 'Williams', 'Jones'],
    'First_name': ['John', 'Emma', 'James', 'Olivia'],
    'Gender': ['male', 'female', 'male', 'female'],
    'Country': ['US', 'US', 'Sweden', 'Sweden'],
    'Date_of_Birth': pd.to_datetime(['1990-05-21', '1985-08-12', '1992-03-15', '1989-11-30']),
    'Street': ['Main St', '2nd St', '3rd St', '4th St'],
    'House_Number': ['123', '456', '789', '101'],
    'Postal_Area': ['10001', '10002', '10003', '10004'],
    'City': ['New York', 'Los Angeles', 'Stockholm', 'Gothenburg'],
    'SSN': ['123-45-6789', '987-65-4321', '111-22-3333', '444-55-6666']
})

# Function to shuffle last names
def shuffle_last_names(data):
    last_names = data['Last_name'].tolist()
    random.shuffle(last_names)
    data['Last_name'] = last_names
    return data

# First name generators for US and Sweden
first_names_us = {
    'male': ['John', 'Michael', 'Robert', 'James'],
    'female': ['Mary', 'Patricia', 'Jennifer', 'Linda']
}

first_names_sweden = {
    'male': ['Erik', 'Lars', 'Karl', 'Anders'],
    'female': ['Maria', 'Anna', 'Margareta', 'Elisabeth']
}

# Function to generate new first names based on gender and country
def generate_first_name(gender, country):
    if country == 'US':
        return random.choice(first_names_us[gender])
    elif country == 'Sweden':
        return random.choice(first_names_sweden[gender])

def mask_first_names(data):
    for index, row in data.iterrows():
        gender = row['Gender']
        country = row['Country']
        data.at[index, 'First_name'] = generate_first_name(gender, country)
    return data

# Function to mask dates of birth
def mask_date_of_birth(data):
    data['Date_of_Birth'] = data['Date_of_Birth'].apply(lambda x: x.replace(day=1))
    return data

# Function to group shuffle address components
def group_shuffle_addresses(data):
    addresses = data[['Street', 'House_Number', 'Postal_Area', 'City']].values.tolist()
    random.shuffle(addresses)
    shuffled_addresses = pd.DataFrame(addresses, columns=['Street', 'House_Number', 'Postal_Area', 'City'])
    data[['Street', 'House_Number', 'Postal_Area', 'City']] = shuffled_addresses
    return data

# Function to generate new SSNs
def generate_ssn(data):
    ssn_prefix = np.arange(100, 999)
    ssn_suffix = np.arange(1000, 9999)
    data['SSN'] = [f"{random.choice(ssn_prefix)}-{random.choice(ssn_suffix)}" for _ in range(len(data))]
    return data

# Applying data masking
data = shuffle_last_names(data)
data = mask_first_names(data)
data = mask_date_of_birth(data)
data = group_shuffle_addresses(data)
data = generate_ssn(data)

# Display the masked data
print(data)
