import pandas as pd
from faker import Faker
import random

# Initialize the data generator
fake = Faker()
random.seed(42)  # Ensures mathematical replication for large-scale data

roles = ['Engineering Manager', 'AI Engineer', 'Data Scientist', 'DevOps Specialist', 'FullStack Developer']
skills_pool = ['Python', 'Docker', 'Kubernetes', 'LLMs', 'PyTorch', 'AWS', 'SQL', 'Scrum', 'Git', 'CI/CD']

def generate_synthetic_cv(cv_id):
    years_exp = random.randint(1, 15)
    num_skills = random.randint(4, 8)
    
    university_name = f"{fake.company()} University"
    
    profile = {
        "id": f"CV_{cv_id:04d}",  # Supports up to 4 digits (CV_0001)
        "name": fake.name(),
        "role": random.choice(roles),
        "experience_years": years_exp,
        "skills": ", ".join(random.sample(skills_pool, num_skills)),
        "education": f"Bachelor in Computer Science - {university_name}",
        "current_company": fake.company(),
        "summary": fake.paragraph(nb_sentences=3)
    }
    
    # Control injection of elite manager profiles with a Kozminski EMBA
    if years_exp > 6 and random.random() > 0.4:
        profile["education"] += " | Executive MBA @ Koźmiński University"
        profile["role"] = "Senior Engineering Manager"
        
    return profile

# Generate exactly 1,000 synthetic records
cv_data = [generate_synthetic_cv(i) for i in range(1, 1001)]

# Save to CSV (overwrites the old file)
df = pd.DataFrame(cv_data)
df.to_csv("source_data.csv", index=False)
print("✅ Step 1 completed successfully! Saved 1,000 profiles into 'source_data.csv'.")
