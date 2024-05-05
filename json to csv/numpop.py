import json
import csv

# Load JSON data from file
with open('result.json', 'r') as json_file:
    data = json.load(json_file)

# Extract contact list from JSON
contacts = data['contacts']['list']

# Define CSV file and headers
csv_file = 'contacts.csv'
csv_headers = [
    'Name', 'Given Name', 'Additional Name', 'Family Name', 'Yomi Name', 'Given Name Yomi',
    'Additional Name Yomi', 'Family Name Yomi', 'Name Prefix', 'Name Suffix', 'Initials',
    'Nickname', 'Short Name', 'Maiden Name', 'Birthday', 'Gender', 'Location',
    'Billing Information', 'Directory Server', 'Mileage', 'Occupation', 'Hobby',
    'Sensitivity', 'Priority', 'Subject', 'Notes', 'Language', 'Photo', 'Group Membership',
    'E-mail 1 - Type', 'E-mail 1 - Value', 'E-mail 2 - Type', 'E-mail 2 - Value',
    'Phone 1 - Type', 'Phone 1 - Value', 'Phone 2 - Type', 'Phone 2 - Value',
    'Phone 3 - Type', 'Phone 3 - Value', 'Address 1 - Type', 'Address 1 - Formatted',
    'Address 1 - Street', 'Address 1 - City', 'Address 1 - PO Box', 'Address 1 - Region',
    'Address 1 - Postal Code', 'Address 1 - Country', 'Address 1 - Extended Address',
    'Organization 1 - Type', 'Organization 1 - Name', 'Organization 1 - Yomi Name',
    'Organization 1 - Title', 'Organization 1 - Department', 'Organization 1 - Symbol',
    'Organization 1 - Location', 'Organization 1 - Job Description'
]

# Write data to CSV file
with open(csv_file, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write headers to CSV
    csv_writer.writerow(csv_headers)

    # Write contact information to CSV
    for contact in contacts:
        first_name = contact['first_name']
        last_name = contact['last_name']
        phone_number = contact['phone_number']

        # Write a row with empty values for additional fields
        csv_writer.writerow([f"{first_name} {last_name}", first_name, '', last_name, '', '', '', '',
                             '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                             '', '', '', '', '', '', '', '', '', '', 'Mobile', phone_number, '', '',
                             '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                             '', '', '', '', '', '', '', ''])

print(f'CSV file "{csv_file}" created successfully.')
