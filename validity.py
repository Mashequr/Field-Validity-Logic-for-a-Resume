import re

# using regular expressions to validate relevant fields

def validate_name(name):
    if name is None:
        return False
    name_regex = r'^(([A-Z][a-z]\.)|([A-Z][a-z]+)|\s(([A-Z]\.)|([A-Z][a-z]+)))+$'
    return len(name) <= 100 and re.match(name_regex, name) is not None

def validate_email(email):
    if email is None:
        return False
    email_regex = r'^[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

def validate_phone(phone):
    if phone is None:
        return False
    phone_regex = r'^((\+8801)|(01))[0-9]{9}$'
    return re.match(phone_regex, phone) is not None

def validate_address(address):
    return isinstance(address, str) and len(address) > 0  # Basic validation for non-empty string

def validate_url(url):
    if url is None:
        return False
    url_regex = r'^(http|https)://[^\s/$.?#].[^\s]*$'
    return re.match(url_regex, url) is not None

def validate_resume_fields(resume):
        results = {}

        results["name"] = validate_name(resume.get("name", ""))
        results["email"] = validate_email(resume.get("email", ""))
        results["phone"] = validate_phone(resume.get("phone", ""))
        results["address"] = validate_address(resume.get("address", ""))
        results["github"] = validate_url(resume.get("github", ""))
        results["linkedin"] = validate_url(resume.get("linkedin", ""))
        results["portfolio_website"] = validate_url(resume.get("portfolio_website", ""))

        return results
    
# test cases
print("Valid data test case")

resume_data = {
    "name": "Mashequr Rahman Khan",
    "email": "khanmashequr@gmail.com",
    "phone": "01763307060",
    "github": "https://github.com/Mashequr/",
    "linkedin": "https://www.linkedin.com/in/mashequr-khan/",
    "portfolio_website": "https://www.mashequr.com",
    "address": "Uttara, Dhaka 1230"
}

validation_results = validate_resume_fields(resume_data)

for field, is_valid in validation_results.items():
    print(f"{field.capitalize()}: {'Valid' if is_valid else 'Invalid'}")

print()

resume_data = {
    "name": "Md. Rezwan Al Islam",
    "email": "md._rezwan_al_islam@bat.com",
    "phone": "01763307060",
    "github": "https://github.com/johndoe",
    "linkedin": "https://www.linkedin.com/in/johndoe",
    "portfolio_website": "https://www.batb.com",
    "address": "Dhaka, Bangladesh"
}

validation_results = validate_resume_fields(resume_data)

for field, is_valid in validation_results.items():
    print(f"{field.capitalize()}: {'Valid' if is_valid else 'Invalid'}")

print()

# Test case with invalid data
print("Invalid data test case")

invalid_resume_data = {
    "name": "This Is An Extremely Long Name That Exceeds The Hundred Character Limit And Is Therefore Invalid And Will Not Work",
    "email": "invalid_email@example",  # Missing top-level domain
    "phone": "123",  # Invalid phone number length
    "github": "not_a_url",  # Invalid URL format
    "linkedin": "www.linkedin.com/in/johndoe",  # Missing URL scheme
    "portfolio_website": "ftp://www.johndoe.com",  # Unsupported URL scheme
    "address": "123 Main St, City, Country"
}

validation_results = validate_resume_fields(invalid_resume_data)

for field, is_valid in validation_results.items():
    print(f"{field.capitalize()}: {'Valid' if is_valid else 'Invalid'}")

print()
print("Additional Test Cases")

# Test case with variations in email format
email_variations = [
    "valid_email@example.com",
    "john.doe@company.co.uk",
    "user123@subdomain.example",
    "user.name123@site-domain.com",
    "invalid_email@example",  # Missing top-level domain
    "invalid_email@.com",  # Missing domain name
    "@example.com",  # Missing username
]

print()
print("Email Variations Test Case")
for email in email_variations:
    is_valid = validate_email(email)
    print(f"Email: {email}, {'Valid' if is_valid else 'Invalid'}")

print()

# Test case with different valid phone number formats
phone_formats = [
    "+8801763307060",
    "01763307060",
    "+8801914604979", # Invalid due to white spaces and brackets
    "+44 20 7946 0958", # Invalid due to white spaces
    "1234567890",  # Invalid (10 digits only excluding Bangladesh code)
    "+123",  # Invalid without a complete number
]

print()
print("Phone Number Formats Test Case")
for phone in phone_formats:
    is_valid = validate_phone(phone)
    print(f"Phone: {phone}, {'Valid' if is_valid else 'Invalid'}")

print()

# Test case with potentially invalid address formats
address_formats = [
    "123 Main St, City, Country",
    "",  # Invalid: Empty address
    None,  # Invalid: None value
    12345,  # Invalid: Non-string value
]

print("Address Formats Test Case")
for address in address_formats:
    is_valid = validate_address(address)
    print(f"Address: {address}, {'Valid' if is_valid else 'Invalid'}")