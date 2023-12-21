# Resume Field Validation

This Python script provides a set of functions to validate key fields in a resume based on specific criteria. The validation logic covers fields such as name, email, phone number, GitHub URL, LinkedIn URL, and portfolio website URL.

## Validation Functions

### `validate_name(name)`

Purpose: Validates the 'name' field in a resume.

Criteria:
- Must be within 100 characters.
- Should follow a specific format where each word starts with an uppercase letter.

### `validate_email(email)`

Purpose: Validates the 'email' field in a resume.

Criteria:
- Follows standard industry practices for email validity.

### `validate_phone(phone)`

Purpose: Validates the 'phone' field in a resume.

Criteria:
- Adheres to standard industry practices for phone number validity.

### `validate_url(url)`

Purpose: Validates URL fields (GitHub, LinkedIn, and portfolio website) in a resume.

Criteria:
- Must be a valid URL according to basic URL format.

### `validate_resume_fields(resume)`

Purpose: Validates all key fields in a resume.

Validation includes:
- Name, Email, and Phone fields using specific validation functions.
- Address field, which is considered valid if present.
- GitHub, LinkedIn, and Portfolio Website fields using the URL validation function.

## Assumptions and Considerations

1. **Name Validation:**
   - Assumes that the name should not exceed 100 characters.
   - Applies a specific format requirement to the name, where each word starts with an uppercase letter.

2. **Email Validation:**
   - Follows standard industry practices for email validity without detailed email format specification.

3. **Phone Validation:**
   - Adheres to a specific phone number format commonly used in the industry.

4. **URL Validation:**
   - Applies a basic URL format check for GitHub, LinkedIn, and Portfolio Website fields.

5. **Address Field:**
   - Considers the 'address' field valid if it is present; no specific validation criteria provided.

6. **Error Handling:**
   - Assumes that missing fields will result in validation failure.

## Test Cases

The script includes test cases to demonstrate the functionality of each validation function with both valid and invalid inputs.

---

Feel free to adapt and expand this README based on your preferences and additional details you want to include.
