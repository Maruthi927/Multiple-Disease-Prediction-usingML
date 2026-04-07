class Config:
    ENVIRONMENT = "development"
    DEBUG = True
    DATABASE_URI = "sqlite:///development.db"

class DevelopmentConfig(Config):
    pass

class TestingConfig(Config):
    ENVIRONMENT = "testing"
    DATABASE_URI = "sqlite:///testing.db"
    DEBUG = True

class ProductionConfig(Config):
    ENVIRONMENT = "production"
    DATABASE_URI = "mysql://user:password@localhost/prod_db"
    DEBUG = False

MODEL_CONFIG = {
    'disease_1': {'name': 'Diabetes', 'treatment': 'Insulin'},
    'disease_2': {'name': 'Hypertension', 'treatment': 'Lisinopril'},
    'disease_3': {'name': 'Cancer', 'treatment': 'Chemotherapy'}
}