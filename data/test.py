import pandas as pd

df = pd.read_csv("./raw data/data_vancouver_copy.csv",encoding = "ISO-8859-1")

# print(df.area.unique())

# vancouver west
st = 'Champlain-Heights,Collingwood,Downtown-East,Fraser-East,Fraserview-East,Grandview-East,Hastings,Hastings-Sunrise,Killarney,Knight,Main,Mount-Pleasant-East,Renfrew,Renfrew-Heights,South-Vancouver,Victoria-East'

st = st.split(',')

for i in st:
	print(f"<option value='{i}'>{i}</option>")

