"# AI Crop Yield & Price Prediction System

## 📋 Project Overview

The AI Crop Yield & Price Prediction System is an intelligent agricultural application that predicts crop yields and market prices based on various environmental and geographical factors. This system helps farmers and agricultural stakeholders make informed decisions about crop cultivation and market timing.

**Key Features:**
- Real-time crop yield prediction using machine learning
- Dynamic market price estimation based on weather conditions
- Profit margin calculation for different crops
- Interactive web-based dashboard
- Support for multiple crop types (Wheat, Rice, Sugarcane, Bajra, Maize, Soybean)

---

## 🎯 Project Goals

1. **Prediction Accuracy**: Provide accurate crop yield predictions based on historical data and environmental factors
2. **Market Intelligence**: Estimate fair market prices considering rainfall and temperature conditions
3. **Farmer Support**: Help farmers optimize planting decisions and market timing strategies
4. **Scalability**: Build a foundation for future enhancements and integrations

---

## 📁 Project Structure

```
AI_Crop_Project/
├── app.py                           # Main Flask application server
├── requirements.txt                 # Python dependencies
├── README.md                        # Project documentation
├── .gitignore                       # Git ignore rules
│
├── data/
│   └── crop_yield_dataset_3200_rows.csv    # Training dataset with 3200 records
│
├── model/
│   ├── model.pkl                   # Trained machine learning model
│   └── model.pkl.txt               # Model metadata/notes
│
├── notebook/                        # Jupyter notebooks for analysis & training
│   └── (Currently empty - for future exploration notebooks)
│
└── templates/
    └── index.html                  # Web interface template
```

---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd AI_Crop_Project
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Update Model Path (Important)
Edit `app.py` and update the model path on line 12:
```python
# Change this hardcoded path to your local path
model = pickle.load(open(r"C:\Users\KANZARIYA HARDIK\Desktop\AI_Crop_Project\model\model.pkl", 'rb'))
```

Or better, use a relative path:
```python
import os
model_path = os.path.join(os.path.dirname(__file__), 'model', 'model.pkl')
model = pickle.load(open(model_path, 'rb'))
```

### Step 5: Run the Application
```bash
python app.py
```

The application will start at `http://localhost:5000`

---

## 📊 Dataset Information

**File**: `data/crop_yield_dataset_3200_rows.csv`

**Dataset Size**: 3,200 records

**Features Used in Model**:
- State (numerical encoding)
- Crop Type (0: Wheat, 1: Rice, 2: Sugarcane, 3: Bajra, 4: Maize, 5: Soybean)
- Year (cultivation year)
- Rainfall (in mm)
- Temperature (in Celsius)
- Area (cultivation area in hectares)

**Target Variable**: Crop Yield (in tons/hectares)

---

## 🤖 Machine Learning Model

**Model File**: `model/model.pkl`

**Model Details**:
- Type: Supervised Learning (Regression)
- Training Data: 3,200 records with 6 input features
- Output: Predicted crop yield

**Model Performance**:
- Trained on historical crop data
- Supports prediction for 6 major crop types
- Predicts yield based on environmental and geographical conditions

---

## 💰 Price Prediction Algorithm

The system uses a dynamic pricing model that considers:

1. **Base Price**: Predetermined base market price for each crop
2. **Rainfall Adjustment**: 
   - Rainfall > 200mm: -₹150 (increased supply)
   - Rainfall < 100mm: +₹150 (scarcity premium)
3. **Temperature Adjustment**:
   - Temperature > 30°C: +₹100 (heat stress premium)
   - Temperature < 20°C: -₹50 (reduced demand)
4. **Market Fluctuation**: Random variation (±₹100) to simulate market dynamics

**Base Prices by Crop**:
- Wheat: ₹2,200
- Rice: ₹1,800
- Maize: ₹1,700
- Bajra: ₹1,500
- Soybean: ₹4,000
- Sugarcane: ₹3,000

**Profit Calculation**:
```
Profit = Predicted Yield × Estimated Price
```

---

## 🌐 Web Interface

**File**: `templates/index.html`

**Features**:
- Sidebar navigation with Agro AI branding
- Input form for crop parameters
- Real-time prediction display
- Results cards showing:
  - Predicted Yield
  - Estimated Market Price
  - Estimated Profit
- Responsive design with green agricultural theme
- Chart.js integration for data visualization

**Input Fields**:
- State (dropdown)
- Crop Type (dropdown)
- Year (numeric)
- Rainfall (numeric)
- Temperature (numeric)
- Area (numeric)

---

## 🚀 Usage Guide

