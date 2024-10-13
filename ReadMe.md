## Create a new Conda env
conda create -n my_env python=3.10 -y
conda info --envs
conda activate my_env
pip install -r requirements.txt
conda deactivate

## Run the Application
```python
streamlit run app.py
```