from django import forms
from django.core.validators import RegexValidator

country_codes = [
    ('+1', 'United States (+1)'),
    ('+44', 'United Kingdom (+44)'),
    ('+91', 'India (+91)'),
    ('+61', 'Australia (+61)'),
    ('+81', 'Japan (+81)'),
]

us_states = {
    'AL': 'Alabama',
    'AK': 'Alaska',
    'AZ': 'Arizona',
    'AR': 'Arkansas',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DE': 'Delaware',
    'DC': 'District of Columbia',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'IA': 'Iowa',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'ME': 'Maine',
    'MD': 'Maryland',
    'MA': 'Massachusetts',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MS': 'Mississippi',
    'MO': 'Missouri',
    'MT': 'Montana',
    'NE': 'Nebraska',
    'NV': 'Nevada',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NY': 'New York',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VT': 'Vermont',
    'VA': 'Virginia',
    'WA': 'Washington',
    'WV': 'West Virginia',
    'WI': 'Wisconsin',
    'WY': 'Wyoming',
}

class CustomerForm(forms.Form):
    full_name = forms.CharField(
        label="Customer Full Name",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Full Name'}),
        validators=[RegexValidator(r'^[a-zA-Z\s]+$', message='Name can only contain letters and spaces.')]
    )
    bank_name = forms.CharField(
        label="Name of the Bank",
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Bank Name'})
    )
    zip_code = forms.CharField(
        label="Zip Code",
        max_length=10,
        widget=forms.TextInput(attrs={'placeholder': '12345678'})
    )
    state = forms.ChoiceField(
        choices=us_states,
        label="State",
        initial="AL",
    )
    country_code = forms.ChoiceField(
        choices=country_codes,
        label='Country Code',
        initial='+91',  # Default selected value (India)
    )
    phone_number = forms.CharField(
        label="Phone Number",
        max_length=15,
        validators=[RegexValidator(regex=r'^\d+$', message='Phone number can only contain numbers.')]
    )
    account_number = forms.CharField(
        label="Full Account Number",
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder': 'Account Number'})
    )
    file_name = forms.CharField(
        label="Uploaded File Name",
        max_length=100,
        required=False,  # Not required if it’s just for storing the file name
        widget=forms.HiddenInput()
    )
