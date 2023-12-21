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
        results["address"] = "address" in resume
        results["github"] = validate_url(resume.get("github", ""))
        results["linkedin"] = validate_url(resume.get("linkedin", ""))
        results["portfolio_website"] = validate_url(resume.get("portfolio_website", ""))

        return results
    
# test case
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
