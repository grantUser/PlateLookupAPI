# PlateLookupAPI

PlateLookupAPI is a web application that retrieves vehicle information based on its license plate.

## 🚀 Features
- Flask API that queries LaCentrale to retrieve vehicle details.
- HTML/TailwindCSS web interface for easy use.
- Supports French license plates (more countries can be added).

## 🛠 Installation
### Prerequisites
- Python 3
- Flask & curl_cffi
- Node.js (optional for TailwindCSS)

### Backend Installation
```bash
# Clone the repository
git clone https://github.com/grantUser/PlateLookupAPI.git
cd PlateLookupAPI

# Install dependencies
pip install flask flask-cors curl_cffi

# Run the API
python app.py
```

### Running the Frontend
Open the `index.html` file in a browser.

## 🔥 Usage
The API can be accessed at:
```
GET http://localhost:5000/car/fr?plate=XX-XXX-XX
```
Response:
```json
{
  "data": {
    "category": "XXXXXX",
    "commercialName": "XXXXXX",
    "doors": "XXXXXX",
    "energy": "XXXXXX",
    "firstTrafficDate": "XXXXXX",
    "gearbox": "XXXXXX",
    "licensePlate": "XXXXXX",
    "make": "XXXXXX",
    "model": "XXXXXX",
    "vertical": "XXXXXX",
    "vin": "XXXXXXXXXXXXXXXXXX"
  },
  "success": true
}

```

## 📌 Future Improvements
- Support for UK license plates and other countries
- Better error handling
- More advanced user interface

## 📝 License
This project is open-source under the MIT license.

