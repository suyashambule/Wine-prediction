# Wine Quality Prediction

A machine learning project that predicts wine quality based on physicochemical properties. This project implements an end-to-end ML pipeline with a Flask web application for real-time predictions.

## 🍷 About the Project

This project uses wine quality data to build a predictive model that can assess wine quality based on various chemical properties such as acidity, sugar content, pH levels, and alcohol content. The application provides both a web interface for individual predictions and a complete ML pipeline for model training and evaluation.

## 🚀 Features

- **End-to-end ML Pipeline**: Complete data science workflow from ingestion to model deployment
- **Web Application**: Flask-based web interface for real-time predictions
- **Modular Architecture**: Well-structured codebase with separate components for different pipeline stages
- **Docker Support**: Containerized application for easy deployment
- **Research Notebooks**: Jupyter notebooks for data exploration and experimentation
- **MLflow Integration**: Experiment tracking and model management

## 📊 Model Input Features

The model takes the following wine characteristics as input:

1. **Fixed Acidity**: Non-volatile acids in wine
2. **Volatile Acidity**: Acetic acid content (high levels can lead to vinegar taste)
3. **Citric Acid**: Acts as a preservative and adds freshness
4. **Residual Sugar**: Sugar remaining after fermentation
5. **Chlorides**: Salt content in wine
6. **Free Sulfur Dioxide**: Prevents microbial growth and wine oxidation
7. **Total Sulfur Dioxide**: Total amount of SO2 (free + bound forms)
8. **Density**: Density of wine (depends on alcohol and sugar content)
9. **pH**: Acidity/alkalinity level (0-14 scale)
10. **Sulphates**: Wine additive acting as antimicrobial and antioxidant
11. **Alcohol**: Alcohol percentage in wine

## 🛠️ Project Structure

```
Wine-prediction/
│
├── src/datascience/           # Main source code
│   ├── components/            # Pipeline components
│   ├── config/               # Configuration management
│   ├── entity/               # Data classes and entities
│   ├── pipeline/             # ML pipeline stages
│   └── utils/                # Utility functions
│
├── config/                   # Configuration files
├── research/                 # Jupyter notebooks for research
├── templates/                # HTML templates for web app
├── logs/                     # Application logs
├── artifacts/                # Generated artifacts (models, data)
│
├── app.py                    # Flask web application
├── main.py                   # Pipeline execution script
├── requirements.txt          # Python dependencies
├── Dockerfile               # Docker configuration
├── config.yaml              # Main configuration
├── params.yaml              # Model parameters
└── schema.yaml              # Data schema
```

## 🔧 Installation

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Local Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Wine-prediction
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

   The application will be available at `http://localhost:8080`

### Docker Setup

1. **Build the Docker image**
   ```bash
   docker build -t wine-prediction .
   ```

2. **Run the container**
   ```bash
   docker run -p 8080:8080 wine-prediction
   ```

## 💻 Usage

### Web Application

1. **Home Page**: Navigate to `http://localhost:8080`
2. **Training**: Visit `/train` to trigger model training
3. **Prediction**: Use the prediction form to input wine characteristics and get quality predictions

### Training Pipeline

```bash
python main.py
```

This will execute the complete ML pipeline:
- Data ingestion
- Data validation
- Data transformation
- Model training
- Model evaluation

### API Endpoints

- `GET /`: Home page with prediction form
- `GET /train`: Trigger model training pipeline
- `POST /predict`: Submit wine characteristics for prediction

## 📈 Research Notebooks

Explore the research notebooks in the `research/` directory:

- `1_data_ingestion.ipynb`: Data loading and initial exploration
- `2_data_validation.ipynb`: Data quality checks and validation
- `3_data_transformation.ipynb`: Feature engineering and preprocessing
- `4_model_trainer.ipynb`: Model selection and training
- `5_model_evaluation.ipynb`: Model performance evaluation

## 🛠️ Technology Stack

- **Backend**: Python, Flask
- **ML Libraries**: Scikit-learn, Pandas, NumPy
- **Experiment Tracking**: MLflow
- **Web Framework**: Flask
- **Containerization**: Docker
- **Data Visualization**: Matplotlib
- **Configuration**: PyYAML
- **Logging**: Python logging

## 📋 Configuration

- **config.yaml**: Main configuration file with data sources and paths
- **params.yaml**: Model hyperparameters and training settings
- **schema.yaml**: Data schema and validation rules

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the terms specified in the LICENSE file.

## 🙏 Acknowledgments

- Wine quality dataset from UCI Machine Learning Repository
- Flask community for the excellent web framework
- Scikit-learn for machine learning tools

## 📞 Contact

For questions or suggestions, please open an issue in the repository.

---

*Happy wine quality prediction! 🍷*
