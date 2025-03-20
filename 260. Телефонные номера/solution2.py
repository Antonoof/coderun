import re

def parse_phone_number(number):
    return "".join([d for d in number if d.isdigit()])

def parse_template(template):
    match = re.match(r"\+(\d+) \((\d+)\) ([X\d]+) - (.+)", template)
    if match:
        country_code, operator_code, personal_number, operator = match.groups()
        return country_code, operator_code, personal_number, operator

def match_number_to_template(number, templates):
    for template in templates:
        country_code, operator_code, personal_number, operator = template
        if number.startswith(country_code + operator_code):
            remaining_number = number[len(country_code + operator_code):]
            if len(remaining_number) == len(personal_number) and re.fullmatch(personal_number.replace("X", "\d"), remaining_number):
                return f"+{country_code} ({operator_code}) {remaining_number} - {operator}"

def main():
    n = int(input())
    phone_numbers = [parse_phone_number(input()) for _ in range(n)]
    
    m = int(input())
    templates = [parse_template(input()) for _ in range(m)]
    
    for number in phone_numbers:
        result = match_number_to_template(number, templates)
        print(result)

if __name__ == "__main__":
    main()