### Making a Prediction

1. Open the web application at `http://localhost:5000`
2. Fill in the prediction form with:
   - **State**: Select your state (numerical encoding)
   - **Crop**: Choose from the 6 supported crops
   - **Year**: Enter the cultivation year
   - **Rainfall**: Enter expected/historical rainfall in mm
   - **Temperature**: Enter average temperature in °C
   - **Area**: Enter cultivation area in hectares
3. Click "Predict" button
4. View results:
   - **Yield**: Predicted crop yield (tons/hectares)
   - **Price**: Estimated market price (₹)
   - **Profit**: Total estimated profit (₹)

### Interpreting Results

- **High Yield + High Price**: Optimal conditions
- **High Yield + Low Price**: Market oversupply scenario
- **Low Yield + High Price**: Potential profit opportunity (scarcity)
- **Low Yield + Low Price**: Challenging conditions

---

## 🔧 Configuration

### Flask Configuration
- Debug Mode: Currently enabled (change for production)
- Host: localhost (127.0.0.1)
- Port: 5000

### Recommended Production Changes
```python
if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
```

### Environment Variables (Recommended)
Create a `.env` file:
```
FLASK_ENV=production
FLASK_APP=app.py
MODEL_PATH=model/model.pkl
DEBUG=False
```

---

## 📈 Model Improvement Ideas

1. **Real-time Weather Data**: Integrate weather APIs for live rainfall/temperature
2. **Market Price Integration**: Connect to live commodity market data
3. **Historical Trends**: Include multi-year trend analysis
4. **Soil Data**: Add soil quality and pH levels as features
5. **Pest/Disease Indicators**: Include pest and disease prevalence data
6. **Crop Rotation Recommendations**: Suggest crop rotations
7. **Advanced Models**: Ensemble methods, Deep Learning for better predictions
8. **Mobile App**: Develop mobile application for farmer accessibility

---

## 🐛 Troubleshooting

### Issue: Model File Not Found
**Solution**: Update the model path in `app.py` or place `model.pkl` in the correct directory

### Issue: Module Import Error
**Solution**: Reinstall requirements
```bash
pip install --upgrade -r requirements.txt
```

### Issue: Port 5000 Already in Use
**Solution**: Change port in app.py or kill existing process
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# macOS/Linux
lsof -i :5000
kill -9 <PID>
```

### Issue: CORS Errors
**Solution**: Enable CORS by uncommenting in app.py:
```python
from flask_cors import CORS
CORS(app)
```

---

## 🔐 Security Considerations

1. **Model Protection**: Keep `model.pkl` secure and protected
2. **Input Validation**: Validate all user inputs on backend
3. **API Rate Limiting**: Implement rate limiting for production
4. **HTTPS**: Use HTTPS in production deployment
5. **Error Handling**: Avoid exposing sensitive error details to users

---

## 📦 Dependencies Details

| Package | Version | Purpose |
|---------|---------|---------|
| Flask | 2.3.3 | Web framework |
| Flask-CORS | 4.0.0 | Cross-Origin Resource Sharing |
| NumPy | 1.24.3 | Numerical computing |
| Pandas | 2.0.3 | Data manipulation |
| scikit-learn | 1.3.0 | Machine learning |
| Matplotlib | 3.7.2 | Data visualization |
| Seaborn | 0.12.2 | Statistical visualization |
| Joblib | 1.3.1 | Model serialization |
| Werkzeug | 2.3.7 | WSGI utilities |
| python-dotenv | 1.0.0 | Environment variables |

---

## 📝 License

[Specify your license here - e.g., MIT, Apache 2.0, etc.]

---

## 👥 Contributors

- **Project Lead**: [Your Name]
- **Lead Developer**: [Developer Name]
- **ML Engineer**: [ML Engineer Name]

---

## 📞 Support & Contact

For issues, suggestions, or improvements:
- Create an issue on GitHub
- Email: [contact-email]
- Documentation: See related notebooks in `/notebook/` directory

---

## 🗺️ Future Roadmap

- [ ] Mobile application development
- [ ] Real-time weather API integration
- [ ] Live commodity price feeds
- [ ] Advanced analytics dashboard
- [ ] Multilingual support
- [ ] IoT sensor integration
- [ ] Blockchain for supply chain tracking
- [ ] AI-powered crop advisory system

---

## 📚 Resources & References

- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [NumPy Documentation](https://numpy.org/)
- [Agricultural Data Sources](https://data.gov.in/)

---

**Last Updated**: May 10, 2026  
**Version**: 1.0.0  
**Status**: Active Development" 
