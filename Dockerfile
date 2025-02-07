FROM continuumio/miniconda3

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD streamlit run Dashboard.py
